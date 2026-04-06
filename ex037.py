#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual
#será a base de conversão: 1 para binário, 2 octal, 3 hexadecimal
number = int(input('Digite um número inteiro: '))
option = int(input('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRI0
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
'''))
print('Sua opção: {}'.format(option))
if option == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(number, bin(number)[2:]))
elif option == 2:
    print('{} convertido para OCTAL é igual a {}'.format(number, oct(number)[2:]))
elif option == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(number, hex(number)[2:]))
else:
    print('Opção inválida!!')