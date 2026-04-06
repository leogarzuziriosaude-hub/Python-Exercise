print('=' * 30)
print('10 TERMOS DE UMA P.A.'.center(30))
print('=' * 30)
first = int(input('Primeiro termo: '))
reason = int(input('Razão: '))
tenth = first + (10 - 1) * reason
for c in range(first, tenth + reason, reason):
    print(c, end = ' → ')
print('ACABOU')