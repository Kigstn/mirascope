from tenacity import retry, stop_after_attempt, wait_exponential

from mirascope.core import anthropic, prompt_template


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10),
)
@anthropic.call("claude-3-5-sonnet-20240620", stream=True)
def recommend_book(genre: str) -> str:
    return f"Recommend a {genre} book."


def stream():
    for chunk, _ in recommend_book("fantasy"):
        print(chunk.content, end="", flush=True)


stream()
