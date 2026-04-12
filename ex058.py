import random
pc_choice = random.randint(0, 10)
att = 1

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
guess = int(input('Qual é o seu palpite? '))
if guess > 10:
    print('Escolha um número entre 0 e 10!')

while guess != pc_choice:
    guess = int(input('Errou, mais uma tentativa: '))
    att += 1
    if guess > 10:
        print('Escolha um número entre 0 e 10!')
    if guess > pc_choice:
        print('Um pouco menos...')
    else:
        print('Um pouco mais...')
print(f'Você acertou com {att} tentativas. Parabéns!')
