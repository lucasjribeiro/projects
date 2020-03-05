import random
li = [0, 1, 2, 3, 4, 5]
va = random.choice(li)
print(' • ' * 10)
print('TENTE ADIVINHAR QUAL FOI O NÚMERO SORTEADO ENTRE 0 E 5:')
print(' • ' * 10)
ad = int(input('Digite o número: '))
if ad == va:
    print('VOCÊ ACERTOU, PARABÉNS!!!')
    print('O número Sorteado foi {}.'.format(va))
else:
    print('VOCÊ ERROU, TENTE NOVAMENTE!')
    print('O número Sorteado foi {}.'.format(va))
