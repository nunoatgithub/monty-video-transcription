import asyncio

from openai import OpenAI
from openai.types.responses import Response

from postprocess.cleanup.abstract_cleanup import TranscriptCleanup


class OpenAICleanup(TranscriptCleanup):

    def __init__(self):
        super().__init__()
        self._openai = OpenAI()
        self._model = "gpt-4o-mini"

    async def close(self) -> None:
        await asyncio.to_thread(self._openai.close)

    @property
    def model(self) -> str:
        return self._model

    @property
    def delay_secs(self) -> float:
        return 0

    async def _call_llm(self, input_prompt: str) -> str :
        response: Response = await asyncio.to_thread(
            self._openai.responses.create,
            model=self.model,
            instructions=self._SYSTEM_PROMPT,
            input=input_prompt,
            temperature=0
        )
        return response.output_text
