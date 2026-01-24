from __future__ import annotations

import asyncio

from langchain_text_splitters import RecursiveCharacterTextSplitter
from openai import OpenAI
from openai.types.responses import Response

from postprocess.cleanup.cleanup import CleanupContext, TranscriptCleanup


class OpenAICleanup(TranscriptCleanup):

    _SYSTEM_PROMPT = """
You are an audio transcription auditor for videos from the Thousand Brains Project YouTube channel. 

CONTEXT:
- The transcript may be too big, so what you get to audit are chunks, one at each request
- To help you understand the context of that chunk, a context object is provided in the input.
- That context object is comprised of 
    - the title, which may contain useful metadata (date, topic, speaker)
    - a description of the content of the video (the video whose chunk you are being provided)
    - the last parts of the previous chunk, if one exists. this chunk will already have been cleaned so there may be a discontinuity that you need to address in this chunk.
    - the first parts of the next chunk (non-cleaned yet), if one exists
- The Thousand Brains Project focuses on neuroscience-inspired AI, cortical columns, and the Monty sensorimotor learning system
- Audio transcriptions often contain homophone errors, unclear technical terms, and speech disfluencies

INSTRUCTIONS:
1. Rewrite the text provided to remove disfluencies (um, uh, you know, like, yeah),
2. Remove repeated phrases and false starts, fix punctuation and sentence boundaries,
and preserve the original meaning EXACTLY.
3. Preserve all important technical terms and names, and do not invent new content.
4. Keep meaning and domain terms unchanged
5. Do not add summaries or explanations
6. DO NOT SUMMARIZE THE CONTENT.
7. Output only the cleaned transcript, and do so in markdown format (if you introduce new lines do so with two new line chars, not just one).
8. Do not include any content from the previous or next chunks, if they are present.
9. The previous and next chunks are only there to allow you to produce the same text fluency that would be possible were you to have the full transcript in one go.

OUTPUT REQUIREMENTS:
- Valid GitHub-Flavored Markdown only
- No code fences, explanatory preambles, or meta-commentary
- No closing remarks or summaries beyond the content itself
- No final notes listing corrections from transcript.
- Begin directly with the refined content.
- Remember, the text you produce will be concatenated as is to the results of the previous chunk.
    """

    def __init__(self):
        self._openai = OpenAI()
        self._model = "gpt-4o-mini"
        self._text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=7000,
            chunk_overlap=0,
            separators=["\n\n", "."],
            keep_separator=True,
            strip_whitespace=False
        )
        self._words_in_previous_chunk = 20
        self._words_in_next_chunk = 20

    async def clean(self, transcription: str, description: str, title: str) -> str:
        return await asyncio.to_thread(self._clean, transcription, description, title)

    async def close(self) -> None:
        return await asyncio.to_thread(self._openai.close)

    @property
    def model(self) -> str:
        return self._model

    @property
    def delay_secs(self) -> float:
        return 0

    def _clean(self, transcription:str, description:str, title:str) -> str:

        chunks: list[str] = self._text_splitter.split_text(transcription)
        clean_chunks: list[str] = []
        for i, chunk in enumerate(chunks):
            previous_chunk = ""
            next_chunk = ""
            if i > 0:
                previous_chunk = clean_chunks[i - 1]
            if i < len(chunks) - 1:
                next_chunk = chunks[i + 1]

            context = self._build_chunk_context(description, title, previous_chunk, next_chunk)
            input_prompt = self._build_input_prompt(chunk, context)
            clean_chunk = self._cleanup_with_llm(input_prompt)

            # Preserve any leading newlines from the original chunk (distinguish single vs double).
            leading_newlines_count = len(chunk) - len(chunk.lstrip("\n"))
            if leading_newlines_count:
                leading_newlines = "\n" * leading_newlines_count
                if not clean_chunk.startswith(leading_newlines):
                    clean_chunk = leading_newlines + clean_chunk

            clean_chunks.append(clean_chunk)

        return "".join(clean_chunks)

    def _build_chunk_context(
            self,
            description: str,
            title: str,
            previous_chunk: str,
            next_chunk: str
    ) -> CleanupContext:

        def get_last_words(text: str, count: int) -> str:
            """ get last 'count' words, including special chars"""
            if not text:
                return ""
            words = text.strip().split()
            if len(words) <= count:
                return " ".join(words)
            return " ".join(words[-count:])

        def get_first_words(text: str, count: int) -> str:
            """ get first 'count' words, including special chars"""
            if not text:
                return ""
            words = text.strip().split()
            if len(words) <= count:
                return " ".join(words)
            return " ".join(words[:count])

        last_words = get_last_words(previous_chunk, self._words_in_previous_chunk)
        first_words = get_first_words(next_chunk, self._words_in_next_chunk)
        return CleanupContext(description or "", title or "", last_words, first_words)

    @staticmethod
    def _build_input_prompt(chunk: str, context: CleanupContext) -> str:
        return f"""
CHUNK_CONTEXT:
    File title: {context.title}
    Description: {context.description}
    Previous chunk last words: {context.previous_chunk_last_words}
    Next chunk first words: {context.next_chunk_first_words}
    
Chunk to clean:
{chunk}
"""

    def _cleanup_with_llm(self, input_prompt:str) -> str :
        response: Response = self._openai.responses.create(
            model = self.model,
            instructions=self._SYSTEM_PROMPT,
            input=input_prompt,
            temperature=0
        )
        return response.output_text
