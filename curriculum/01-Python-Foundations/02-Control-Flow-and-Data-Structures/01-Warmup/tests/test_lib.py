"""
Tests for Warmup
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


@pytest.mark.parametrize("output_idx, expected", [
    (0, 12),
    (1, 31),
    (2, 28),
    (3, 30),
    (4, ["Carol", "Albert", "Ben", "Donna", "Eugenia"]),
    (5, "Carol & Albert & Ben & Donna & Eugenia")
])
def test_indexing(capsys, output_idx, expected):
    interface.main()

    output = [s for s in capsys.readouterr().out.split('\n')
              if len(s) > 0][output_idx]

    assert output == str(expected)
