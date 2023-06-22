from jokes.jokesv2 import AllJokes

jokes = AllJokes()  # jokes module: DadJokes class


class TestDadJokes:
    def test_random_json(self):
        res = jokes.random_joke_as_json()

        # status
        assert res["status"] == 200

        # types
        assert type(res["id"]) == type("")
        assert type(res["joke"]) == type("")

        # values
        assert res["id"] is not None
        assert res["joke"] is not None

    def test_random_text(self):
        res = jokes.random_joke_as_text()

        # types
        assert type(res) == type("")

        # values
        assert res is not None

    def test_specific_json(self):
        res = jokes.specific_joke_as_json(id="R7UfaahVfFd")

        # status
        assert res["status"] == 200

        # types
        assert type(res["id"]) == type("")
        assert type(res["joke"]) == type("")

        # values
        assert res["id"] is not None
        assert res["joke"] is not None

    def test_specific_text(self):
        res = jokes.specific_joke_as_text(id="R7UfaahVfFd")

        # types
        assert type(res) == type("")

        # values
        assert res is not None

    def test_list_json(self):
        page = 2
        limit = 5
        term = "cat"

        res = jokes.list_jokes_as_json(page=page, limit=limit, term=term)

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

        res = jokes.list_jokes_as_text(limit=limit)

        # arguments
        res_list = res.splitlines()

        assert len(res_list) == limit

        # types
        assert type(res) == type("")

        # values
        assert res is not None


class TestOtherJokes:
    def test_get_joke_json(self):
        res = jokes.get_joke_json(joke_type=["single"], joke_amount=2)

        # success
        assert res["error"] == False

        # joke type
        assert res["jokes"][0]["type"] and res["jokes"][1]["type"] == "single"

        # no of jokes
        assert len(res["jokes"]) == 2

        # is valid
        assert res["jokes"][0]["joke"] and res["jokes"][1]["joke"] is not None

        # type
        assert type(res["jokes"][0]["joke"]) and type(res["jokes"][1]["joke"]) == type(
            ""
        )

    def test_get_joke_text(self):
        res = jokes.get_joke_text(joke_type=["single"], joke_amount=2)

        # no of jokes
        new_list = res.split("\n\n")

        new_list = [new_list[0], new_list[-1]]

        assert len(new_list) == 2

        # success
        assert res is not None

        # type
        assert type(res) == type("")

    def test_get_joke2_json(self):
        res = jokes.get_joke_json(joke_type=["twopart"], joke_amount=2)

        # success
        assert res["error"] == False

        # joke type
        assert res["jokes"][0]["type"] and res["jokes"][1]["type"] == "twopart"

        # no of jokes
        assert len(res["jokes"]) == 2

        # is valid
        assert res["jokes"][0]["setup"] and res["jokes"][1]["setup"] is not None
        assert res["jokes"][0]["delivery"] and res["jokes"][1]["delivery"] is not None

        # type
        assert type(res["jokes"][0]["setup"]) and type(
            res["jokes"][1]["delivery"]
        ) == type("")
        assert type(res["jokes"][0]["setup"]) and type(
            res["jokes"][1]["delivery"]
        ) == type("")

    def test_get_joke2_text(self):
        res = jokes.get_joke_text(joke_type=["twopart"], joke_amount=2)

        # no of jokes
        new_list = res.split("\n\n")

        new_list = [new_list[0], new_list[1], new_list[3], new_list[4]]

        assert len(new_list) == 4

        # success
        assert res is not None

        # type
        assert type(res) == type("")
