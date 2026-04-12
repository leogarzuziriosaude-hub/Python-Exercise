import time

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
choice = 0

while choice != 5:
    choice = int(input('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Qual é a sua opção? '''))
    if choice == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
        print('==-' * 10)
        time.sleep(2)
        print()

    elif choice == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}')
        print('==-' * 10)
        time.sleep(2)

    elif choice == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2}, {n1} é maior!!')
        else:
            print(f'Entre {n1} e {n2}, {n2} é maior!!')
        print('==-' * 20)
        time.sleep(2)

    elif choice == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('==-' * 20)
        time.sleep(2)

    elif choice == 5:
        print('Finalizando...')
        print('==*' * 15)
        time.sleep(3)
        print('Fim do programa.')
    else:
        print('Entrada inválida, tente novamente!')