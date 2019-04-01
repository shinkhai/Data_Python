"""
Tests
"""
import re

import pytest

from src import calculator as interface


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
        self.prompts = []
        self.output = []

        def mock_input(s):
            self.prompts.append(s)
            return next(self.input_values)

        interface.input = mock_input
        interface.print = lambda s: self.output.append(s)

    def teardown_method(self):
        interface.input = self._input
        interface.print = self._print

    @pytest.mark.parametrize("input_values", [
        ['+', '1', '2', 'quit'],
    ])
    def test_len_prompts(self, input_values):
        expected = len(input_values)
        self.input_values = iter(input_values)

        interface.main()

        assert len(self.prompts) == expected, (
            f"You should be prompting {expected} times")

    @pytest.mark.parametrize("input_values", [
        ['+', '1', '2', 'quit'],
    ])
    def test_prompts_values(self, input_values):
        self.input_values = iter(input_values)
        interface.main()

        expected = [
            "Pick an operator (+, -, *, /, //, %): ",
            "First number: ",
            "Second number: "
        ]

        assert all(e in self.prompts for e in expected), (
            "At least one of your prompts value is wrong")

    @pytest.mark.parametrize("input_values", [
        ['quit', '1', '2'],
        ['1', 'quit', '2'],
        ['1', '2', 'quit']
    ])
    def test_quitting(self, input_values):
        self.input_values = iter(input_values)

        interface.main()

        assert any("Quitting" in s for s in self.output), (
            "Users should be able to quit your program any time")

    def test_prints(self):
        self.input_values = iter(["+", "3", "1", "quit"])

        interface.main()
        prints = [
            r"Welcome to Calculator, you can quit anytime by typing 'quit'",
            r"The result is: \d+(.\d+)?",
            r"-+"
        ]
        # TODO: Probably split this into individual tests
        #       To provide more guidance
        assert all([
            any([re.search(p, o) is not None for o in self.output])
            for p in prints
        ]), "At least one of your print statement is incorrect"

    def test_len_output(self):
        self.input_values = iter(["+", "3", "1", "quit"])

        interface.main()

        assert len(self.output) == 4, "You should print out 4 times"

    @pytest.mark.parametrize("input_values, expected", [
        (['+', '1', '2', 'quit'], 3.0),
        (['+', '0', '2', 'quit'], 2),
        (['-', '0', '2', 'quit'], -2),
        (['*', '3', '2', 'quit'], 6.0),
        (['*', '0', '2', 'quit'], 0.0),
        (['/', '3', '2', 'quit'], 1.5),
        (['%', '3', '2', 'quit'], 1.0),
        (['%', '3', '2', 'quit'], 1.0),
        (['**', '2', '10', 'quit'], 1024.0)
    ])
    def test_ouput_value(self, input_values, expected):
        self.input_values = iter(input_values)

        interface.main()

        pattern = r"The\sresult\sis:\s(-?\d+(.\d)?)"
        match = re.search(pattern, self.output[1])
        assert float(match.group(1)) == expected, (
            "'{}' not implemented properly".format(input_values[0]))

    def test_invalid_operator(self):
        self.input_values = iter(['invalid_operator', '1', '3', 'quit'])

        interface.main()

        assert (
            "Sorry, 'invalid_operator' "
            "is not a valid operator") in self.output, (
            "You need to handle invalid operators")
        assert all(["The result is: " not in o for o in self.output]), (
            "If the operator is invalid, you shouldn't display the result")
