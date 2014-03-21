# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/Users/rich/OneDrive/edX 6.00.1x files/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    check = False
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            check = True
        else:
            return False
    return check



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    output = ''
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            output += secretWord[i]
        else:
            output += '_ '
    return output



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    output = ''
    for i in range(len(string.ascii_lowercase)):
        if string.ascii_lowercase[i] in lettersGuessed:
            output += ''
        else:
            output += string.ascii_lowercase[i]
    return output

    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    MAX_GUESSES = 8
    lettersGuessed = ''
    mistakesMade = 0
    # availableLetters = string.ascii_lowercase
    breakLine = '---------------'
    wordGuessed = False
    
    print('Welcome to the Hangman game.')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print(breakLine)
    
    while mistakesMade < MAX_GUESSES and not wordGuessed:
        print('You have ' + str(MAX_GUESSES - mistakesMade) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        letter = raw_input('Please guess a letter: ')
        if letter.lower() in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print(breakLine)
        else:
            lettersGuessed += letter.lower()
            if letter.lower() in secretWord:
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
                print(breakLine)
                if isWordGuessed(secretWord, lettersGuessed):
                    wordGuessed = True
            else:
                print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
                print(breakLine)
                mistakesMade += 1
    if wordGuessed:
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was ' + secretWord)
                


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
hangman('to')
