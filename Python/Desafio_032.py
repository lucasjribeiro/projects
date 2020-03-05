from datetime import date
print('Verificar se o Ano é Bissexto')
a = int(input('Digite o Ano: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O Ano de {} é Bissexto'.format(a))
else:
    print('O Ano de {} NÃO é Bissexto'.format(a))
