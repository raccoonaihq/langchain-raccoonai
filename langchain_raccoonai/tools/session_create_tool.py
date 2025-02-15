from .base import BaseRaccoonAITool
from typing import Type, Any

from pydantic import BaseModel, Field

from raccoonai import RaccoonAI, AsyncRaccoonAI
from raccoonai.types import FleetCreateParams


class RaccoonAISessionCreateTool(BaseRaccoonAITool):
    name: str = "create_browser_session"
    description: str = """
        Creates remote browser sessions for automated web interaction. Use when you need:
        - Direct browser control via CDP (Chrome DevTools Protocol)
        - Custom browser automation with Playwright
        - Persistent browsing sessions
        Returns a WebSocket URL in its response for connecting Playwright or Puppeteer over CDP.
        """
    args_schema: Type[BaseModel] = FleetCreateParams
    client: RaccoonAI = Field(exclude=True)
    async_client: AsyncRaccoonAI = Field(exclude=True)

    def _run(self, **kwargs) -> Any:
        return self.client.fleet.create(**kwargs)

    async def _arun(self, **kwargs) -> Any:
        return await self.async_client.fleet.create(**kwargs)
