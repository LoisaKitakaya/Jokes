from .context import *


class TestJokes:
    def test_random_json(self):
        res = random_json()

        # status
        assert res["status"] == 200

        # types
        assert type(res["id"]) == type("")
        assert type(res["joke"]) == type("")

        # values
        assert res["id"] is not None
        assert res["joke"] is not None

    def test_random_text(self):
        res = random_text()

        # types
        assert type(res) == type("")

        # values
        assert res is not None

    def test_specific_json(self):
        res = specific_json("R7UfaahVfFd")

        # status
        assert res["status"] == 200

        # types
        assert type(res["id"]) == type("")
        assert type(res["joke"]) == type("")

        # values
        assert res["id"] is not None
        assert res["joke"] is not None

    def test_specific_text(self):
        res = specific_text("R7UfaahVfFd")

        # types
        assert type(res) == type("")

        # values
        assert res is not None

    def test_list_json(self):
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

    def test_list_text(self):
        limit = 5

        res = list_text(limit)

        # arguments
        res_list = res.splitlines()

        assert len(res_list) == limit

        # types
        assert type(res) == type("")

        # values
        assert res is not None
