from typing import List


class Wordbites_Solver:

    def __init__(self, sLetters: List[str], hLetters: List[str], vLetters: List[str]):
        self.singleLetters: List[str] = [] #Single letters on the board
        self.horizontalLetters: List[str] = [] #Horizontal letter pairs
        self.verticalLetters: List[str] = [] #Vertical letter pairs
        self.wordList: dict[str, str] = {} #Dictionary of english words
        self.createWordList()
        self.processInput(sLetters, hLetters, vLetters)

    def createWordList(self):
        file = open('word_lists/wordbites_wordList.txt')
        for line in file:
            line = line.strip()
            self.wordList[line] = line

    def processInput(self, sLetters: List[str], hLetters: List[str], vLetters: List[str]):
        for letter in sLetters:
            self.singleLetters.append(letter)
        for i in range(0, len(hLetters), 2):
            self.horizontalLetters.append(hLetters[i] + hLetters[i+1])
        for i in range(0, len(vLetters), 2):
            self.verticalLetters.append(vLetters[i]  + vLetters[i+1])

    def getAllLetters(self) -> List[str]:
        allLetters: List[str] = []
        for letter in self.singleLetters:
            allLetters.append(letter)
        for letter in self.verticalLetters:
            for char in letter:
                allLetters.append(char)
        for letter in self.horizontalLetters:
            for char in letter:
                allLetters.append(char)
        return allLetters

    def solve(self) -> List[str]:
        vOptions: List[str | List[str]] = self.verticalCombinations() #Tiles on board organized for creating vertical combinations
        hOptions: List[str | List[str]] = self.horizontalCombinations() #Same as above but horizontal.
        vSolutions: List[str] = [] #Vertical Solutions
        hSolutions: List[str] = [] #Horizontal Solutions
        for word in self.wordList: 
            if self.wordIsPossible(word):
                if self.checkForWord(word, vOptions): #See if the word can be made using the tiles vertically
                    vSolutions.append(word)
                elif self.checkForWord(word, hOptions): #See if word can be made horizontallly
                    hSolutions.append(word)
        for idx, word in enumerate(vSolutions):
            vSolutions[idx] = "VERTICAL     " + word
        for idx, word in enumerate(hSolutions):
            hSolutions[idx] = "HORIZONTAL   " + word
        answers = vSolutions + hSolutions
        answers = sorted(answers, key=len, reverse=True)
        return answers

    #If all the letters for the word aren't on the board, go to the next word     
    def wordIsPossible(self, word: str) -> bool: 
        allLetters = self.getAllLetters() #Combine all letters on the board to one list
        for letter in word:     
            if letter not in allLetters: 
                return False
        return True

    #Attempt to build the word 
    def checkForWord(self, word: str, options: List[str | List[str]]) -> bool:
        startingSpots = self.getOccurances(word[0], options) #Indexes of starting spots
        for i in startingSpots:
            usedLetters = self.resetUsedLetters(len(options))
            usedLetters[i] = 1
            if isinstance(options[i],str) and len(options[i]) > 1 and str(options[i])[1] == word[1]:
                if self.findNextLetter(word, 2, usedLetters, options):
                    return True
            elif (isinstance(options[i],str) and len(options[i]) ==1) or isinstance(options[i], list):
                if self.findNextLetter(word, 1, usedLetters, options):
                    return True
        return False

    def findNextLetter(self, word: str, letterIndex: int, usedLetters: List[int], options: List[str | List[str]]) -> bool: #type: ignore
        if letterIndex < len(word):
            numOfNextLetters = self.getOccurances(word[letterIndex], options)
            for i in numOfNextLetters:
                if usedLetters[i] == 0:
                    if isinstance(options[i], str) and len(options[i]) >1: #If an option is a string longer than one char
                        try:
                            if options[i][1] == word[letterIndex + 1]: #If the second char is correct
                                usedLetters[i] = 1
                                found = self.findNextLetter(word, letterIndex + 2, usedLetters, options)
                                if found:
                                    return True
                        except: 
                            pass
                    else:
                        usedLetters[i] = 1
                        found = self.findNextLetter(word, letterIndex + 1, usedLetters, options)
                        if found:
                            return True
            usedLetters[letterIndex] = 0
        else:
            return True

    #Returns index of occurances of a char within a list
    def getOccurances(self, char: str, list: List[str | List[str]]) -> List[int]:
        indices = []
        for idx, value in enumerate(list): #Loop through list fed in
            if isinstance(list[idx], List): #If item is a list
                for item in list[idx]: #Loop through the list to test if any chars are what we need
                    if item == char:
                        indices.append(idx)
                        break
            else:
                if value[0] == char:
                    indices.append(idx)
        return indices

    def resetUsedLetters(self, num: int) -> List[int]:
        usedLetters = []
        for i in range(num):
            usedLetters.append(0)
        return usedLetters

    def verticalCombinations(self) -> List[str | List[str]]:
        letters = []
        for letter in self.singleLetters:
            letters.append(letter)
        for letter in self.verticalLetters:
            letters.append(letter)
        for letter in self.horizontalLetters:
            listInHL = [] #List storing horizontal letter pairs
            for char in letter:
                listInHL.append(char)
            letters.append(listInHL)
        return letters

    def horizontalCombinations(self) -> List[str | List[str]]:
        letters = []
        for letter in self.singleLetters:
            letters.append(letter)
        for letter in self.horizontalLetters:
            letters.append(letter)
        for letter in self.verticalLetters:
            listInVL = [] #List storing vertical letter pairs
            for char in letter:
                listInVL.append(char)
            letters.append(listInVL) 
        return letters




    #OLD CODE ---- RUNS TOO SLOWLY

    #def getCombinations(letters):
    #    combinations = []
    #    for r in range(8,3,-1):
    #        for combination in itertools.permutations(letters, r):
    #            if len(combination) > 2:
    #                combinations = getMoreCombinations(combination, combinations)
    #                print(combination)
    #    return combinations

    #def convertCombinationsToStr(combinations):
    #    newCombinations = []
    #    for combination in combinations:
    #        temp = ""
    #        for letter in combination:
    #            temp += letter
    #        newCombinations.append(temp)
    #    return newCombinations

    #def getMoreCombinations(combination, combinations):
    #    for idLetter, letter in enumerate(combination):
    #        if type(letter) is not str: # If the letter in the combination is a list of letters

    #            temp = list(combination)
    #            temp[idLetter] = letter[0] # Set the letter to the first letter in the list
    #            getMoreCombinations(tuple(temp), combinations) # Start over 
    #            
    #            temp = list(combination)
    #            temp[idLetter] = letter[1] # Set the letter to the second letter in the list
    #            getMoreCombinations(tuple(temp), combinations) # Start over
    #    if all(isinstance(letter,str) for letter in combination):
    #        temp = ""
    #        for letter in combination:
    #            temp += letter
    #        if temp in wordList and temp not in combinations:
    #            print(temp)
    #            combinations.append(temp) #Once there are no more letters that are lists, append
    #                                         #each combination to combinations list
    #    return combinations


    #def combineBlocks():

    #    vCombos = verticalCombinations()
    #    hCombos = horizontalCombinations()

    #    words = vCombos + hCombos
    #    print(combos)

    #    words = set(combos).intersection(wordList)
    #    vCombos = sorted(vCombos, key = len, reverse = True)
    #    hCombos = sorted(hCombos, key = len, reverse = True)    
    #
    #    print("Vertical Words:")
    #    print(vCombos)
    #    print("Horizontal Words:")
    #    print(hCombos)
