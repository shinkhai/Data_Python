"""
Tests Taxi Fare
"""
import inspect

import pytest

try:
    from src.taxi_fare import compute_fare as f
    imported = True
except ImportError:
    imported = False


_DEFAULT_MSG = "Check the implementation of your function"


def test_compute_fare_should_exist():
    assert imported, "Did you create the function?"


def test_compute_fare_has_docstring():
    assert f.__doc__ is not None, "Did you create a docstring?"
    assert len(f.__doc__) >= 10, (
        "Your docstring seems a bit short, did you really explain what your "
        "function is doing?"
    )

class TestFunction:

    args_ = inspect.getargspec(f).args

    def test_it_should_take_3_arguments(self):
        assert len(self.args_) == 3, (
            "Your function should take 3 arguments")

    def test_it_takes_a_distance_argument(self):
        assert 'distance' in self.args_

    def test_it_takes_a_duration_argument(self):
        assert 'duration' in self.args_

    def test_it_takes_a_drop_charge_argument(self):
        assert 'drop_charge' in self.args_

    def test_it_should_take_only_one_default_argument(self):
        assert len(inspect.getargspec(f).defaults) == 1, (
            "Your function should only take one default argument")

    def test_drop_charge_should_take_a_default_value(self):
        assert inspect.getargspec(f).defaults[0] == 2.6, (
            "Did you check the default value for the drop_charge parameter?")

    @pytest.mark.parametrize("input_values, expected, msg", [
        ((0, 0, 2.6), 2.6, "What if the distance and duration are null?"),
        ((3, 3, 2.6), 12.200000000000001, _DEFAULT_MSG)
    ])
    def test_returned_values(self, input_values, expected, msg):
        assert f(*input_values) == expected, msg
