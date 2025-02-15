import json
from typing import Any, Optional, Literal

from langchain_core.callbacks import CallbackManagerForToolRun, AsyncCallbackManagerForToolRun
from langchain_core.tools import BaseTool


class BaseRaccoonAITool(BaseTool):

    def _run(self, *args: Any, **kwargs: Any) -> Any:
        pass

    def _arun(self, *args: Any, **kwargs: Any) -> Any:
        pass

    def _handle_stream(self, response_chunks, call_type: Literal['run', 'extract'], run_manager: Optional[CallbackManagerForToolRun]):
        final_result = None
        for line in response_chunks.response.iter_lines():
            chunk_data = json.loads(line)

            if run_manager and 'message' in chunk_data:
                run_manager.on_text(chunk_data['message'] + "\n")

            final_result = self._get_final_response(call_type, chunk_data)

        return final_result

    async def _ahandle_stream(self, response_chunks, call_type: Literal['run', 'extract'],
                              run_manager: Optional[AsyncCallbackManagerForToolRun]):
        final_result = None
        async for line in response_chunks.response.iter_lines():
            chunk_data = json.loads(line)

            if run_manager and 'message' in chunk_data:
                await run_manager.on_text(chunk_data['message'] + "\n")

            final_result = self._get_final_response(call_type, chunk_data)

        return final_result

    def _get_final_response(self, call_type: Literal['run', 'extract'], chunk_data: Any):
        match call_type:
            case 'run':
                if chunk_data.get('status', 'PROCESSING') == 'DONE':
                    return chunk_data.get('message')

                if chunk_data.get('status', 'PROCESSING') == 'FAILURE':
                    return chunk_data.get('message')
            case 'extract':
                if chunk_data.get('status', 'PROCESSING') == 'DONE':
                    return chunk_data.get('data', chunk_data.get('message'))

                if chunk_data.get('status', 'PROCESSING') == 'FAILURE':
                    return chunk_data.get('data', chunk_data.get('message'))
            case _:
                raise NotImplementedError
