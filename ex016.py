#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua parte inteira
from math import trunc
n = float(input('Digite um número: '))
print('O número real {:.5f} tem a parte inteira {}'.format(n, trunc(n)))
