from dad_jokes.jokes import DadJokes

# jokes module: DadJokes class

dad_jokes = DadJokes()


def random_json():
    return dad_jokes.random_joke_as_json()


def random_text():
    return dad_jokes.random_joke_as_text()


def specific_json(id):
    return dad_jokes.specific_joke_as_json(id=id)


def specific_text(id):
    return dad_jokes.specific_joke_as_text(id=id)


def list_json(page, limit, term):
    return dad_jokes.list_jokes_as_json(page=page, limit=limit, term=term)


def list_text(limit):
    return dad_jokes.list_jokes_as_text(limit=limit)
