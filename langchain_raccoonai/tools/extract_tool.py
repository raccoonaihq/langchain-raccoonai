from typing import Optional, Type, Any, Dict

from langchain_core.callbacks import (
    CallbackManagerForToolRun,
    AsyncCallbackManagerForToolRun,
)
from pydantic import Field
from raccoonai import RaccoonAI, AsyncRaccoonAI
from raccoonai.types import lam_extract_params

from .base import BaseRaccoonAITool
from ..models import ExtractParams


class RaccoonAIExtractTool(BaseRaccoonAITool):
    name: str = "raccoonai_extract_web_data"
    description: str = """
        Extracts structured data from web pages in a given response_schema using RaccoonAI. Useful for:
        - Scraping product information from e-commerce sites
        - Gathering contact details from business directories
        - Collecting article metadata from news sites
        - Converting webpages into structured data
        - Getting any available information on the web in a structured format
        """
    args_schema: Type[ExtractParams] = ExtractParams
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
            *,
            query: str,
            raccoon_passcode: str,
            app_url: Optional[str] = None,
            response_schema: Optional[Dict[str, Any]] = None,
            max_count: Optional[int] = 2,
            run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> Any:
        try:
            if not self.client:
                raise ValueError("You must pass RaccoonAI client while initializing.")
            with self.client.lam.extract(
                    query=query,
                    raccoon_passcode=raccoon_passcode,
                    app_url=app_url,
                    schema=response_schema,
                    max_count=max_count,
                    stream=True,
                    advanced=lam_extract_params.Advanced(
                        proxy=False,
                        solve_captchas=True,
                        block_ads=True
                    ),
            ) as response_chunks:
                return self._handle_stream(response_chunks, run_manager)

        except Exception as e:
            if run_manager:
                run_manager.on_tool_error(e)
            raise

    async def _arun(
            self,
            *,
            query: str,
            raccoon_passcode: str,
            app_url: Optional[str] = None,
            response_schema: Dict[str, Any],
            max_count: Optional[int] = 2,
            run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> Any:
        try:
            if not self.async_client:
                raise ValueError("You must pass AsyncRaccoonAI client while initializing.")
            async with await self.async_client.lam.extract(
                    query=query,
                    raccoon_passcode=raccoon_passcode,
                    app_url=app_url,
                    schema=response_schema,
                    max_count=max_count,
                    stream=True,
                    advanced=lam_extract_params.Advanced(
                        proxy=False,
                        solve_captchas=True,
                        block_ads=True
                    )) as response_chunks:
                return await self._ahandle_stream(response_chunks, run_manager)

        except Exception as e:
            if run_manager:
                await run_manager.on_tool_error(e)
            raise
