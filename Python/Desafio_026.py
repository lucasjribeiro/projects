fr = input('Digite uma frase: ').upper() .strip()
print ('A letra A aparece {} vezes.'.format(fr.count('A')))
print ('A letra A aparece pela 1ª vez na posição {}.'.format(fr.find('A')+1))
print ('A letra A aparece pela última vez na posição {}.'.format(fr.rfind('A')+1))
