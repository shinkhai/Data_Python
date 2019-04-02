"""
Tests for "Fizz Buzz" program
"""
import os
import inspect

from src import fizz_buzz as interface


class TestDocstring:

    def test_presence(self):
        assert interface.__doc__ is not None, (
            "You need to write a docstring")

    def test_length(self):
        assert len(interface.__doc__) >= 10, (
            "Your docstring is probably too short.")


def test_for_loop():
    source_lines = inspect.getsourcelines(interface.main)[0]
    lines = [l.strip() for l in source_lines if not l.strip().startswith("#")]
    assert any(["for" in l for l in lines]), "Did you use a `for` loop?"


def test_base(capsys):
    interface.main()
    with open(os.path.join('tests', 'expected.txt'), 'r') as f:
        expected = f.read()
    output = capsys.readouterr().out
    assert output == expected
