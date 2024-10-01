import json

from mirascope.core import Messages, anthropic


@anthropic.call("claude-3-5-sonnet-20240620", json_mode=True)
def get_book_info(book_title: str) -> Messages.Type:
    return Messages.User(f"Provide the author and genre of {book_title}")


try:
    response = get_book_info("The Name of the Wind")
    print(json.loads(response.content))
except json.JSONDecodeError:
    print("The model produced invalid JSON")