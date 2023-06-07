from dad_jokes.jokes import DadJokes

# jokes module


def random_json():
    res = DadJokes()

    response = res.random_joke_as_json()

    return response


def random_text():
    res = DadJokes()

    response = res.random_joke_as_text()

    return response


def specific_json(id):
    res = DadJokes()

    response = res.specific_joke_as_json(id=id)

    return response


def specific_text(id):
    res = DadJokes()

    response = res.specific_joke_as_text(id=id)

    return response


def list_json(page, limit, term):
    res = DadJokes()

    response = res.list_jokes_as_json(page=page, limit=limit, term=term)

    return response


def list_text(limit):
    res = DadJokes()

    response = res.list_jokes_as_text(limit=limit)

    return response
