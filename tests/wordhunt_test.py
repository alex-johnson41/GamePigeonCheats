import unittest
from solvers.wordhunt_solver import WordHunt_Solver


class test_wordhunt(unittest.TestCase):

    def test_largest_word(self):
        solver = WordHunt_Solver(['a','s','d','f','h','u','r','e','w','i','o','p','c','h','f','u'])
        x = solver.solve()
        self.assertEqual(x.popitem()[0], 'choired') # type: ignore