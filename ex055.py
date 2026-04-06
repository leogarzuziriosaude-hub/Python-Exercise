maior = 0
menor = 0
for c in range(1, 6):
    weigth = float(input('Peso da {}ª pessoa: '.format(c)))

    if c == 1:
        maior = weigth
        menor = weigth
    else:
        if weigth > maior:
            maior = weigth
        if weigth < menor:
            menor = weigth
print('O maior peso lido foi de {}Kg.'.format(maior))
print('O menor peso lido foi de {}Kg.'.format(menor))
