from __future__ import annotations

import argparse
import json
import random
import re
import time
import traceback
from pathlib import Path

from torch import manual_seed
from youtube_transcript_api import YouTubeTranscriptApi, FetchedTranscript, NoTranscriptFound

from youtube.info import YouTubeVideoInfo

class YouTubeTranscript:

    _ytt_api = None
    _TRANSCRIPTS_DIR = Path(__file__).parent.parent.parent / "youtube" / "transcripts"

    def __init__(self, title: str, video_id:str, fetched_transcript: list[dict]) -> None:
        self.title = title
        self.video_id = video_id
        self.fetched_transcript = fetched_transcript
        self._path: Path | None = None

    @property
    def path(self) -> Path:
        if self._path is None:
            self._path = self._TRANSCRIPTS_DIR / f"{self.title}.{self.video_id}.json"
        return self._path

    def process(self):
        md_path = self.path.parent / Path(self.path.stem + ".md")
        if md_path.exists():
            print(f"Pre-processed transcript {self.title} already exists.")
        else:
            preproc_transcript = self._to_pre_processed_str()
            with open(md_path, "w") as f:
                f.write(preproc_transcript)
            print(f"Pre-processed transcript saved: {str(md_path)}")

    @staticmethod
    def load_transcript_from_file(path: Path) -> YouTubeTranscript | None:
        try:
            title, video_id, _ = path.name.rsplit('.')
            with open(path) as f:
                fetched_transcript = json.load(f)
                return YouTubeTranscript(title, video_id, fetched_transcript)
        except Exception as e:
            print(f"ERROR: Failed to load transcript from path {path}: {e}")
            traceback.print_exc()
            return None

    @staticmethod
    def fetch_or_load_transcript(video_info: YouTubeVideoInfo) -> tuple[YouTubeTranscript, bool]:
        """Fetch or load a YouTube transcript for the given video info.
           Returns the transcript plus a flag indicating whether it was fetched (true) or loaded.
        """
        path = YouTubeTranscript._find_existing_raw_transcript(video_info)
        if path is not None:
            print(f"Transcript {video_info.title} already exists, loading it from file {path}...")
            return YouTubeTranscript.load_transcript_from_file(path), False
        else:
            # manual transcripts are much metter quality,
            # if they exist we need to use their language as a fetching key
            transcript_list = YouTubeTranscript._get_ytt_appi().list(video_info.video_id)
            try:
                manual_transcript = transcript_list.find_manually_created_transcript(['en-US', 'en'])
                languages = [manual_transcript.language_code]
            except NoTranscriptFound:
                languages = ['en-US', 'en']

            fetched_transcript = YouTubeTranscript._get_ytt_appi().fetch(video_info.video_id, languages=languages)
            transcript = YouTubeTranscript(
                video_info.title,
                video_info.video_id,
                fetched_transcript.to_raw_data()
            )
            transcript._save()
            return transcript, True

    def _save(self) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.fetched_transcript, f, indent=4)
        print(f"YouTube transcript saved: {str(self.path)}")

    def _to_pre_processed_str(self, silence_threshold: float = 2) -> str:
        """Convert the transcript to a text string.

        Processing steps:
        1. Concatenate all text fields, inserting newlines based on silence gaps
        2. Apply sequential text replacements:
           - Replace ellipsis with three dots
           - Remove bracketed content like [Music]
           - Remove forbidden characters
           - Normalize whitespace (preserve newlines)
           - Fix spaces before punctuation
           - Insert newlines before speaker labels

        Args:
            silence_threshold: Minimum silence gap (in seconds) between entries
                               to trigger a newline. Defaults to 1.2 seconds.
        Returns:
            The transcript as a formatted text string.
        """
        if not self.fetched_transcript:
            return ""

        # Step 1: Concatenate all text fields with appropriate separators (space or newline)
        parts = []
        for i, entry in enumerate(self.fetched_transcript):
            text = entry.get("text", "")
            if not text.strip():
                continue

            # Clean internal newlines in this text field
            text = text.replace("\n", " ")

            if i == 0:
                parts.append(text)
            else:
                prev_entry = self.fetched_transcript[i - 1]
                prev_end = prev_entry.get("start", 0) + prev_entry.get("duration", 0)
                curr_start = entry.get("start", 0)
                silence_gap = curr_start - prev_end

                # Only insert paragraph break if silence gap AND previous text ended a sentence
                prev_text = prev_entry.get("text", "").strip()
                prev_ends_sentence = prev_text and prev_text[-1] in '.?!'

                if silence_gap > silence_threshold and prev_ends_sentence:
                    parts.append("\n\n")
                else:
                    parts.append(" ")
                parts.append(text)

        result = "".join(parts)

        # Step 2: Sequential replacement passes
        # 2a. Replace ellipsis character with three dots
        result = result.replace("…", "...")
        # 2b. Remove bracketed content like [Music]
        result = re.sub(r'\[.*?]', '', result)
        # 2c. Remove forbidden characters (keep alphanumerics, space, newline, and common punctuation)
        result = re.sub(r"[^A-Za-z0-9 \n,?\"'\-.:]", '', result)
        # 2d. Normalize whitespace (but preserve newlines for paragraph breaks)
        result = re.sub(r'[^\S\n]+', ' ', result)
        # 2e. Fix spaces before punctuation (from removed content)
        result = re.sub(r' ([.?!,;:])', r'\1', result)

        # 2f. Two-pass speaker normalization
        # Pass 1: Discover all speaker labels - find patterns like "Name:" or "First Last:"
        # Only at start of text, after newline, or after sentence-ending punctuation
        # Pattern allows mixed case names like "JHawkins" or "Niels Leadholm"
        speaker_pattern = re.compile(r'(?:^|[\n.!?])\s*([A-Z][a-zA-Z]*(?:\s+[A-Z][a-zA-Z]*)*):')
        all_matches = speaker_pattern.findall(result)
        # Count occurrences - real speakers appear multiple times
        from collections import Counter
        speaker_counts = Counter(all_matches)
        # Common words that should not be treated as speaker names
        common_words = {'And', 'But', 'The', 'This', 'That', 'Or', 'So', 'If', 'As', 'It', 'In', 'On', 'At', 'To', 'For', 'With', 'By', 'From', 'About', 'Into'}
        # Build a dict: last word -> longest full name (only for names appearing 2+ times)
        speakers = {}
        for match, count in speaker_counts.items():
            if count < 2:
                continue
            # Skip if first word is a common word
            first_word = match.split()[0]
            if first_word in common_words:
                continue
            last_word = match.split()[-1]
            if last_word not in speakers or len(match) > len(speakers[last_word]):
                speakers[last_word] = match

        # Get unique full speaker names
        speaker_names = set(speakers.values())

        # Pass 2: For each speaker, add blank line before their label
        # Process longer names first to avoid partial replacements
        for speaker in sorted(speaker_names, key=len, reverse=True):
            # Replace all occurrences of "Speaker:" with newline before it
            # Handles: start of string, after space, after punctuation
            result = re.sub(rf'(\s|^){re.escape(speaker)}:', f'\n\n{speaker}:', result)

        # Clean up: normalize multiple newlines to double (paragraph break) and remove leading newlines
        result = re.sub(r'\n{2,}', '\n\n', result)
        result = result.lstrip('\n')

        return result

    @staticmethod
    def _find_existing_raw_transcript(video_info: YouTubeVideoInfo) -> Path | None:
        for path in YouTubeTranscript._TRANSCRIPTS_DIR.glob(f"*.{video_info.video_id}.json"):
            return path
        return None

    @staticmethod
    def _get_ytt_appi():
        if YouTubeTranscript._ytt_api is None:
            YouTubeTranscript._ytt_api = YouTubeTranscriptApi()
        return YouTubeTranscript._ytt_api

def main():
    parser = argparse.ArgumentParser(description="YouTube transcription with Whisper")
    parser.add_argument("input_path", help="Single video_info file or folder containing multiple such files")
    args = parser.parse_args()

    input_path = Path(args.input_path)

    video_infos: list[YouTubeVideoInfo] = []
    if input_path.is_file():
        video_info = YouTubeVideoInfo.from_file(input_path)
        video_infos.append(video_info)
    elif input_path.is_dir():
        for video_info in input_path.glob("*.json"):
            video_infos.append(YouTubeVideoInfo.from_file(video_info))
    else:
        raise ValueError(f"Input path does not exist: {input_path}")

    for i, video_info in enumerate(video_infos):
        raw_transcript, fetched = YouTubeTranscript.fetch_or_load_transcript(video_info)
        raw_transcript.process()
        if fetched and i + 1 < len(video_infos):
            time.sleep(random.randint(30, 60)) # otherwise you get your IP blocked...

if __name__ == "__main__":
    main()