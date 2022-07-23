#Jogo Forca

import random
import string
from palavras import words
from grafico import lives_visual_dict

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def forca():
    word = get_valid_word(words)
    word_letters = set(word)
    alfabeto = set(string.ascii_uppercase)
    used_latters = set()
    lives = 7
    
    #input
    while len(word_letters) > 0 and lives != 0:
        print("\033c") #clear log
        print(lives_visual_dict[lives])
        word_list = [letter if  letter in used_latters else '_' for letter in word]
        print('Palavra: ',' '.join(word_list))
        print('Letras usadas: ',' '.join(used_latters))
        print('Vidas:',lives)
        
        user_letter = input('Escolha uma letra: ').upper()
        if user_letter in alfabeto - used_latters:
            used_latters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
        elif user_letter in used_latters:
            print('Voce ja usou essa letra seu burro') 
        else:
            print('Letra invalida')   
    print("\033c")       
    if lives == 0:
        print('Mureu, a palavra era:',word)
    else:
        print('GG')


forca()