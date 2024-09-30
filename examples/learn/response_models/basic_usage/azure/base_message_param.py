from typing import cast

from mirascope.core import BaseMessageParam, azure
from pydantic import BaseModel


class Book(BaseModel):
    """An extracted book."""

    title: str
    author: str


@azure.call("gpt-4o-mini", response_model=Book)
def extract_book(text: str) -> list[BaseMessageParam]:
    return [BaseMessageParam(role="user", content=f"Extract {text}")]


book = extract_book("The Name of the Wind by Patrick Rothfuss")
print(book)
# Output: title='The Name of the Wind' author='Patrick Rothfuss'

response = cast(azure.AzureCallResponse, book._response)  # pyright: ignore[reportAttributeAccessIssue]
print(response.model_dump())
# > {'metadata': {}, 'response': {'id': ...}, ...}