import requests
from dad_jokes.jokes import DadJokes


class AllJokes(DadJokes):
    def __init__(self) -> None:
        super().__init__()

        self.JOKES_BASE_URL = "https://v2.jokeapi.dev/joke"

    def get_joke_json(
        self,
        joke_lang: str = "en",
        joke_category: list = ["Any"],
        joke_flags: list = [""],
        joke_type: list = ["single", "twopart"],
        joke_contains: str = "",
        joke_id: str = "",
        joke_amount: int = 1,
    ):
        category = (
            "+".join(joke_category) if len(joke_category) > 1 else joke_category[0]
        )

        flag = "+".join(joke_flags) if len(joke_flags) > 1 else joke_flags[0]

        type = "+".join(joke_type) if len(joke_type) > 1 else joke_type[0]

        url = f"{self.JOKES_BASE_URL}/{category}"

        payload = {
            "lang": joke_lang,
            "blacklistFlags": flag,
            "format": "json",
            "type": type,
            "contains": joke_contains,
            "idRange": joke_id,
            "amount": str(joke_amount),
        }

        joke = requests.get(url, headers=self.json_response, params=payload)

        return joke.json()

    def get_joke_text(
        self,
        joke_lang: str = "en",
        joke_category: list = ["Any"],
        joke_flags: list = [""],
        joke_type: list = ["single", "twopart"],
        joke_contains: str = "",
        joke_id: str = "",
        joke_amount: int = 1,
    ):
        category = (
            "+".join(joke_category) if len(joke_category) > 1 else joke_category[0]
        )

        flag = "+".join(joke_flags) if len(joke_flags) > 1 else joke_flags[0]

        type = "+".join(joke_type) if len(joke_type) > 1 else joke_type[0]

        url = f"{self.JOKES_BASE_URL}/{category}"

        payload = {
            "lang": joke_lang,
            "blacklistFlags": flag,
            "format": "txt",
            "type": type,
            "contains": joke_contains,
            "idRange": joke_id,
            "amount": str(joke_amount),
        }

        joke = requests.get(url, headers=self.json_response, params=payload)

        return joke.text
