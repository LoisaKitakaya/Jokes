"""
Module: jokesv2.py

This module provides an extended Python wrapper for a jokes API,
inheriting from the DadJokes class.

Classes:
- AllJokes

"""

import requests
from jokes.jokes import DadJokes


class AllJokes(DadJokes):
    """
    Class: AllJokes

    A class representing an extended Python wrapper for a jokes API, inheriting from DadJokes.

    Methods:
        - __init__(self)
        - get_joke_json(self, joke_lang, joke_category, joke_flags, joke_type, joke_contains, joke_id, joke_amount)
        - get_joke_text(self, joke_lang, joke_category, joke_flags, joke_type, joke_contains, joke_id, joke_amount)


    NOTE: The following are the available and valid values that could be passed as arguments:

        Categories:
            - Any
            - Programming
            - Misc
            - Dark
            - Pun
            - Spooky
            - Christmas

        Language:
            - en -> English
            - fr -> French
            - cs -> Czech
            - de -> German
            - es -> Spanish
            - pt -> Portuguese

        flags:
            - nsfw
            - religious
            - political
            - racist
            - sexist
            - explicit

        format response:
            - json
            - text

        joke type:
            - single
            - two part

        id range:
            - e.g. 0-100 (default="")

        amount of jokes:
            - e.g. 10 (default=1)
    """

    def __init__(self) -> None:
        """
        Initialize the AllJokes class.

        Parameters:
        self

        Returns:
        None
        """

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
        """
        Retrieve jokes in JSON format based on various parameters.

        Parameters:
        self
        joke_lang (str): The language of the jokes (default: "en").
        joke_category (list): The categories of the jokes (default: ["Any"]).
        joke_flags (list): The flags to blacklist specific types of jokes (default: [""]).
        joke_type (list): The types of jokes to retrieve (default: ["single", "twopart"]).
        joke_contains (str): The keyword to filter jokes based on their content (default: "").
        joke_id (str): The ID range of the jokes to retrieve (default: "").
        joke_amount (int): The number of jokes to retrieve (default: 1).

        Returns:
        dict: A dictionary representing the retrieved jokes in JSON format.
        """

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
        """
        Retrieve jokes in plain text format based on various parameters.

        Parameters:
        self
        joke_lang (str): The language of the jokes (default: "en").
        joke_category (list): The categories of the jokes (default: ["Any"]).
        joke_flags (list): The flags to blacklist specific types of jokes (default: [""]).
        joke_type (list): The types of jokes to retrieve (default: ["single", "twopart"]).
        joke_contains (str): The keyword to filter jokes based on their content (default: "").
        joke_id (str): The ID range of the jokes to retrieve (default: "").
        joke_amount (int): The number of jokes to retrieve (default: 1).

        Returns:
        str: A string representing the retrieved jokes in plain text.
        """

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
