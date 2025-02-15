from .base import BaseRaccoonAITool
from typing import Optional, Type, Any, Dict

from langchain_core.callbacks import (
    CallbackManagerForToolRun,
    AsyncCallbackManagerForToolRun,
)
from pydantic import BaseModel, Field

from raccoonai import RaccoonAI, AsyncRaccoonAI
from raccoonai.types import LamRunParams


class RaccoonAIRunTool(BaseRaccoonAITool):
    name: str = "browse_web"
    description: str = """
        Navigates and interacts with websites using RaccoonAI. Best for:
        - Searching and collecting information across multiple pages
        - Following links and navigating website hierarchies
        - Interacting with dynamic web content
        - Executing complex web browsing sequences
        """
    args_schema: Type[BaseModel] = LamRunParams
    client: RaccoonAI = Field(exclude=True)
    async_client: AsyncRaccoonAI = Field(exclude=True)

    def _run(
            self,
            run_manager: Optional[CallbackManagerForToolRun] = None,
            **kwargs: Dict[str, Any],
    ) -> Any:
        try:
            stream = kwargs.get('stream', False)

            if stream:
                with self.client.lam.run(**kwargs) as response_chunks:
                    return self._handle_stream(response_chunks, 'run', run_manager)
            else:
                return self.client.lam.run(stream=False, **kwargs)

        except Exception as e:
            if run_manager:
                run_manager.on_tool_error(e)
            raise

    async def _arun(
            self,
            run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
            **kwargs: Dict[str, Any],
    ) -> Any:
        try:
            stream = kwargs.get('stream', False)

            if stream:
                async with await self.async_client.lam.run(**kwargs) as response_chunks:
                    return await self._ahandle_stream(response_chunks, 'run', run_manager)
            else:
                return await self.async_client.lam.run(stream=False, **kwargs)

        except Exception as e:
            if run_manager:
                await run_manager.on_tool_error(e)
            raise
