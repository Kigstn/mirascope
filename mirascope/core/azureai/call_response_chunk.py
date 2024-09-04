"""This module contains the `AzureAICallResponseChunk` class.

usage docs: learn/streams.md#handling-streamed-responses
"""

from azure.ai.inference.models import (
    CompletionsFinishReason,
    CompletionsUsage,
    StreamingChatCompletionsUpdate,
)
from pydantic import SkipValidation

from ..base import BaseCallResponseChunk


class AzureAICallResponseChunk(
    BaseCallResponseChunk[StreamingChatCompletionsUpdate, CompletionsFinishReason]
):
    """A convenience wrapper around the AzureAI `ChatCompletionChunk` streamed chunks.

    When calling the AzureAI API using a function decorated with `azureai_call` and
    `stream` set to `True`, the stream will contain `AzureAIResponseChunk` instances with
    properties that allow for more convenient access to commonly used attributes.

    Example:

    ```python
    from mirascope.core import prompt_template
    from mirascope.core.azureai import azureai_call


    @azureai_call("gpt-4o-mini", stream=True)
    @prompt_template("Recommend a {genre} book")
    def recommend_book(genre: str):
        ...


    stream = recommend_book("fantasy")  # response is an `AzureAIStream`
    for chunk, _ in stream:
        print(chunk.content, end="", flush=True)
    ```
    """

    chunk: SkipValidation[StreamingChatCompletionsUpdate]

    @property
    def content(self) -> str:
        """Returns the content for the 0th choice delta."""
        delta = None
        if self.chunk.choices:
            delta = self.chunk.choices[0].delta
        return delta.content if delta is not None and delta.content else ""

    @property
    def finish_reasons(self) -> list[CompletionsFinishReason]:
        """Returns the finish reasons of the response."""
        return [
            finish_reason
            if isinstance(finish_reason, CompletionsFinishReason)
            else CompletionsFinishReason(finish_reason)
            for choice in self.chunk.choices
            if (finish_reason := choice.finish_reason)
        ]

    @property
    def model(self) -> str:
        """Returns the name of the response model."""
        return self.chunk.model

    @property
    def id(self) -> str:
        """Returns the id of the response."""
        return self.chunk.id

    @property
    def usage(self) -> CompletionsUsage:
        """Returns the usage of the chat completion."""
        return self.chunk.usage

    @property
    def input_tokens(self) -> int:
        """Returns the number of input tokens."""
        return self.usage.prompt_tokens

    @property
    def output_tokens(self) -> int:
        """Returns the number of output tokens."""
        return self.usage.completion_tokens
