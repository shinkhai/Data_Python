"""
Tests for "stopwords" program
"""
import pytest

from src import text_processing as interface


class TestDocstring:

    def test_presence(self):
        assert interface.__doc__ is not None, (
            "You need to write a docstring")

    def test_length(self):
        assert len(interface.__doc__) >= 10, (
            "Your docstring is probably too short.")


_OUTPUT_0 = ['This', 'is', 'a', 'sample', 'sentence,', 'the', 'purpose', 'of',
             'this', 'sentence', 'is', 'to', 'be', 'used', 'as', 'a', 'demo',
             'for', 'our', 'exercice']

_OUTPUT_1 = ['this', 'is', 'a', 'sample', 'sentence,', 'the', 'purpose', 'of',
             'this', 'sentence', 'is', 'to', 'be', 'used', 'as', 'a', 'demo',
             'for', 'our', 'exercice']
_OUTPUT_2 = ['sample', 'sentence,', 'purpose', 'sentence', 'used', 'demo',
             'exercice']


@pytest.mark.parametrize("output_idx, expected", [
    (0, _OUTPUT_0),
    (1, _OUTPUT_1),
    (2, _OUTPUT_2)
])
def test_base(capsys, output_idx, expected):
    interface.main()

    output = capsys.readouterr().out.split('\n')[output_idx]
    assert output == str(expected), "Unexpected result"
