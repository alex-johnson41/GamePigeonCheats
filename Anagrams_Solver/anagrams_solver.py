import itertools

class Anagrams_Solver():
    def __init__(self, letters):
        self.letters = []
        for letter in letters:
            self.letters.append(letter)
        self.wordList = self.createWordList()
        
    def solve(self):
        combos = self.getCombinations()
        words = self.getWords(combos)
        words = sorted(words, key= len, reverse=True)
        return words

    def createWordList(self):
        file = open('anagrams_wordList.txt')
        wordList = {}
        for line in file:
            line = line.strip()
            wordList[line] = line
        return wordList


    def getInput(self):
        inp = None

        print("Welcome to Anagrams Solver")
        print("Enter all letters with no spaces, then press enter")
        inp = input()
        for char in inp:
            self.letters.append(char)


    def getCombinations(self):
        combos = []
        s = ' '
        for r in range(3, len(self.letters)+1,1):
            for combination in itertools.permutations(self.letters, r):
                for char in combination:
                    s = s + char
                combos.append(s)
                s = ''
        return combos

    def getWords(self, combos):
        words = []
        for word in combos:
            if word in self.wordList and word not in words:
                words.append(word)
                #print(word)
        return words
