import unittest
from solvers.anagrams_solver import Anagrams_Solver

class test_anagrams(unittest.TestCase):

    def testSixletters(self):
        solver = Anagrams_Solver(['t', 'e', 'l', 'l', 'h', 'y'])
        x = solver.solve()
        self.assertEqual(x, ['theyll', 'telly', 'lythe', 'lethy', 'helly', 'ethyl', 
                             'yeth', 'yelt', 'yell', 'they', 'tell', 'hyte', 'hyle', 
                             'htel', 'hell', 'yet', 'yeh', 'tye', 'thy', 'the', 'tel', 
                             'lye', 'ley', 'let', 'hye', 'hey', 'het', 'hel', 'eyl', 
                             'ety', 'eth', 'elt', 'ell'])

    def testFiveLetters(self):
        solver = Anagrams_Solver(['s', 'a', 'g', 't', 'e'])
        x = solver.solve()
        self.assertEqual(x, ['stage', 'getas', 'geast', 'gates', 'tegs', 'tega', 'teas', 
                             'tags', 'stge', 'steg', 'stag', 'seta', 'seat', 'sate', 'sage', 
                             'gets', 'geta', 'gest', 'geat', 'gats', 'gate', 'gast', 'gaet', 
                             'gaes', 'etas', 'eats', 'east', 'ates', 'agst', 'aget', 'ages', 
                             'teg', 'tea', 'tas', 'tag', 'tae', 'stg', 'sta', 'set', 'seg', 
                             'sea', 'sat', 'sag', 'sae', 'gte', 'get', 'ges', 'gat', 'gas', 
                             'gae', 'eta', 'est', 'eat', 'ate', 'ast', 'asg', 'ase', 'agt', 
                             'age', 'aet', 'aes'])

    def testInputOrder(self):
        solver1 = Anagrams_Solver(['t', 'e', 'l', 'l', 'h', 'y'])
        solver2 = Anagrams_Solver(['t', 'h', 'e', 'y', 'l', 'l'])
        x = solver1.solve()
        y = solver2.solve()
        self.assertEqual(x, y)