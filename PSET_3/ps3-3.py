def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    lettersGuessedLower = []
    letters = "abcdefghijklmnopqrstuvwxyz"
    letterTrim = ''
    letterList = []

    if len(lettersGuessed) > 0:
        # convert string letters to list of letter
        for letter in letters:
            letterList.append(letter)

        # convert letter guess to lowercase
        # assign to letteGuessedLower
        for char in lettersGuessed:
            char = char.lower()
            lettersGuessedLower.append(char)
        
        # remove char in letterList which same with character in letterGuessedLower
        for char in lettersGuessedLower:
            letterList.remove(char)

        # convert letterlist to string
        # remove letterlist (pop)
        letterList.reverse()
        while len(letterList) > 0:
            letterTrim += letterList.pop()

        return letterTrim
    else:
        return letters