# Se a distância for maior que 200 km = 0.45 por km, senão 0.50
d = int(input('Digite a distância em km da Viagem que deseja fazer: '))
vc = 0.50 * d
vl = 0.45 * d
if d <= 200:
    print('O valor a ser pago é R${}.'.format(vc))
else:
    print('O valor anser pago é R${}.'.format(vl))
