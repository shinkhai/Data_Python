"""
Tests for "NBA Stats" program
"""
import pytest

from src import nba_stats as interface


class TestDocstring:

    def test_presence(self):
        assert interface.__doc__ is not None, (
            "You need to write a docstring")

    def test_length(self):
        assert len(interface.__doc__) >= 10, (
            "Your docstring is probably too short.")


@pytest.mark.parametrize("output_idx, expected", [
    (0, "Total number of points: 214.8"),
    (1, "Best player: James Harden"),
    (2, ['James Harden', 'Anthony Davis', 'LeBron James', 'Damian Lillard',
         'Stephen Curry', 'Russell Westbrook', 'DeMarcus Cousins',
         'Devin Booker'])
])
def test_base(capsys, output_idx, expected):
    interface.main()

    output = capsys.readouterr().out.split('\n')[output_idx]
    assert output == str(expected)
