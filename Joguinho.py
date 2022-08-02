from time import sleep
from random import randint

computador = randint(0, 5) # Faz o computador "PENSAR"
print('\033[0;49;31m-=-' * 20)
print('-=-' * 20)
print('\033[0;49;95mVou pensar em um numero entre 0 e 5. Tente adivinhar... ')
print('-=-' * 20)
print('\033[0;49;33m-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tentando advinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabéns você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}!')


sleep(1)







