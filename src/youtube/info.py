from __future__ import annotations

import argparse
import json
import re
import traceback
from pathlib import Path

import yt_dlp

class YouTubeVideoInfo:

    _VIDEO_INFO_DIR = Path(__file__).parent.parent.parent / "data/youtube/info"

    def __init__(self, url: str, metadata: dict) -> None:
        self.url = url
        self.metadata = metadata
        self._path: Path | None = None
        self._title: str | None = None
        self._video_id: str | None = None

    @property
    def path(self) -> Path:
        if self._path is None:
            self._path = self._VIDEO_INFO_DIR / f"{self.title}.{self.video_id}.json"
        return self._path

    @property
    def video_id(self) -> str:
        if self._video_id is None:
            self._video_id = self.metadata["id"]
        return self._video_id

    @property
    def title(self) -> str:
        if self._title is None:
            metadata_title = self.metadata['title']
            self._title = self._sanitize_title(metadata_title)
        return self._title

    @property
    def description(self):
        metadata_description = self.metadata.get("description") or ""
        return metadata_description.split("\n\n")[0]

    @staticmethod
    def from_file(path: Path) -> YouTubeVideoInfo | None:
        try:
            with open(path) as f:
                json_data = json.load(f)
                return YouTubeVideoInfo(json_data["url"], json_data["metadata"])
        except Exception as e:
            print(f"ERROR: Failed to get video info for path {path}: {e}")
            traceback.print_exc()
            return None

    @staticmethod
    def from_url(url: str) -> YouTubeVideoInfo | None:
        path = YouTubeVideoInfo._find_existing(url)
        if path is not None:
            print(f"Info about {url} already exists, loading it from file {path}...")
            return YouTubeVideoInfo.from_file(path)
        else:
            try:
                with yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True}) as ydl:
                    metadata = ydl.extract_info(url, download=False)
                video_info = YouTubeVideoInfo(url, metadata)
                video_info._save()
                return video_info
            except Exception as e:
                print(f"ERROR: Failed to fetch video info for {url}: {e}")
                traceback.print_exc()
                return None

    def _save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump({"url": self.url, "metadata": self.metadata}, f, indent=4)
        print(f"Video info saved: {str(self.path)}")

    @staticmethod
    def _sanitize_title(title: str) -> str:
        """Replace non-alphanumeric chars with underscores, collapse repeats, and trim trailing underscores."""
        sanitized = re.sub(r"[^A-Za-z0-9]", "_", title)
        sanitized = re.sub(r"_+", "_", sanitized)
        return sanitized.rstrip("_")

    @staticmethod
    def _extract_video_id(url: str) -> str | None:
        """Extract video ID from a YouTube URL."""
        # Handle various YouTube URL formats
        patterns = [
            r'(?:v=|/v/|youtu\.be/)([a-zA-Z0-9_-]{11})',
            r'(?:embed/)([a-zA-Z0-9_-]{11})',
            r'^([a-zA-Z0-9_-]{11})$',  # Just the video ID
        ]
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        return None

    @staticmethod
    def _find_existing(url: str) -> Path | None:
        video_id = YouTubeVideoInfo._extract_video_id(url)
        for path in YouTubeVideoInfo._VIDEO_INFO_DIR.glob(f"*.{video_id}.json"):
            return path
        return None

class YouTubeChannel:

    def __init__(self, url: str) -> None:
        self.url = url

    def fetch_video_info(self) -> list[YouTubeVideoInfo]:
        video_urls = self._get_youtube_channel_video_urls()
        video_info = []
        for url in video_urls:
            info = YouTubeVideoInfo.from_url(url)
            if info is not None:
                video_info.append(info)
        return video_info

    def _get_youtube_channel_video_urls(self) -> list[str]:
        """Get all video URLs from a YouTube channel."""
        ydl_opts = {
            "quiet": True,
            "extract_flat": True,  # only metadata, no downloads
            "skip_download": True,
        }

        urls = []
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(self.url, download=False)
            entries = info.get("entries", [])
            for entry in entries:
                if entry:
                    url = entry.get("webpage_url") or entry.get("url")
                    if url:
                        urls.append(url)
        return urls

def main():
    parser = argparse.ArgumentParser(
        description="Download info about YouTube videos"
    )
    parser.add_argument("channel", nargs="?", help="URL of a YouTube channel")
    args = parser.parse_args()

    if not args.channel:
        parser.error("You must provide a YouTube channel URL.")

    print(f"Fetching video list from channel: {args.channel}")
    video_info = YouTubeChannel(args.channel).fetch_video_info()
    print(f"Fetched information for {len(video_info)} videos in the channel")

if __name__ == "__main__":
    main()