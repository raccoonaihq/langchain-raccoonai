"""RaccoonAI tools."""

from typing import Optional, Type, Iterable

from langchain_core.callbacks import (
    CallbackManagerForToolRun,
    AsyncCallbackManagerForToolRun,
)
from langchain_core.tools import BaseTool
from pydantic import BaseModel

from raccoonai import RaccoonAI, AsyncRaccoonAI
from raccoonai.types import LamExtractParams, LamRunParams, FleetCreateParams


# --- Extraction Tool ---
class RaccoonAIExtractionTool(BaseTool):
    name: str = "RaccoonAI_Web_Extraction"
    description: str = """Useful for extracting structured data from web pages."""
    args_schema: Type[BaseModel] = LamExtractParams
    client: RaccoonAI
    async_client: AsyncRaccoonAI

    def _run(
            self,
            *,
            query: str,
            raccoon_passcode: str,
            schema: dict,
            app_url: Optional[str] = None,
            max_count: Optional[int] = None,
            advanced: Optional[dict] = None,
            chat_history: Optional[list] = None,
            stream: Optional[bool] = None,
            run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        try:
            response = self.client.lam.extract(
                query=query,
                raccoon_passcode=raccoon_passcode,
                schema=schema,
                app_url=app_url,
                max_count=max_count,
                advanced=advanced,
                chat_history=chat_history,
                stream=False,
            )
            return str(response.model_dump())
        except Exception as e:
            return f"Error during extraction: {e}"

    async def _arun(
            self,
            *,
            query: str,
            raccoon_passcode: str,
            schema: dict,
            app_url: Optional[str] = None,
            max_count: Optional[int] = None,
            advanced: Optional[dict] = None,
            chat_history: Optional[list] = None,
            stream: Optional[bool] = None,
            run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        try:
            response = await self.async_client.lam.extract(
                query=query,
                raccoon_passcode=raccoon_passcode,
                schema=schema,
                app_url=app_url,
                max_count=max_count,
                advanced=advanced,
                chat_history=chat_history,
                stream=False,
            )
            return str(response.model_dump())
        except Exception as e:
            return f"Error during extraction: {e}"

    def _stream(
            self,
            *,
            query: str,
            raccoon_passcode: str,
            schema: dict,
            app_url: Optional[str] = None,
            max_count: Optional[int] = None,
            advanced: Optional[dict] = None,
            chat_history: Optional[list] = None,
            run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> Iterable[str]:
        try:
            response_stream = self.client.lam.extract(
                query=query,
                raccoon_passcode=raccoon_passcode,
                schema=schema,
                app_url=app_url,
                max_count=max_count,
                advanced=advanced,
                chat_history=chat_history,
                stream=True,
            )
            for chunk in response_stream:
                if run_manager:
                    run_manager.on_tool_end(str(chunk.model_dump()))
                yield str(chunk.model_dump())

        except Exception as e:
            if run_manager:
                run_manager.on_tool_error(e)
            yield f"Error during extraction: {e}"

    async def _astream(
            self,
            *,
            query: str,
            raccoon_passcode: str,
            schema: dict,
            app_url: Optional[str] = None,
            max_count: Optional[int] = None,
            advanced: Optional[dict] = None,
            chat_history: Optional[list] = None,
            run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> Iterable[str]:
        try:
            response_stream = await self.async_client.lam.extract(
                query=query,
                raccoon_passcode=raccoon_passcode,
                schema=schema,
                app_url=app_url,
                max_count=max_count,
                advanced=advanced,
                chat_history=chat_history,
                stream=True,
            )
            async for chunk in response_stream:
                if run_manager:
                    await run_manager.on_tool_end(str(chunk.model_dump()))
                yield str(chunk.model_dump())

        except Exception as e:
            if run_manager:
                await run_manager.on_tool_error(e)
            yield f"Error during extraction: {e}"


# --- Run Tool ---
class RaccoonAIRunTool(BaseTool):
    name: str = "RaccoonAI_Web_Browsing"
    description: str = """Useful for browsing the web to gather information."""
    args_schema: Type[BaseModel] = LamRunParams
    client: RaccoonAI
    async_client: AsyncRaccoonAI

    def _run(
            self,
            *,
            query: str,
            raccoon_passcode: str,
            app_url: Optional[str] = None,
            advanced: Optional[dict] = None,
            chat_history: Optional[list] = None,
            stream: Optional[bool] = None,
            run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        try:
            response = self.client.lam.run(
                query=query,
                raccoon_passcode=raccoon_passcode,
                app_url=app_url,
                advanced=advanced,
                chat_history=chat_history,
                stream=False,
            )
            return str(response.model_dump())
        except Exception as e:
            return f"Error during browsing: {e}"

    async def _arun(
            self,
            *,
            query: str,
            raccoon_passcode: str,
            app_url: Optional[str] = None,
            advanced: Optional[dict] = None,
            chat_history: Optional[list] = None,
            run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        try:
            response = await self.async_client.lam.run(
                query=query,
                raccoon_passcode=raccoon_passcode,
                app_url=app_url,
                advanced=advanced,
                chat_history=chat_history,
                stream=False,
            )
            return str(response.model_dump())
        except Exception as e:
            return f"Error during browsing: {e}"

    def _stream(
            self,
            *,
            query: str,
            raccoon_passcode: str,
            app_url: Optional[str] = None,
            advanced: Optional[dict] = None,
            chat_history: Optional[list] = None,
            run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> Iterable[str]:
        try:
            response_stream = self.client.lam.run(
                query=query,
                raccoon_passcode=raccoon_passcode,
                app_url=app_url,
                advanced=advanced,
                chat_history=chat_history,
                stream=True,
            )
            for chunk in response_stream:
                if run_manager:
                    run_manager.on_tool_end(str(chunk.model_dump()))
                yield str(chunk.model_dump())

        except Exception as e:
            if run_manager:
                run_manager.on_tool_error(e)
            yield f"Error during browsing: {e}"

    async def _astream(
            self,
            *,
            query: str,
            raccoon_passcode: str,
            app_url: Optional[str] = None,
            advanced: Optional[dict] = None,
            chat_history: Optional[list] = None,
            run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> Iterable[str]:
        try:
            response_stream = await self.async_client.lam.run(
                query=query,
                raccoon_passcode=raccoon_passcode,
                app_url=app_url,
                advanced=advanced,
                chat_history=chat_history,
                stream=True,
            )
            async for chunk in response_stream:
                if run_manager:
                    await run_manager.on_tool_end(str(chunk.model_dump()))
                yield str(chunk.model_dump())

        except Exception as e:
            if run_manager:
                await run_manager.on_tool_error(e)
            yield f"Error during browsing: {e}"


# --- Session Tool ---
class RaccoonAISessionTool(BaseTool):
    name: str = "RaccoonAI_Playwright_Session"
    description: str = """Useful for creating a remote Playwright browser session."""
    args_schema: Type[BaseModel] = FleetCreateParams
    client: RaccoonAI
    async_client: AsyncRaccoonAI

    def _run(
            self,
            *,
            raccoon_passcode: Optional[str] = None,
            app_name: Optional[str] = None,
            url: Optional[str] = None,
            advanced: Optional[dict] = None,
            browser_type: Optional[str] = None,
            headless: Optional[bool] = None,
            session_timeout: Optional[int] = None,
            settings: Optional[dict] = None,
            run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        try:
            response = self.client.fleet.create(
                raccoon_passcode=raccoon_passcode,
                app_name=app_name,
                url=url,
                advanced=advanced,
                browser_type=browser_type,
                headless=headless,
                session_timeout=session_timeout,
                settings=settings,
            )
            return str(response.model_dump())
        except Exception as e:
            return f"Error creating session: {e}"

    async def _arun(
            self,
            *,
            raccoon_passcode: Optional[str] = None,
            app_name: Optional[str] = None,
            url: Optional[str] = None,
            advanced: Optional[dict] = None,
            browser_type: Optional[str] = None,
            headless: Optional[bool] = None,
            session_timeout: Optional[int] = None,
            settings: Optional[dict] = None,
            run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        try:
            response = await self.async_client.fleet.create(
                raccoon_passcode=raccoon_passcode,
                app_name=app_name,
                url=url,
                advanced=advanced,
                browser_type=browser_type,
                headless=headless,
                session_timeout=session_timeout,
                settings=settings,
            )
            return str(response.model_dump())
        except Exception as e:
            return f"Error creating session: {e}"
