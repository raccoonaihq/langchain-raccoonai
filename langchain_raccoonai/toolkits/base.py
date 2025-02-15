from typing import List

from langchain_core.tools import BaseTool, BaseToolkit

from raccoonai import RaccoonAI, AsyncRaccoonAI


class BaseRaccoonAIToolkit(BaseToolkit):

    class Config:
        arbitrary_types_allowed = True

    client: RaccoonAI
    async_client: AsyncRaccoonAI

    def get_tools(self) -> List[BaseTool]:
        pass
