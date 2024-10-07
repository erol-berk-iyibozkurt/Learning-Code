# Bagels - 
# 

import random

NUM_DIGITS = 3 # to create the digit of the secret number
MAX_GUESSES = 10 # to decide the attempt of the guesses

def getSecretNum():
    # for the number made by randomize
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess,secretNum):
    if guess == secretNum:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi') # the place and the number is correct
        elif guess[i] in secretNum:
            clues.append('Pico') # the number is correct, the place is incorrect
    if len(clues) == 0:
        return 'Bagels'# neither place nor number is wrong.
    else:
        clues.sort()
        return ' '.join(clues)

def main():
    print('''Bagels, a deductive logic game.
You're very welcome!
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is.

Here is some clues for you:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct. 

For example, if the secret number was 248 and your guess as 843, theclues would be Fermi Pico.'''.format(NUM_DIGITS))
    
    while True:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')
    
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
    
            if guess == secretNum:
                break  # They're correct, so break out of this loop.
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))
    
        # Ask player if they want to play again.
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

if __name__ == '__main__':
    main()