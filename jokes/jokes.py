"""
Module: jokes.py

This module provides a Python wrapper for a jokes API,
allowing users to retrieve random jokes, specific jokes,
and list jokes based on search criteria.

Classes:
    - DadJokes

Functions:
    - __init__(self)
    - random_joke_as_json(self)
    - random_joke_as_text(self)
    - specific_joke_as_json(self, id)
    - specific_joke_as_text(self, id)
    - list_jokes_as_json(self, page, limit, term)
    - list_jokes_as_text(self, page, limit, term)

"""

import requests


class DadJokes:
    """
    Class: DadJokes

    A class representing a Python wrapper for a jokes API.

    Methods:
        - __init__(self)
        - random_joke_as_json(self)
        - random_joke_as_text(self)
        - specific_joke_as_json(self, id)
        - specific_joke_as_text(self, id)
        - list_jokes_as_json(self, page, limit, term)
        - list_jokes_as_text(self, page, limit, term)

    """

    def __init__(self) -> None:
        """
        Initialize the DadJokes class.

        Parameters:
        self

        Returns:
        None
        """

        self.DAD_JOKES_BASE_URL = "https://icanhazdadjoke.com"

        self.json_response = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        self.text_response = {
            "Accept": "text/plain",
            "Content-Type": "application/json",
        }

    def random_joke_as_json(self):
        """
        Retrieve a random joke as JSON format.

        Parameters:
        self

        Returns:
        dict: A dictionary representing the random joke in JSON format.
        """

        url = f"{self.DAD_JOKES_BASE_URL}/"

        joke = requests.get(url, headers=self.json_response)

        return joke.json()

    def random_joke_as_text(self):
        """
        Retrieve a random joke as plain text.

        Parameters:
        self

        Returns:
        str: A string representing the random joke in plain text.
        """

        url = f"{self.DAD_JOKES_BASE_URL}/"

        joke = requests.get(url, headers=self.text_response)

        return joke.text

    def specific_joke_as_json(self, id: str = ""):
        """
        Retrieve a specific joke by its ID in JSON format.

        Parameters:
        self
        id (str): The ID of the specific joke (optional).

        Returns:
        dict: A dictionary representing the specific joke in JSON format.
        """

        url = f"{self.DAD_JOKES_BASE_URL}/j/{id}"

        joke = requests.get(url, headers=self.json_response)

        return joke.json()

    def specific_joke_as_text(self, id: str = ""):
        """
        Retrieve a specific joke by its ID in plain text.

        Parameters:
        self
        id (str): The ID of the specific joke (optional).

        Returns:
        str: A string representing the specific joke in plain text.
        """

        url = f"{self.DAD_JOKES_BASE_URL}/j/{id}"

        joke = requests.get(url, headers=self.text_response)

        return joke.text

    def list_jokes_as_json(self, page: int = 1, limit: int = 10, term: str = ""):
        """
        Retrieve a list of jokes in JSON format based on search criteria.

        Parameters:
        self
        page (int): The page number of the jokes list (default: 1).
        limit (int): The maximum number of jokes per page (default: 10).
        term (str): The search term for filtering jokes (optional).

        Returns:
        dict: A dictionary representing the list of jokes in JSON format.
        """

        url = f"{self.DAD_JOKES_BASE_URL}/search"

        payload = {"page": f"{page}", "limit": f"{limit}", "term": term}

        jokes = requests.get(url, headers=self.json_response, params=payload)

        return jokes.json()

    def list_jokes_as_text(self, page: int = 1, limit: int = 10, term: str = ""):
        """
        Retrieve a list of jokes in plain text based on search criteria.

        Parameters:
        self
        page (int): The page number of the jokes list (default: 1).
        limit (int): The maximum number of jokes per page (default: 10).
        term (str): The search term for filtering jokes (optional).

        Returns:
        str: A string representing the list of jokes in plain text.
        """

        url = f"{self.DAD_JOKES_BASE_URL}/search"

        payload = {"page": f"{page}", "limit": f"{limit}", "term": term}

        jokes = requests.get(url, headers=self.text_response, params=payload)

        return jokes.text
