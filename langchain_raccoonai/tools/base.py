import json
from typing import Any, Optional

from langchain_core.callbacks import CallbackManagerForToolRun, AsyncCallbackManagerForToolRun
from langchain_core.tools import BaseTool


class BaseRaccoonAITool(BaseTool):

    def _run(self, *args: Any, **kwargs: Any) -> Any:
        pass

    def _arun(self, *args: Any, **kwargs: Any) -> Any:
        pass

    def _handle_stream(self, response_chunks, run_manager: Optional[CallbackManagerForToolRun]):
        final_result = None
        for chunk in response_chunks.response.iter_lines():
            chunk_json = json.loads(chunk)
            if run_manager:
                run_manager.on_text(chunk_json)
                run_manager.on_text("\n")

            if chunk_json.get("task_status", "PROCESSING") in ["DONE", "FAILURE"]:
                final_result = chunk_json
                break

        return final_result

    async def _ahandle_stream(self, response_chunks, run_manager: Optional[AsyncCallbackManagerForToolRun]):
        final_result = None
        async for chunk in response_chunks.response.aiter_lines():
            chunk_json = json.loads(chunk)
            if run_manager:
                await run_manager.on_text(chunk_json)
                await run_manager.on_text("\n")

            if chunk_json.get("task_status", "PROCESSING") in ["DONE", "FAILURE"]:
                final_result = chunk_json
                break

        return final_result
