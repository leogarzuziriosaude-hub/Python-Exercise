#Desenvolva um programa que leia o comprimeiro de três segmentos de reta e diga ao usuário
#se ela podem ou não formar um triângulo
print('-=' * 30)
print('Analisador de Existência de Triângulo')
print('-=' * 30)
a = float(input('Primeiro seguimento: '))
b = float(input('Segundo seguimento: '))
c = float(input('Terceiro seguimento: '))
if a + b > c and b + c > a and a + c > b:
    print('Os seguimentos acima podem formar um triânculo!!')
else:
    print('Os seguimentos acima não podem formar um triângulo.')