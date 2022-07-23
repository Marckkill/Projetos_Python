#Jogo onde o computador tenta acertar o numero

import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'O numero {guess} esta muito alto(A), baixo(B) ou correto(C)').lower()
        if feedback == 'a':
                high = guess - 1
        elif feedback == 'b':
                low = guess + 1
        elif feedback == 'c':
            print(f'Boa! o numero era {guess}')
                    
computer_guess(10)