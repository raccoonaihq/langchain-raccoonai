"""RaccoonAI toolkits."""

from typing import List

from langchain_core.tools import BaseTool, BaseToolkit

from raccoonai import RaccoonAI, AsyncRaccoonAI
from langchain_raccoonai.tools import RaccoonAIExtractionTool, RaccoonAIRunTool, RaccoonAISessionTool


class RaccoonAIToolkit(BaseToolkit):
    """RaccoonAI toolkit."""

    client: RaccoonAI
    async_client: AsyncRaccoonAI

    def get_tools(self) -> List[BaseTool]:
        """Return a list of tools this toolkit provides."""
        return [
            RaccoonAIExtractionTool(client=self.client, async_client=self.async_client),
            RaccoonAIRunTool(client=self.client, async_client=self.async_client),
            RaccoonAISessionTool(client=self.client, async_client=self.async_client),
        ]