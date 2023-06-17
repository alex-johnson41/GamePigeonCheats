import unittest
from solvers.anagrams_solver import Anagrams_Solver

class test_anagrams(unittest.TestCase):

    def test_six_letters(self):
        solver = Anagrams_Solver(['t', 'e', 'l', 'l', 'h', 'y'])
        x = solver.solve()
        self.assertEqual(x[0], 'theyll')

    def test_five_letters(self):
        solver = Anagrams_Solver(['s', 'a', 'g', 't', 'e'])
        x = solver.solve()
        self.assertEqual(x[0], 'stage')
        self.assertEqual(x[1], 'gates')
        