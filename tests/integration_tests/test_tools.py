import pytest
from typing import Type, Dict
from langchain_raccoonai.tools import RaccoonAIExtractTool, RaccoonAIRunTool
from langchain_tests.integration_tests import ToolsIntegrationTests
from raccoonai import RaccoonAI, AsyncRaccoonAI
import os
from dotenv import load_dotenv

load_dotenv()

RACCOON_SECRET_KEY = os.getenv("RACCOON_SECRET_KEY")
if not RACCOON_SECRET_KEY:
    pytest.skip("RACCOON_SECRET_KEY environment variable not set.", allow_module_level=True)


class TestRaccoonAIExtractToolIntegration(ToolsIntegrationTests):
    @property
    def tool_constructor(self) -> Type[RaccoonAIExtractTool]:
        return RaccoonAIExtractTool

    @property
    def tool_constructor_params(self) -> Dict:
        return {
            "client": RaccoonAI(timeout=3000, max_retries=0),
            "async_client": AsyncRaccoonAI(timeout=3000, max_retries=0),
        }

    @property
    def tool_invoke_params_example(self) -> Dict:
        return {
            "query": "Find me top hacker news post today.",
            "raccoon_passcode": "platformraccoonchat",
            "app_url": "https://news.ycombinator.com/",
            "response_schema": {
                "title": {
                    "type": "text",
                    "description": "Title of the post."
                },
                "author": {
                    "type": "string",
                    "description": "Author of the post."
                }
            },
            "max_count": 1,
        }


class TestRaccoonAIRunToolIntegration(ToolsIntegrationTests):
    @property
    def tool_constructor(self) -> Type[RaccoonAIRunTool]:
        return RaccoonAIRunTool

    @property
    def tool_constructor_params(self) -> Dict:
        return {
            "client": RaccoonAI(timeout=3000, max_retries=0),
            "async_client": AsyncRaccoonAI(timeout=3000, max_retries=0),
        }

    @property
    def tool_invoke_params_example(self) -> Dict:
        return {
            "query": "Go to the YCombinator website and find information about what they are up to.",
            "raccoon_passcode": "platformraccoonchat",
            "app_url": "https://www.ycombinator.com",
        }
