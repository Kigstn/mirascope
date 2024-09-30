from mirascope.core import anthropic


@anthropic.call("claude-3-5-sonnet-20240620")
def recommend_book(genre: str) -> anthropic.AnthropicDynamicConfig:
    return {"messages": [{"role": "user", "content": f"Recommend a {genre} book"}]}


print(recommend_book("fantasy"))