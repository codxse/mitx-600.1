def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    x = False
    y = True
    for char in secretWord:
        if char in lettersGuessed:
            x = True
        else:
            y = False

    return x and y