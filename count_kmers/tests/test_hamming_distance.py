from unittest import TestCase
from neighbors import hamming_distance


class TestHamming_distance(TestCase):

    def test_equal(self):
        s1 = 'abcdefg'
        s2 = 'abcdefg'
        assert hamming_distance(s1, s2) == 0, "Identical strings should have zero hamming distance"

    def test_distance_1(self):
        s1 = 'abcdefg'
        s2 = 'abcdefz'
        assert hamming_distance(s1, s2) == 1, "Incorrect Hamming distance calculated"

    def test_unequal_length(self):
        s1 = 'abcdefg'
        s2 = 'abcdef'
        assert hamming_distance(s1, s2) == None, "Hamming distance undefined for unequal length strings"

    def test_missing_string(self):
        s1 = 'abcdefg'
        s2 = None
        assert hamming_distance(s1, s2) == None, "Hamming distance undefined for missing string"
        assert hamming_distance(s2, s1) == None, "Hamming distance undefined for missing string"