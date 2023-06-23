# py-jokes-py

Python wrapper for the jokes APIs provided by:

- [icanhazdadjokes.com](https://icanhazdadjoke.com/)
- [jokeapi.dev](https://jokeapi.dev/)

## How to install

```
pip install py-jokes-py
```

## Usage

Something to note, the `jokes` module has two classes:

- `DadJokes()` - wrapper for [icanhazdadjokes.com](https://icanhazdadjoke.com/) api
- `AllJokes()` - wrapper for [jokeapi.dev](https://jokeapi.dev/) api

##### Class `DadJokes()`

This class provides the following methods:

- `random_joke_as_json(self)`
- `random_joke_as_text(self)`
- `specific_joke_as_json(self, id)`
- `specific_joke_as_text(self, id)`
- `list_jokes_as_json(self, page, limit, term)`
- `list_jokes_as_text(self, page, limit, term)`

##### Class `AllJokes()`

This class inherits from the `DadJokes` class, but also provides the following methods:

- `get_joke_json(self, joke_lang, joke_category, joke_flags, joke_type, joke_contains, joke_id, joke_amount)`
- `get_joke_text(self, joke_lang, joke_category, joke_flags, joke_type, joke_contains, joke_id, joke_amount)`

#### Basic Usage

```
from jokes.jokesv2 import AllJokes

jokes = AllJokes()

joke = jokes.get_joke_json()
print(joke)

joke = jokes.get_joke_text()
print(joke)

joke = jokes.random_joke_as_json()
print(joke)

joke = jokes.random_joke_as_text()
print(joke)

joke = jokes.specific_joke_as_json(id="12")
print(joke)

joke = jokes.specific_joke_as_text(id="12")
print(joke)

joke = jokes.list_jokes_as_json()
print(joke)

joke = jokes.list_jokes_as_text()
print(joke)
```

## Example

Here is a simple implementation of this package. Check it out:

- [jokes_cli](https://github.com/LoisaKitakaya/jokes_cli)

## Issues

For any issus encountered while using this package, feel free to submit a new issue [here](https://github.com/LoisaKitakaya/Jokes/issues).

Enjoy! 🤪