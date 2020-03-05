print('\033[1;4;31m~=~\033[m' *17)
print('MÉDIA ESCOLAR')
n1 = float(input('Nota do 1º Bimestre: '))
n2 = float(input('Nota do 2º Bimestre: '))
n3 = float(input('Nota do 3º Bimestre: '))
n4 = float(input('Nota do 4º Bimestre: '))
m = ((n1+n2+n3+n4) / 4)
if m < 5:
    print('Você foi REPROVADO!')
if m >= 5 <= 6.9:
    print('Você está de RECUPERAÇÃO!')
if m >= 7:
    print('Você foi APROVADO!')
