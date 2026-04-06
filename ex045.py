import time
import random
option = int(input('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
Qual a sua jogada? '''))
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!!')
time.sleep(0.5)
choice = random.choice([1, 2, 3])
if choice == 1:
    resultado_pc = 'PEDRA'
elif choice == 2:
    resultado_pc = 'PAPEL'
elif choice == 3:
    resultado_pc = 'TESOURA'
print('{}'.format('-=' * 20))
if option == 1:
    resultado = 'PEDRA'
elif option == 2:
    resultado = 'PAPEL'
elif option == 3:
    resultado = 'TESOURA'
print('Computador jogou {}'.format(resultado_pc))
print('Jogador jogou {}'.format(resultado))
print('{}'.format('-=' * 20))
if resultado == resultado_pc:
    print('EMPATE')
elif resultado == 'PEDRA' and resultado_pc == 'PAPEL':
    print('DERROTA')
elif resultado == 'PEDRA' and resultado_pc == 'TESOURA':
    print('VITÓRIA')
elif resultado == 'PAPEL' and resultado_pc == 'PEDRA':
    print('VITÓRIA')
elif resultado == 'PAPEL' and resultado_pc == 3:
    print('DERROTA')
elif resultado == 'TESOURA' and resultado_pc == 'PEDRA':
    print('VITÓRIA')
elif resultado == 'TESOURA' and resultado_pc == 'PAPEL':
    print('VITÓRIA')
