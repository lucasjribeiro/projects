n1 = float(input('\nDigite a Nota da AV1: '))
n2 = float(input('Digite a Nota da AV2: '))
if (n1 + n2) / 2 >= 7:
    print ('\nParabéns, Você foi APROVADO!')
else:
    print ('\nVocê não atingiu a Média adequada.')
    print ('Mas ainda tem a última Avaliação.')
    
if (n1 + n2) / 2 >= 9:
    print ('Ótima Nota, Continue assim Empenhado!')
    
if (n1 + n2) / 2 < 7:
    n3 = float(input('\nDigite a Nota da AV3: '))
    a = (n3 + n1) / 2 >= 7
    b = (n3 + n2) / 2 >= 7
    if a == True or b == True:
        print('\nParabéns, Você foi APROVADO!')
    else:
        print('\nInfelizmente Você foi REPROVADO!')
        print('Pois não atingiu a Nota Adequada.')
