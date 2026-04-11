sum_age = 0
per_maxage = ''
max_age = 0
cont_fem = 0
cont_femage = 0

for c in range(1,5):
    print('----- {}ª PESSOA -----'.format(c))
    per = str(input('Nome: '))
    age = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).upper()
    if sex != 'F' or sex != 'M':
        print('Entrada inválida!!')

    if sex == 'F':
        if age < 20:
            cont_fem += 1


    sum_age += age
    if sex == "M":
        if age > max_age:
            max_age = age
            per_maxage = per

print('A média de idade do grupo é de {} anos'.format(sum_age / 4))
print('O homem mais velho tem {} e se chama {}.'.format(max_age, per_maxage))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(cont_fem))