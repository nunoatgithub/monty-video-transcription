import random

from copilot import CopilotClient, CopilotSession
from postprocess.cleanup.abstract_cleanup import TranscriptCleanup


class CopilotCleanup(TranscriptCleanup):

    def __init__(self):
        super().__init__()
        self._client: CopilotClient | None = None
        self._model = "gpt-4.1"

    @property
    def model(self) -> str:
        return self._model

    @property
    def delay_secs(self) -> float:
        return random.randint(15, 60)

    async def close(self) -> None :
        if self._client is not None:
            await self._client.stop()
            self._client = None

    async def _call_llm(self, input_prompt: str) -> str:
        session = await self._get_cli_session()
        response = await session.send_and_wait({"prompt": input_prompt})
        return response.data.content

    async def _get_cli_session(self) -> CopilotSession:
        if self._client is None:
            self._client = CopilotClient()
            await self._client.start()
        return await self._client.create_session({"model": self._model})
