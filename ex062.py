print('GERADOR DE PA')
print('-=' * 10)
first = int(input('Primeiro termo: '))
reason = int(input('Razão da PA: '))
term = first
cont = 1
total = 0
plus = 10
while plus != 0:
    total += plus
    while cont <= total:
        print('{} → '.format(term), end = '')
        term += reason
        cont += 1
    print('PAUSA')
    plus = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
