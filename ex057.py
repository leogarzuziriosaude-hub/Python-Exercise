sex = str(input('Qual o seu sexo? [M/F] ')).upper()
while sex != 'M' and sex != 'F':
    sex = str(input('Dados inválidos. Por favor informe seu sexo: [M/F] ')).upper()
print('Sexo {} registrado com sucesso'.format(sex))
