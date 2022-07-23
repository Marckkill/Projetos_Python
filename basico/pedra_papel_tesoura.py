#Jogo pedra papel tesoura

import random

def play():
    user = input('escolha: pedra(1), papel(2) ou tesoura(3)')
    computer = print(random.choice([1,2,3]))
    
    if user == computer:
        return "Empate"
    
    if win:
        return "Ganhou"
    return "Perdeu"

def win(player,oponent):
    
    if (player == 1 and oponent ==3) or (player == 3 and oponent == 2) or (player == 2 and oponent == 1):
        return True
    
print(play())