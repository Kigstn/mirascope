"""This module contains the type definition for the Groq call keyword arguments."""

from groq.types.chat import ChatCompletionMessageParam, ChatCompletionToolParam

from ..base import BaseCallKwargs
from .call_params import GroqCallParams


class GroqCallKwargs(GroqCallParams, BaseCallKwargs[ChatCompletionToolParam]):
    model: str
    messages: list[ChatCompletionMessageParam]