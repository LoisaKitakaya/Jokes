import requests


class DadJokes:
    def __init__(self) -> None:
        self.BASE_URL = "https://icanhazdadjoke.com"

        self.json_response = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        self.text_response = {
            "Accept": "text/plain",
            "Content-Type": "application/json",
        }

    def random_joke_as_json(self):
        url = f"{self.BASE_URL}/"

        joke = requests.get(url, headers=self.json_response)

        return joke.json()

    def random_joke_as_text(self):
        url = f"{self.BASE_URL}/"

        joke = requests.get(url, headers=self.text_response)

        return joke.text

    def specific_joke_as_json(self, id: str = ""):
        url = f"{self.BASE_URL}/j/{id}"

        joke = requests.get(url, headers=self.json_response)

        return joke.json()

    def specific_joke_as_text(self, id: str = ""):
        url = f"{self.BASE_URL}/j/{id}"

        joke = requests.get(url, headers=self.text_response)

        return joke.text

    def list_jokes_as_json(self, page: int = 1, limit: int = 10, term: str = ""):
        url = f"{self.BASE_URL}/search"

        payload = {"page": f"{page}", "limit": f"{limit}", "term": term}

        jokes = requests.get(url, headers=self.json_response, params=payload)

        return jokes.json()

    def list_jokes_as_text(self, page: int = 1, limit: int = 10, term: str = ""):
        url = f"{self.BASE_URL}/search"

        payload = {"page": f"{page}", "limit": f"{limit}", "term": term}

        jokes = requests.get(url, headers=self.text_response, params=payload)

        return jokes.text
