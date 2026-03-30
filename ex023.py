#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
a = int(input('Informe um número inteiro: '))
print('Analisando o número {}'.format(a))
print('Unidade: {}' .format(a//1 % 10))
print('Centena: {}' .format(a//10 % 10))
print('Dezena: {}' .format(a//100 % 10))
print('Milhar: {}' .format(a//1000 % 10))
