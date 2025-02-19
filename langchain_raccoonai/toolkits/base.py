from typing import List, Optional

from langchain_core.tools import BaseTool, BaseToolkit
from pydantic import ConfigDict
from raccoonai import RaccoonAI, AsyncRaccoonAI


class BaseRaccoonAIToolkit(BaseToolkit):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    client: Optional[RaccoonAI]
    async_client: Optional[AsyncRaccoonAI]

    def get_tools(self) -> List[BaseTool]:
        pass
