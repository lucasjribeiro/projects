va = float(input('Valor do Produto: R$'))
d10 = 90 * va / 100
d05 = 95 * va / 100
j20 = 120 * va / 100
print('\nConsiderando...')
print('1 para À Vista no Dinheiro ou Cheque')
print('2 para À Vista no Cartão')
print('3 para até 2X no Cartão')
print('4 para 3X ou mais no Cartão')
fo = int(input('\nDigite a Forma de Pagamento: '))
if fo == 1:
    print('O valor do Produto é R${:.2f}, mas com 10% de Desconto vai para R${}'.format(va, d10))
if fo == 2:
    print('O valor do Produto é R${:.2f}, mas com 5% de Desconto vai para R${}'.format(va, d05))
if fo == 3:
    print('O valor do Produto é R${:.2f}'.format(va))
if fo == 4:
    print('O valor do Produto é R${:.2f}, mas com 20% de Juros vai para R${}'.format(va, j20))
