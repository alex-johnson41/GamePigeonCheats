import itertools
from typing import Dict, List

class Anagrams_Solver():

    def __init__(self, letters):
        self.letters = []
        for letter in letters:
            self.letters.append(letter)
        self.wordList = self.createWordList()
        
    def solve(self) -> List[str]:
        combos = self.getCombinations()
        words = self.getWords(combos)
        words = sorted(words, key= len, reverse=True)
        return words

    def createWordList(self) -> Dict[str, str]:
        file = open('word_lists/anagrams_wordList.txt')
        wordList = {}
        for line in file:
            line = line.strip()
            wordList[line] = line
        return wordList

    def getCombinations(self) -> List[str]:
        combos = []
        s = ' '
        for r in range(3, len(self.letters)+1,1):
            for combination in itertools.permutations(self.letters, r):
                for char in combination:
                    s = s + char
                combos.append(s)
                s = ''
        return combos

    def getWords(self, combos) -> List[str]:
        words = []
        for word in combos:
            if word in self.wordList and word not in words:
                words.append(word)
                #print(word)
        return words
