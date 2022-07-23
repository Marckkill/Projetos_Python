#Contador de tempo

import time

def timer(t):
    while t:
        mins, secs = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer,end="\r")
        time.sleep(1)
        t -= 1 
    print('\n')
    print('Fim')

t = input('Tempo em segundos: ')
timer(int(t))