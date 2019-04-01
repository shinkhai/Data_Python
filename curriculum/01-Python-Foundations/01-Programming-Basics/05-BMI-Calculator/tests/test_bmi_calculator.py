"""test_base.py

"""
from itertools import tee

import pytest

from src import bmi_calculator as interface


@pytest.fixture
def input_values():
    return iter(['georges', 193, 96])


class TestDocstring:

    def test_presence(self):
        assert interface.__doc__ is not None, (
            "You need to write a docstring")

    def test_length(self):
        assert len(interface.__doc__) >= 10, (
            "Your docstring is probably too short.")


# TODO: We're manually mocking `input`
#       We should be using unittest's mock or pytest-mock
class TestBase:

    def setup_method(self, input_values):
        self._input = input
        self._print = print
        self.output = []

        def mock_input(s):
            self.output.append(s)
            return next(self.input_values)

        interface.input = mock_input
        interface.print = lambda s: self.output.append(s)

    def teardown_method(self):
        interface.input = self._input
        interface.print = self._print

    def test_len_output(self, input_values):
        input_it, input_ = tee(input_values)
        self.input_values = input_it

        interface.main()

        assert len(self.output) == len(list(input_)) + 1

    def test_first_input_prompt(self, input_values):
        self.input_values = input_values

        interface.main()

        assert self.output[0] == "What's your name? "

    def test_second_input_prompt(self, input_values):
        self.input_values = input_values

        interface.main()

        assert self.output[1] == "How tall are you (in cm)? "

    def test_third_input_prompt(self, input_values):
        self.input_values = input_values

        interface.main()
        assert self.output[2] == "How much do you weight (in kg)? "

    def test_ouput_value(self, input_values):
        input_it, (name, height, weight) = tee(input_values)
        self.input_values = input_it

        interface.main()

        output = self.output[3]
        expected_bmi = weight / (height / 100)**2

        assert name.lower() in output.lower(), "Did you use the name?"
        assert output[6] == name[0].upper(), "Did you capitalize the name?"
        assert output[-1] == "!", "Don't forget the mark at the end"
        assert output[-6:-1] == "{:.2f}".format(expected_bmi), (
            "Did you format the BMI to only 2 decimals?")
        assert output == "Hello Georges, your BMI is {:.2f}!".format(
            expected_bmi)

    @pytest.mark.parametrize('name, height, weight', [
        ("georges", "abc", 13),
        ("georges", 13, "abc"),
        ("georges", "abc", "abc")
    ])
    @pytest.mark.xfail(raises=ValueError, strict=True)
    def test_invalid_height(self, name, height, weight):
        self.input_values = iter([name, height, weight])
        try:
            interface.main()
        except TypeError:
            raise TypeError("Did you cast your input?")
