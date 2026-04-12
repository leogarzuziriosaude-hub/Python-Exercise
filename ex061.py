print('GERADOR DE PA')
print('-=' * 10)
first = int(input('Primeiro termo: '))
reason = int(input('Razão da PA: '))
term = first
cont = 1
while cont <= 10:
    print('{} → '.format(term), end = '')
    term += reason
    cont += 1
print('FIM')