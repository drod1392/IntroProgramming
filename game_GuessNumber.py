## game_GuessNumber.py
#
# Number Guessing Game
# Try to guess the random number in 6 tries

# This imports a library to generate random numbers
# we will talk more about this soon
import random

secret = random.randint(1,99) # secret has the random number (of type integer)
guess = 0 # varaible for holding your guessed number
tries = 0 # how many guesses you have taken

print('I have a secret number...do you think you can guess what number im thiniking of?')
print('Its a number from 1 to 99. I\'ll give you 6 tries to get it.')

while guess != secret and tries < 6:
    guess = int(input('Whats your guess? '))
    if guess < secret:
        print("Your guess is too low...pick a larger number")
    elif guess > secret:
        print("Your guess is too high...pick a smaller number")
    tries = tries + 1

if guess == secret:
    print('You guessed my number! Are you a sorcerer?')
else:
    print('Sorry, no more guesses.')
    #print('My secret number was: '+ str(secret))
    print('My secret number was:', secret)
