#Escreva um programa que faça o computador "pensar" em um número inteiro
#entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
#pelo computador. O programa deverá escrever na tela se acertou ou erro.
import random
from random import choice
text = int(input('Digite um número inteiro entre 0 e 5: '))
numberlist = [0, 1, 2, 3, 4, 5]
n = random.choice(numberlist)
if n == text:
    print('Acertou mizeravi')
else:
    print('Burrão!!!')
print('O número escolhido foi {}'.format(n))
