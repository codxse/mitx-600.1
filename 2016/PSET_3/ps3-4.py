def isWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if lettersGuessed[-1] in secretWord;
      False otherwise
    '''
    if len(lettersGuessed) > 0:
        x = False
        for char in secretWord:
            if lettersGuessed[-1] == char:
                x = True
        return False or x
    else:
        return False

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
    nGuess = 8
    mistakeMade = 0
    isFullGuesses = False
    won = False
    lettersGuessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")

    while not isFullGuesses and not won:
        if nGuess > 0:
            print("-------------")
            print("You have %d guesses left." % nGuess)
            availableLetters = getAvailableLetters(lettersGuessed)
            print("Available letters: " + availableLetters)
            guessed = input("Please guess a letter: ")
            guessed = guessed.lower()
            lettersGuessed.append(guessed)
            listgw = lettersGuessed[:]

            guesses = getGuessedWord(secretWord, listgw)
             


            isWordx = isWord(secretWord, listgw)
            if isWordx:
                # if player alredy guessed same letter
                if listgw.count(guessed) > 1:
                    print("Oops! You've already guessed that letter: " + guesses)
                    listgw.pop()               
                else:
                    print('Good guess: ' + guesses)
                nGuess += 1
            else:
                if listgw.count(guessed) > 1:
                    print("Oops! You've already guessed that letter: " + guesses)
                    listgw.pop()
                    nGuess += 1
                else:
                    print('Oops! That letter is not in my word: ' + guesses)
            
            win = isWordGuessed(secretWord, listgw)
            if win:
                print("------------")
                print("Congratulations, you won!")
                won = True
        else: 
            # if number of guesses is 0, then stop.
            print("-------------")
            print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
            isFullGuesses = True

        if isFullGuesses == False:
            nGuess -= 1

