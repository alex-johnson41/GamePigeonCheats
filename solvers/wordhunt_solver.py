import copy
from typing import Dict, List


class WordHunt_Solver():

    def __init__(self, letters: List[str]):
        self.wordList = {} #List of all english words whose length is >= 3
        self.solutions = [] #Words that can be made using the grid
        self.letters2D = [] #2D array of letters on board
        self.letters = [] #1D array of letters on board
        self.usedLetters2D = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
        self.letterPath = [] #2D array recording the path to draw the letters
        self.processInput(letters)
        self.wordList = self.createWordList()

    def createWordList(self) -> Dict[str, str]:
        wordList = {}
        file = open('word_lists/wordhunt_wordlist.txt')
        for line in file:
            line = line.strip()
            wordList[line] = line
        return wordList

    def processInput(self, letters: List[str]):
        x = 0
        for i in range(4):
            a = []
            for j in range(4):
                a.append(letters[x])
                self.letters.append(letters[x])
                x += 1 
            self.letters2D.append(a)
            
    def solve(self) -> Dict[str, List[List[int]]]:
        solutionsDict: Dict[str, List[List[int]]] = {} 
        for word in self.wordList: 
            if self.wordIsPossible(word):
                if self.checkForWord(word):
                    solutionsDict[word] = copy.deepcopy(self.letterPath) #Copies the values from letterpath to the dictionary with the word
        answers = sorted(list(solutionsDict.items()), key = lambda key : len(key[0]), reverse=False) #Sorts dictionary by the length of the key (the word)
        sortedAnswers = {ele[0] : ele[1]  for ele in answers}
        return sortedAnswers

    #If all the letters for the word aren't in the grid, go to the next word     
    def wordIsPossible(self, word: str) -> bool: 
        for letter in word:     
            if letter not in self.letters: 
                return False
        return True

    #Checks to see if the word can be created using the grid
    def checkForWord(self, word: str) -> bool:
        startingSpots = self.getOccurances(word[0], self.letters) #Indexes of starting letter on the grid
        for i in startingSpots: #For each possible starting position (Repeat letters)
            self.resetUsedLetters()
            row = i // 4 
            column = i % 4 
            self.usedLetters2D[row][column] = 1 #Mark the position as the start of the word
            if self.findNextLetter(row, column, word, 1): #Recursively search for each letter
                return True
        return False

    #Recursive function to find a path for the word on the board
    def findNextLetter(self, startRow: int, startColumn: int, word: str, letterIndex: int) -> bool: #type: ignore
        if letterIndex >= len(word): #If it's reached the end of the word
            self.letterPath = self.usedLetters2D.copy()
            self.usedLetters2D[startRow][startColumn] = 3 #Mark last letter of word
            return True #Once this point is hit it means a path for the word has been found   
        
        numOfNextLetters = self.getOccurances(word[letterIndex], self.letters) #Find occurances of desired letter on board
        for i in numOfNextLetters: #Loop through possible letter locations
            #Calculate the row and column of the desired letter
            nextLetterRow = i // 4 
            nextLetterColumn = i % 4 
            #Figure out if the desired letter is adjacent or diaganol to the current letter and if the desired letter has already been used
            if (startRow - nextLetterRow > -2 and startRow - nextLetterRow < 2 and startColumn - nextLetterColumn > -2 
            and startColumn - nextLetterColumn < 2 and self.usedLetters2D[nextLetterRow][nextLetterColumn] == 0): 
                self.usedLetters2D[nextLetterRow][nextLetterColumn] = 2 #Mark the desired letter as used
                found = self.findNextLetter(nextLetterRow, nextLetterColumn, word, letterIndex + 1) #Call the function again and move onto the next letter
                if found: #If a path for the word was found, bounce back up through stack frames
                    return True
        self.usedLetters2D[startRow][startColumn] = 0 

    #Resets the grid showing what letters have been used
    def resetUsedLetters(self):
        for i in range(4):
            for j in range(4):
                self.usedLetters2D[i][j] = 0

    #Get indexes of occurances of a character in a list
    def getOccurances(self, char: str, list: List[str]) -> List[int]:
        indices = []
        for idx, value in enumerate(list):
            if value == char:
                indices.append(idx)
        return indices
