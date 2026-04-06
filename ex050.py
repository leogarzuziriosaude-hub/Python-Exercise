sum = 0
cont = 0
for x in range(1,7):
    x = int(input('Digite o {}º valor: '.format(x)))
    if x % 2 == 0:
        sum += x
        cont += 1
print('Você informou {} números pares e a soma foi {}.'.format(cont, sum))
