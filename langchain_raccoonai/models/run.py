from typing import Optional

from pydantic import BaseModel, Field


class RunParams(BaseModel):
    query: str = Field(
        description="The input query for the task.",
        examples=["Find YCombinator startups funded in W24."]
    )
    raccoon_passcode: str = Field(
        ...,
        description="The raccoon_passcode provided by the user alongside the query for end user identification."
    )
    app_url: Optional[str] = Field(
        default="",
        description="Entrypoint URL for the task.",
        examples=["https://www.ycombinator.com"]
    )
