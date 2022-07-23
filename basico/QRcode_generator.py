from dataclasses import dataclass
import qrcode
import os

data = input('Escreva a frase ou link a ser convertido como QR code:')
img = qrcode.make(data)
print('Salvo em: '+os.path.dirname(os.path.realpath(__file__)))
img.save(os.path.dirname(os.path.realpath(__file__))+'/qrcode.png')

os.system("pause")