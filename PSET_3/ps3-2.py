def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    letter = ''
    slots = []

    # convert letterGuessed (list) to string called 'letter'
    for char in lettersGuessed:
        letter += char

    # make initial guess
    for char in secretWord:
        if char not in letter:
            slots.append('_ ')
        else:
            slots.append(char)

    # other guess, change underline to char if 
    # the guess is True
    i = 0
    for char in secretWord:
        for guess in lettersGuessed:
            if slots[i] == '_ ':
                if guess == char:
                    slots[i] = char
        i += 1

    letter = ''

    slots.reverse()
    #print slots
    while len(slots) > 0:
        letter += slots.pop()

    #print lettersGuessed
    return letter

