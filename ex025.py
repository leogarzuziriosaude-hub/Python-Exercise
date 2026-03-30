#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
name = str(input('Qual é o seu nome completo? ')).strip()
n = "SILVA" in name.upper()
print('Seu nome tem silva? {}'.format(n))
