weight = float(input('Qual o seu peso? (Kg) '))
height = float(input('Qual a sua altura? (m) '))
IMC = weight / (height**2)
print('O seu IMC é {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Você está abaixo do peso normal.')
elif 18.5 <= IMC < 25:
    print('Você está no peso ideal.')
elif 25 <= IMC < 30:
    print('Você está com sobrepeso.')
elif 30 <= IMC < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')
