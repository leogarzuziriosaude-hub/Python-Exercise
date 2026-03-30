#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
#e o último nome separadamente.
name = str(input('Digite seu nome completo: ')).strip()
namelist = name.split()
print('Muito prazer em te conher!')
print('Seu primeiro nome é {}'.format(namelist[0]))
print('Seu último nome é {}'.format(namelist[-1]))
