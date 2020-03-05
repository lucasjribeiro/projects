p = float(input('\nQual é o seu Peso? '))
a = float(input('Qual é a sua Altura? '))
imc = p / (a**2)
print ('\nSeu IMC é {:.3f}'.format(imc))
if imc < 18.5:
    print('\n{: >19}'.format('(Abaixo do Peso)'))
if imc >= 18.5 and imc <= 25:
    print('\n{: >15}'.format('(peso ideal)'))
if imc > 25 and imc <= 30:
    print('\n{: >14}'.format('(Sobrepeso)'))
if imc > 30 and imc <= 40:
    print('\n{: >14}'.format('(Obesidade)'))
if imc > 40:
    print('\n{: >22}'.format('(Obesidade Mórbida)'))
