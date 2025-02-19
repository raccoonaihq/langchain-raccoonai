from typing import Type, Dict
from unittest.mock import MagicMock, AsyncMock
from langchain_raccoonai.tools import RaccoonAIExtractTool, RaccoonAIRunTool
from langchain_tests.unit_tests import ToolsUnitTests
from raccoonai import RaccoonAI, AsyncRaccoonAI


class TestRaccoonAIExtractToolUnit(ToolsUnitTests):
    @property
    def tool_constructor(self) -> Type[RaccoonAIExtractTool]:
        return RaccoonAIExtractTool

    @property
    def tool_constructor_params(self) -> Dict:
        mock_client = MagicMock(spec=RaccoonAI)
        mock_client.lam = MagicMock()
        mock_client.lam.extract = MagicMock()

        mock_async_client = AsyncMock(spec=AsyncRaccoonAI)
        mock_async_client.lam = AsyncMock()
        mock_async_client.lam.extract = AsyncMock()

        return {
            "client": mock_client,
            "async_client": mock_async_client,
        }

    @property
    def tool_invoke_params_example(self) -> Dict:
        return {
            "query": "test query",
            "raccoon_passcode": "test_passcode",
            "app_url": "https://example.com",
            "response_schema": {"type": "object", "properties": {}},
            "max_count": 2,
        }


class TestRaccoonAIRunToolUnit(ToolsUnitTests):
    @property
    def tool_constructor(self) -> Type[RaccoonAIRunTool]:
        return RaccoonAIRunTool

    @property
    def tool_constructor_params(self) -> dict:
        mock_client = MagicMock(spec=RaccoonAI)
        mock_client.lam = MagicMock()
        mock_client.lam.run = MagicMock()

        mock_async_client = AsyncMock(spec=AsyncRaccoonAI)
        mock_async_client.lam = AsyncMock()
        mock_async_client.lam.run = AsyncMock()

        return {
            "client": mock_client,
            "async_client": mock_async_client,
        }

    @property
    def tool_invoke_params_example(self) -> dict:
        return {
            "query": "test query",
            "raccoon_passcode": "test_passcode",
            "app_url": "https://example.com",
        }