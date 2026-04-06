#Crie um programa que leia duas notas de um aluno e calcule sua média,
#morstrando uma mensagem final, de acordo com a média atingida
# Média abaixo de 5 = reprovado
#Média entre 5 e 6,9 = recup
#Média 7 ou superior aprovado
score1 = float(input('Primeira nota: '))
score2 = float(input('Segunda nota: '))
average = (score1 + score2) / 2
print('Tirando {:.1f} e {:.1f} a média do aluno é {:.1f}'.format(score1, score2, average))
if average >= 7:
    print('O aluno está APROVADO.')
elif average < 5:
    print('O aluno está REPROVADO.')
else:
    print('O aluno está de RECUPERAÇÃO.')