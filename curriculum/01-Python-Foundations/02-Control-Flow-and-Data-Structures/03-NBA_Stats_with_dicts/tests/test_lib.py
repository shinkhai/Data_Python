"""
Tests for dictionaries warmpup
"""
import pytest

from src import lib as interface


class TestDocstring:

    def test_presence(self):
        assert interface.__doc__ is not None, (
            "You need to write a docstring")

    def test_length(self):
        assert len(interface.__doc__) >= 10, (
            "Your docstring is probably too short.")


_DICT_COMP = {
    'Anthony Davis': 28.1,
    'LeBron James': 27.5,
    'James Harden': 30.4,
    'DeMarcus Cousins': 25.2,
    'Damian Lillard': 26.9,
    'Stephen Curry': 26.4,
    'Devin Booker': 24.9,
    'Russell Westbrook': 25.4
}

_CURRY_SCORE = 26.4

_PLAYER_24_9 = 'Devin Booker'

_MICHAEL_JORDAN = None

_IS_SELECTED = {
    'Anthony Davis': True,
    'LeBron James': True,
    'James Harden': True,
    'DeMarcus Cousins': False,
    'Damian Lillard': True,
    'Stephen Curry': True,
    'Devin Booker': False,
    'Russell Westbrook': False
}

_SELECTION = ['Anthony Davis', 'LeBron James', 'James Harden',
              'Damian Lillard', 'Stephen Curry']


@pytest.mark.parametrize("output_idx, expected", [
    (0, _DICT_COMP),
    (1, _CURRY_SCORE),
    (2, _MICHAEL_JORDAN),
    (3, _PLAYER_24_9),
    (4, _IS_SELECTED),
    (5, _SELECTION)
])
def test_outputs(capsys, output_idx, expected):
    interface.main()

    output = [s for s in capsys.readouterr().out.split('\n')
              if len(s) > 0][output_idx]

    assert output == str(expected)
