from dad_jokes.jokes import DadJokes

dad_jokes = DadJokes()  # jokes module: DadJokes class


class TestJokes:
    def test_random_json(self):
        res = dad_jokes.random_joke_as_json()

        # status
        assert res["status"] == 200

        # types
        assert type(res["id"]) == type("")
        assert type(res["joke"]) == type("")

        # values
        assert res["id"] is not None
        assert res["joke"] is not None

    def test_random_text(self):
        res = dad_jokes.random_joke_as_text()

        # types
        assert type(res) == type("")

        # values
        assert res is not None

    def test_specific_json(self):
        res = dad_jokes.specific_joke_as_json(id="R7UfaahVfFd")

        # status
        assert res["status"] == 200

        # types
        assert type(res["id"]) == type("")
        assert type(res["joke"]) == type("")

        # values
        assert res["id"] is not None
        assert res["joke"] is not None

    def test_specific_text(self):
        res = dad_jokes.specific_joke_as_text(id="R7UfaahVfFd")

        # types
        assert type(res) == type("")

        # values
        assert res is not None

    def test_list_json(self):
        page = 2
        limit = 5
        term = "cat"

        res = dad_jokes.list_jokes_as_json(page=page, limit=limit, term=term)

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

    def test_list_text(self):
        limit = 5

        res = dad_jokes.list_jokes_as_text(limit=limit)

        # arguments
        res_list = res.splitlines()

        assert len(res_list) == limit

        # types
        assert type(res) == type("")

        # values
        assert res is not None
