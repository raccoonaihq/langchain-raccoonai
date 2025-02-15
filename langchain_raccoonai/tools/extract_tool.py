from .base import BaseRaccoonAITool
from typing import Optional, Type, Any, Dict

from langchain_core.callbacks import (
    CallbackManagerForToolRun,
    AsyncCallbackManagerForToolRun,
)
from pydantic import BaseModel, Field

from raccoonai import RaccoonAI, AsyncRaccoonAI
from raccoonai.types import LamExtractParams


class RaccoonAIExtractTool(BaseRaccoonAITool):
    name: str = "extract_web_data"
    description: str = """
        Extracts structured data from web pages using RaccoonAI. Useful for:
        - Scraping product information from e-commerce sites
        - Gathering contact details from business directories
        - Collecting article metadata from news sites
        - Converting webpages into structured data
        - Getting any available information on the web in a structured format
        """
    args_schema: Type[BaseModel] = LamExtractParams
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
                with self.client.lam.extract(**kwargs) as response_chunks:
                    return self._handle_stream(response_chunks, 'extract', run_manager)
            else:
                return self.client.lam.extract(stream=False, **kwargs)

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
                async with await self.async_client.lam.extract(**kwargs) as response_chunks:
                    return await self._ahandle_stream(response_chunks, 'extract', run_manager)
            else:
                return await self.async_client.lam.extract(stream=False, **kwargs)

        except Exception as e:
            if run_manager:
                await run_manager.on_tool_error(e)
            raise
