from typing import List

from langchain_core.tools import BaseTool

from .base import BaseRaccoonAIToolkit
from langchain_raccoonai.tools import RaccoonAISessionCreateTool


class RaccoonAIFleetToolkit(BaseRaccoonAIToolkit):

    def get_tools(self) -> List[BaseTool]:
        return [
            RaccoonAISessionCreateTool(client=self.client, async_client=self.async_client),
        ]
