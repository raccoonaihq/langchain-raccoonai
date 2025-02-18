from typing import Optional, Any, Dict

from pydantic import Field

from .run import RunParams


class ExtractParams(RunParams):
    response_schema: Optional[Dict[str, Any]] = Field(
        description="The expected schema for the response. Describe the fields and their purpose using a JSON schema.",
        example={
            "type": "object",
            "properties": {
                "product_name": {
                    "type": "string",
                    "description": "Name of the graphics card"
                },
                "price": {
                    "type": "number",
                    "description": "Current price in USD"
                },
                "url": {
                    "type": "string",
                    "description": "Product page URL"
                }
            }
        },
        default={
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "Relevant title according to what is mentioned in the query"
                },
                "summary": {
                    "type": "string",
                    "description": "Relevant summary according to what is mentioned in the query"
                },
                "properties": {
                    "type": "object",
                    "description": "Any other relevant properties that might be helpful"
                }
            }
        }
    )
    max_count: Optional[int] = Field(
        default=1,
        description="Max number of results.",
        example=2,
        le=20
    )
