#Gerador de senhas

import random
import string


print('Gerador de Senhas')
alfabeto = string.ascii_letters+string.digits

numero = input('Quantas Senhas? ')
numero = int(numero)
tamanho = input('Tamanho da senha? ')
tamanho = int(tamanho)

print('')
print('Senhas:')

for pwd in range(numero):
    passwords = ''
    for c in range(tamanho):
        passwords += random.choice(alfabeto)
    print(passwords)


