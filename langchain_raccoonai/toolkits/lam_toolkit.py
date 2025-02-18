from typing import List

from langchain_core.tools import BaseTool

from langchain_raccoonai.tools import RaccoonAIExtractTool, RaccoonAIRunTool
from .base import BaseRaccoonAIToolkit


class RaccoonAILAMToolkit(BaseRaccoonAIToolkit):

    def get_tools(self) -> List[BaseTool]:
        return [
            RaccoonAIExtractTool(client=self.client, async_client=self.async_client),
            RaccoonAIRunTool(client=self.client, async_client=self.async_client),
        ]
