print('\033[1;4;31m~=~\033[m' *17)
print('EMPRÉSTIMO BANCÁRIO')
n1 = int(input('Valor da casa: '))
n2 = int(input('Salário do Comprador: '))
n3 = int(input('Em quantos Anos deseja Pagar? '))
pm = n1 / (n3 * 12)
if pm > 30 * n2 / 100:
    print('Infelizmente seu Empréstimo não foi aprovado')
else:
    print('O valor da Prestação Mensal será R${:.2f}'.format(pm))
