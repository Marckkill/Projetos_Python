#Jogo de acertar o numero randomico

import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x} '))
        if guess > random_number:
            print('Wrong. Too high. ')
        elif guess < random_number:
            print('Worng. Too low ')
    print(f'Congratz you got it right!! the nunmber was {random_number} ')

guess(10)