print('=' * 40)
d = float(input('Quantidade de dias alugados: '))
k = float(input('Km percorridos: '))
total = (d * 60) + (k * 0.15)
#n1 = (d * 60)
#n2 = (k * 0.15)
print ('O valor total a ser pago é: R${:.2f}'.format(total))
