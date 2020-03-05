print('= ÷ =' * 10)
ve = int(input('Digite a velocidade do Carro: '))
if ve > 80:
    print('Você foi Multado!')
    mu = (ve - 80)
    pa = mu * 7
    print('O valor a ser pago é R${:.2f}'.format(pa))
