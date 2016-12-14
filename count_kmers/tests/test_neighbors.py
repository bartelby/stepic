# coding=utf-8
from unittest import TestCase
import neighbors

class TestNeighbors(TestCase):
    def test_immediate_neighbors(self):
        expected = set(['ACG','CCG','GCG','TCG','AAG','AGG','ATG','ACA','ACC','ACT'])
        actual = neighbors.immediate_neighbors('ACG')
        assert self.are_equal(actual, expected), "test_immediate_neighborhood failed"

    def test_neighbors_d1(self):
        expected = set(['ACG', 'CCG', 'GCG', 'TCG', 'AAG', 'AGG', 'ATG', 'ACA', 'ACC', 'ACT'])
        actual = neighbors.neighbors('ACG', 1)
        assert self.are_equal(actual, expected), "test_neighborhood_d1 failed"

    def test_neighbors_d2(self):
        expected =  set(['AAA', 'AAC', 'AAG', 'AAT', 'ACA', 'ACC', 'ACG', 'ACT', 'AGA', 'AGC',
                        'AGG', 'AGT','ATA', 'ATC', 'ATG', 'ATT', 'CAG', 'CCA', 'CCC', 'CCG',
                         'CCT', 'CGG', 'CTG', 'GAG', 'GCA', 'GCC', 'GCG', 'GCT', 'GGG',
                         'GTG', 'TAG', 'TCA', 'TCC', 'TCG', 'TCT', 'TGG', 'TTG'])
        actual = neighbors.neighbors('ACG', 2)
        assert self.are_equal(actual, expected), "test_neighbors failed"

    def test_iterative_vs_recursive(self):
        recursive_vals = neighbors.neighbors('ACGTA',2)
        iter_vals = neighbors.neighbors_iterative('ACGTA', 2)
        assert self.are_equal(recursive_vals, iter_vals), "Something very wrong here..."

    def are_equal(self, s1, s2):
        """
        Tests whether two sets are equal - contain the same elements in any order
        :param s1: a set of strings
        :param s2: another set of strings
        :return: True if the two sets contain the same strings, False otherwise
        """
        if len(s1) != len(s2):
            return False
        for s in s1:
            if s not in s2:
                return False
        return True