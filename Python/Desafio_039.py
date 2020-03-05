from datetime import date
hoje = date.today().year
print('\033[1;4;31m~=~\033[m' * 17)
print('ALISTAMENTO MILITAR')
nascimento = int(input('\nAno de Nascimento: '))
idade = hoje - nascimento
if idade < 18:
    print('\nVocê ainda vai se Alistar')
    falta = 18 - idade
    if falta == 1:
        print('Falta {} Ano'.format(falta))
    else:
        print('Faltam {} Anos'.format(falta))

if idade == 18:
    print('\nEstá na hora de se Alistar')

if idade > 18:
    print('\nJá passou do tempo de Alistamento')
    passa = idade - 18
    if passa == 1:
        print('Passou {} Ano'.format(passa))
    else:
        print('Passaram {} Anos'.format(passa))
