"""test_lib.py

"""
from src.stats import sum_, mean, median, mode, variance, stdev


class TestSum:

    def test_empty(self):
        seq = []
        res = sum_(seq)
        exp = 0
        assert res == exp

    def test_base(self):
        seq = [1, 2, 6]
        res = sum_(seq)
        exp = 9
        assert res == exp


class TestMean:

    def test_base(self):
        seq = [1, 2, 6]
        res = mean(seq)
        exp = 3
        assert res == exp


class TestMedian:

    def test_base(self):
        seq = [1, 2, 6]
        res = median(seq)
        exp = 2
        assert res == exp


class TestMode:

    def test_one_value_seq(self):
        v = 3
        seq = [v, v, v, v]
        assert mode(seq) == v

    def test_numerics(self):
        seq = [1, 2, 2, 3, 3, 3, 4]
        assert mode(seq) == 3

    def test_non_numerics(self):
        seq = ['foo', 'bar', 'foo', 'foo', 'bar']
        assert mode(seq) == 'foo'

    def test_multiple_res(self):
        seq = [1, 2, 2, 3, 3]
        assert mode(seq) == 2
        seq = [1, 3, 3, 2, 2]
        assert mode(seq) == 2


class TestVariance:

    def test_null_variation(self):
        seq = [2, 2, 2]
        res = variance(seq)
        exp = 0
        assert res == exp

    def test_base(self):
        seq = [2, 2, 8, 8]
        res = variance(seq)
        exp = 9
        assert res == exp


class TestStandardDeviation:

    def test_null_variation(self):
        seq = [2, 2, 2]
        res = stdev(seq)
        exp = 0
        assert res == exp

    def test_base(self):
        seq = [2, 2, 8, 8]
        res = stdev(seq)
        exp = 3
        assert res == exp
