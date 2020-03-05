from random import choice
from time import sleep
li = [1, 2, 3]
es = choice(li)
print('\033[1;4;31m~=~\033[m' * 17)
print('\nPEDRA, PAPEL & TESOURA')
jo = int(input('\nDigite...\n[1] para Pedra:\n[2] para Papel:\n[3] para Tesoura:  '))
if jo == 1:
    print('\nVocê escolheu PEDRA')
if jo == 2:
    print('\nVocê escolheu PAPEL')
if jo == 3:
    print('\nVocê escolheu TESOURA')
if jo != 1 and jo != 2 and jo != 3:
    print('\nOPÇÃO INVÁLIDA\nDigite: [1],[2] ou [3]\n')
sleep(1)
if es == 1:
    print('A Máquina escolheu PEDRA')
if es == 2:
    print('A Máquina escolheu PAPEL')
if es == 3:
    print('A Máquina escolheu TESOURA')
sleep(1)
if es == 1 and jo == 1:
    print('\n  \033[1;4mDeu EMPATE!!\033[m')
if es == 1 and jo == 2:
    print('\n  \033[1;4mVocê VENCEU!!\033[m')
if es == 1 and jo == 3:
    print('\n  \033[1;4mVocê PERDEU!!\033[m')
if es == 2 and jo == 1:
    print('\n  \033[1;4mVocê PERDEU!!\033[m')
if es == 2 and jo == 2:
    print('\n  \033[1;4mDeu EMPATE!!\033[m')
if es == 2 and jo == 3:
    print('\n  \033[1;4mVocê VENCEU!!\033[m')
if es == 3 and jo == 1:
    print('\n  \033[1;4mVocê VENCEU!!\033[m')
if es == 3 and jo == 2:
    print('\n  \033[1;4mVocê PERDEU!!\033[m')
if es == 3 and jo == 3:
    print('\n  \033[1;4mDeu EMPATE!!\033[m')
