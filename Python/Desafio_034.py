print('\nVocê receberá um Aumento')
sa = int (input('Qual é o seu Salário ?  R$'))
a = (115 * sa) / 100
b = (110 * sa) / 100
if sa <= 1250:
    print('Seu novo Salário será R${:.2f}'.format(a))
else:
    print('Seu novo Salário será R${:.2f}'.format(b))
