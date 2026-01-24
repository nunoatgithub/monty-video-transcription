import abc
import argparse
import asyncio
import signal
from dataclasses import dataclass
from pathlib import Path

from youtube.info import YouTubeVideoInfo

@dataclass
class CleanupContext:
    description: str
    title: str
    previous_chunk_last_words: str
    next_chunk_first_words: str

class TranscriptCleanup(abc.ABC):

    @abc.abstractmethod
    async def clean(self, transcription: str, description: str, title: str) -> str:
        ...

    @abc.abstractmethod
    async def close(self) -> None:
        ...

    @property
    @abc.abstractmethod
    def model(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def delay_secs(self) -> float:
        """Return a polite delay between requests."""
        ...

#----------------------------------------------------------------

shutdown_event: asyncio.Event | None = None

def create_signal_handler():
    """Create a signal handler that triggers graceful shutdown."""
    def signal_handler(sig, frame):
        print("\nShutting down...")
        if shutdown_event is not None:
            shutdown_event.set()
    return signal_handler

async def main():
    global shutdown_event
    shutdown_event = asyncio.Event()

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("input_path", help="Single transcript file or folder containing multiple such files")
    args = parser.parse_args()

    if not args.input_path:
        parser.error("You must provide a transcript input_path.")

    input_path = Path(args.input_path)

    filenames: list[str] = []
    if input_path.is_file():
        filenames.append(input_path.stem)
    elif input_path.is_dir():
        for md_path in input_path.glob("*.md"):
            filenames.append(md_path.stem)
    else:
        raise ValueError(f"Input path does not exist: {input_path}")

    # import the implementation here to avoid a circular import at module import time
    from postprocess.cleanup.copilot_cleanup import CopilotCleanup

    transcript_cleanup: TranscriptCleanup = CopilotCleanup()

    # Register signal handler for graceful shutdown
    signal.signal(signal.SIGINT, create_signal_handler())

    try :
        for i, filename in enumerate(filenames):

            if shutdown_event.is_set():
                print("Shutdown requested, stopping...")
                break

            target_path = Path(__file__).parent.parent.parent.parent / f"post-processed/{filename}.cp.{transcript_cleanup.model}.clean.md"
            if target_path.exists():
                print(f"Clean transcript {target_path} already exists, skipped.")
                continue

            video_info_path = Path(
                __file__).parent.parent.parent.parent / f"youtube/info/{filename}.json"
            video_definition = YouTubeVideoInfo.from_file(video_info_path)

            transcript_path = Path(
                __file__).parent.parent.parent.parent / f"youtube/transcripts/{filename}.md"

            with open(transcript_path, "r") as f:
                transcription = f.read()

            print(f"Processing {filename}...")
            result = await transcript_cleanup.clean(transcription, video_definition.description, video_definition.title)

            with open(target_path, "w", encoding="utf-8") as f:
                f.write(result)
                print(f"Clean transcript saved: {str(target_path)}")

            await asyncio.sleep(transcript_cleanup.delay_secs)


    finally:
        await transcript_cleanup.close()


if __name__ == "__main__":
    asyncio.run(main())