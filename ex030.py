#Crie um programa que leia um número inteiro e mostre na tela se ela é PAR ou ÍMPAR
number = int(input('Me diga um número inteiro qualquer: '))
div = (number)%2
if div == 0:
    print("O número {} é par".format(number))
else:
    print('O número {} é ímpar'.format(number))
