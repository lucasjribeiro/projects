from datetime import date
hoje = date.today().year
print('\033[1;4;31m~=~\033[m' * 17)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
ano = int(input('\nAno de Nascimento: '))
idade = hoje - ano
if idade <= 9:
    print('\nSua Categoria é MIRIM')
if idade > 9 and idade <= 14:
    print('\nSua Categoria é INFANTIL')
if idade > 14 and idade <= 19:
    print('\nSua Categoria é JÚNIOR')
if idade == 20:
    print('\nSua Categoria é SÊNIOR')
if idade > 20:
    print('\nSua Categoria é MASTER')
