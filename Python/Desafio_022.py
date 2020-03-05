nome = input('Qual é o seu nome completo? ').strip()                            #tirar os espaços do início e fim
print ('Seu nome em letras Maiúsculas: {}'.format(nome.upper()))
print ('Seu nome em letras Minúsculas: {}'.format(nome.lower()))
print ('Seu nome completo tem {} letras'.format(len(nome) - (nome.count(' ')))) #Quantidade de caracteres menos os espaços
#dividir = nome.split()
#print (dividir[0])
print ('Seu primeiro nome tem {} letras'.format(nome.find(' ')))                #Quantas letras tem o primeiro nome
