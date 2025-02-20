from typing import Optional, Type, Any

from langchain_core.callbacks import (
    CallbackManagerForToolRun,
    AsyncCallbackManagerForToolRun,
)
from pydantic import Field
from raccoonai import RaccoonAI, AsyncRaccoonAI

from .base import BaseRaccoonAITool
from ..models import RunParams


class RaccoonAIRunTool(BaseRaccoonAITool):
    name: str = "raccoonai_browse_web"
    description: str = """
        Specialized tool for extracting structured data into specific formats. ONLY use this when you need:
        - Data in a specific JSON schema or structure
        - Multiple items in the same format (like product listings, news/posts)
        - Consistent fields extracted from web pages
        - Converting web content into structured formats
        For general web browsing or question-answering, use raccoonai_browse_web instead.
        """
    args_schema: Type[RunParams] = RunParams
    client: Optional[RaccoonAI] = Field(
        default=None,
        exclude=True
    )
    async_client: Optional[AsyncRaccoonAI] = Field(
        default=None,
        exclude=True
    )

    def _run(
            self,
            query: str,
            raccoon_passcode: str,
            app_url: Optional[str] = None,
            run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> Any:
        try:
            if not self.client:
                raise ValueError("You must pass RaccoonAI client while initializing.")
            with self.client.lam.run(
                    query=query,
                    raccoon_passcode=raccoon_passcode,
                    stream=True,
                    app_url=app_url
            ) as response_chunks:
                return self._handle_stream(response_chunks, run_manager)

        except Exception as e:
            if run_manager:
                run_manager.on_tool_error(e)
            raise

    async def _arun(
            self,
            query: str,
            raccoon_passcode: str,
            app_url: Optional[str] = None,
            run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> Any:
        try:
            if not self.async_client:
                raise ValueError("You must pass AsyncRaccoonAI client while initializing.")
            async with await self.async_client.lam.run(
                    query=query,
                    raccoon_passcode=raccoon_passcode,
                    stream=True,
                    app_url=app_url
            ) as response_chunks:
                return await self._ahandle_stream(response_chunks, run_manager)

        except Exception as e:
            if run_manager:
                await run_manager.on_tool_error(e)
            raise
