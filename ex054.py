import datetime
from datetime import date
cont_old = 0
cont_new = 0
ty = date.today().year
for c in range(1, 8):
    year = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if ty - year >= 18:
      cont_old += 1
    else:
        cont_new +=1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(cont_old))
print('E também tivemos {} pessoas menor de idade.'.format(cont_new))
