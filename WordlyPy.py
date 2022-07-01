import string
import random
from numpy import loadtxt
from random import randrange
class WordlyPy:
    guessWords = []
    bannedChars = []
    containChars = []
    indexChars = {

    }
    
    attempts = 0

    def __init__(self, guessWords, attempts):
        self.guessWords = guessWords
        self.attempts = attempts
        pass
    def cleanText(self):
        for idx, x in enumerate(self.guessWords):
            self.guessWords[idx] = x.lower() 

    def selfClean(self):
        for clean in self.bannedChars:
            if(clean in self.containChars):
                self.bannedChars.remove(clean)
    def returnSize(self):
        return len(self.guessWords)
        
    def printGuessWords(self):
        for word in self.guessWords:
            print(word)

    def popRandWord(self):
        
        return random.choice(self.guessWords)

    """ Removes word from list if it contains character (FOR GREY)
        filterBannedChar("s") guessWords = ["self","blah","test"]
    
        Output ---> guessWords = ["blah","test"]
    """
    def filterBannedChar(self, banned):
        newGuesses = []
        if(banned in self.bannedChars):return
        for word in self.guessWords:
            if(word.find(banned) == -1):
                newGuesses.append(word)
        self.bannedChars.append(banned)
        self.guessWords = newGuesses
        self.selfClean()

    """ Removes word from list if letter is not in it. (FOR YELLOW)
        filterContainChar("s") guessWords = ["self","blah","test"]
    
        Output ---> guessWords = ["self","test"]
    """

    def filterContainChar(self, contain):
        newGuesses = []
        if(contain in self.containChars):return
        for word in self.guessWords:
            if(word.find(contain) != -1):
                newGuesses.append(word)
        self.containChars.append(contain)
        self.guessWords = newGuesses
        self.selfClean()

    """ Removes word from list if charcter is not at Index. (FOR GREEN)
        filterContainChar("s",0) guessWords = ["self","blah","test"]
    
        Output ---> guessWords = ["self"]
    """
    def filterIndexChar(self, letter,index):
        newGuesses = []
        for word in self.guessWords:
            if(len(word) > index and word[index] == letter):
                newGuesses.append(word)
        self.indexChars[letter] = index
        self.guessWords = newGuesses

    def printFilters(self):
        print("###############")
        print("Banned Letters")
        for ban in self.bannedChars:
            print(ban)
        print("Contains Letters")
        for con in self.containChars:
            print(con)
        print("Letters at Indices")
        for idx in self.indexChars:
            print(idx, self.indexChars[idx])

"""
with open("words.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

wp = WordlyPy(lines, 2)
wp.cleanText()
"""
#wp.filterBannedChar('s') GREY
#wp.filterContainChar('s') YELLOW
#wp.filterIndexChar('b',0) GREEN
#wp.printFilters()


#wp.printGuessWords()
