import string
import random
from numpy import loadtxt
from random import randrange
# Recieves input and handles all logic, behind filtering words from guess list.
class WordlyPy:
    guessWords = []
    bannedChars = []
    containChars = []
    usedWords = []
    indexChars = {

    }
    removedWords = []
    
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

    ''' Deals with situations where we have duplicate letters, ie
        MOLLY where the first l is grey, and the second is green. Since after the first l it'll be
        removed from our corpus, we check in our removed words if there are l > 1 chars in the word we return it to
        our corpus.
    
    '''
    def selfCleanDup(self, letter):
        print("RESTORED")
        for word in self.removedWords:
            if(word.count(letter) > 1):self.guessWords.append(word)
        
        for char in self.bannedChars:
            if(char != letter):self.filterBannedChar(char)
    def returnSize(self):
        return len(self.guessWords)
        
    def printGuessWords(self):
        for word in self.guessWords:
            print(word)

    def popRandWord(self):
        s = random.choice(self.guessWords)
        self.guessWords.remove(s)
        return s
    # Smart word is actually pretty dumb, gets caught in duplicate loops often with the letter 'o'
    def popSmartWord(self):
        def split(word):
            return [char for char in word]
        # Letter Frequencies.
        weights = {
            'a' : 10.5,
            'e' : 10,
            'r' : 7.2,
            'o' : 6.6,
            'i' : 6.1,
            "s" : 5.6,
            "t" : 5.6,
            'l' : 5.6,
            'n' : 5.2,
            'u' : 4.4,
            'y' : 3.8,
            'c' : 3.6,
            'd' : 3.3,
            'h' : 3.1,
            'm' : 3.1,
            'p' : 3.0,
            'b' : 2.7,
            'g' : 2.6,
            'k' : 2.1,
            'w' : 1.6,
            'f' : 1.6,
            'v' : 1.1,
            'z' : .6,
            'x' : .4,
            'j' : .4,
            'q' : .2
        }
        
        sum = 0
        max = 0
        Gword = ""
        for word in self.guessWords:
            arr = split(word)
            sum = 0
            for letter in arr:
                sum += weights.get(letter)
            if(sum > max):
                max = sum
                Gword = word
        print(Gword)
        self.guessWords.remove(Gword)
                
        return Gword




        

    """ Removes word from list if it contains character (FOR GREY)
        filterBannedChar("s") guessWords = ["self","blah","test"]
    
        Output ---> guessWords = ["blah","test"]
    """
    def filterBannedChar(self, banned):
        
        newGuesses = []
        if(banned in self.bannedChars or banned in self.containChars or banned in self.indexChars):return
        for word in self.guessWords:
            if(word.find(banned) == -1):
                newGuesses.append(word)
            else:
                self.removedWords.append(word)
        self.bannedChars.append(banned)
        self.guessWords = newGuesses
        self.selfClean()

    """ Removes word from list if letter is not in it. (FOR YELLOW)
        filterContainChar("s") guessWords = ["self","blah","test"]
    
        Output ---> guessWords = ["self","test"]
    """

    def filterContainChar(self, contain, index):
        newGuesses = []
        if(contain in self.bannedChars):self.selfCleanDup(contain)
        #if(contain in self.containChars or contain in self.indexChars):return
        if(contain in self.indexChars):return
        
        for word in self.guessWords:
            if(word.find(contain) != -1 and word[index] != contain):
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
        if(letter in self.bannedChars):self.selfCleanDup(letter)
        
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
        
        print("Number of words remaining " + str(len(self.guessWords)))


    #wp.filterBannedChar('s') GREY
    #wp.filterContainChar('s') YELLOW
    #wp.filterIndexChar('b',0) GREEN
    #wp.printFilters()
    #wp.printGuessWords()
