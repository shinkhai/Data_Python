"""
Tests
"""
from src.population import population_density
from src.time_delta import readable_timedelta


_MSG_NO_RETURN = "Does your function returns a value?"


class TestPopulation:

    def test_has_a_docstring(self):
        assert population_density.__doc__ is not None, (
            "Did you define a docstring for {}".format(
                population_density.__name__))

    def test_null_density(self):
        res = population_density(0, 30)
        if res is None:
            assert False, "Does your function returns a value?"
        assert res == 0, (
            "What should be the population density if there is nobody?")

    def test_non_null_density(self):
        res = population_density(1, 20)
        if res is None:
            assert False, "Does your function returns a value?"
        assert res == 0.05, (
            "Check the implementation of your function")


class TestTimedelta:

    assert readable_timedelta.__doc__ is not None, (
        "Did you define a docstring for {}".format(
            readable_timedelta.__name__))

    def test_has_a_docstring(self):
        assert readable_timedelta.__doc__ is not None

    def test_0_days(self, capsys):
        res = readable_timedelta(0)
        if res is None:
            assert False, "Does your function returns a value?"
        assert res == "0 week(s) and 0 day(s)"

    def test_full_week(self, capsys):
        res = readable_timedelta(14)
        if res is None:
            assert False, "Does your function returns a value?"
        assert res == "2 week(s) and 0 day(s)"

    def test_non_full_week(self, capsys):
        res = readable_timedelta(15)
        if res is None:
            assert False, "Does your function returns a value?"
        assert res == "2 week(s) and 1 day(s)"
