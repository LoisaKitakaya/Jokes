from dad_jokes.jokes import DadJokes


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


def test_random_json():
    res = random_json()

    # status
    assert res["status"] == 200

    # types
    assert type(res["id"]) == type("")
    assert type(res["joke"]) == type("")

    # values
    assert res["id"] is not None
    assert res["joke"] is not None


def test_random_text():
    res = random_text()

    # types
    assert type(res) == type("")

    # values
    assert res is not None


def test_specific_json():
    res = specific_json("R7UfaahVfFd")

    # status
    assert res["status"] == 200

    # types
    assert type(res["id"]) == type("")
    assert type(res["joke"]) == type("")

    # values
    assert res["id"] is not None
    assert res["joke"] is not None


def test_specific_text():
    res = specific_text("R7UfaahVfFd")

    # types
    assert type(res) == type("")

    # values
    assert res is not None


def test_list_json():
    page = 2
    limit = 5
    term = "cat"

    res = list_json(page, limit, term)

    # status
    assert res["status"] == 200

    # arguments
    assert res["search_term"] == term
    assert res["current_page"] == page
    assert res["limit"] == limit and len(res["results"]) == limit

    # types
    for joke in res["results"]:
        assert type(joke["id"]) == type("")
        assert type(joke["joke"]) == type("")

    # values
    for joke in res["results"]:
        assert joke["id"] is not None
        assert joke["joke"] is not None


def test_list_text():
    limit = 5

    res = list_text(limit)

    # arguments
    res_list = res.splitlines()

    assert len(res_list) == limit

    # types
    assert type(res) == type("")

    # values
    assert res is not None
