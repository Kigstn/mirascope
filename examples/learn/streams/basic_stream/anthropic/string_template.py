from mirascope.core import anthropic, prompt_template


@anthropic.call("claude-3-5-sonnet-20240620", stream=True)
@prompt_template("Recommend a {genre} book")
def recommend_book(genre: str): ...


stream = recommend_book("fantasy")
for chunk, _ in stream:
    print(chunk.content, end="", flush=True)

print(f"Content: {stream.content}")

call_response = stream.construct_call_response()
print(f"Usage: {call_response.usage}")