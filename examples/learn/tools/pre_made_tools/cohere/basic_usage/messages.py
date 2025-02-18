from mirascope.core import cohere, Messages
from mirascope.tools import DuckDuckGoSearch


@cohere.call("command-r-plus", tools=[DuckDuckGoSearch])
def research(genre: str) -> Messages.Type:
    return Messages.User(f"Recommend a {genre} book and summarize the story")


response = research("fantasy")
if tool := response.tool:
    print(tool.call())
