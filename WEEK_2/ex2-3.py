false_guess = True
_min = 0
_max = 100
initial = 0
str1 = 'Enter \'h\''
str2 = 'to indicate the guess is too high. Enter \'l\' '
str3 = 'to indicate the guess is too low. Enter \'c\' '
str4 = 'to indicate I guessed correctly. '

print('Please think of a number between 0 and 100!')
while(false_guess):
    guess = initial + (_max - _min) // 2
    print('Is your secret number ' + str(guess) + '?')
    i = input(str1 + str2 + str3 + str4)
    if (i == 'c'):
        print('Game over. Your secret number was:', guess)
        false_guess = False
    elif (i == 'l'):
        _min = guess
        initial = _min
    elif (i == 'h'):
        _max = guess
    else:
        print('Sorry, I did not understand your input.')