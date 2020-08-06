frase = input ("Digite a palavra Secreta: ").split()
tamanho = len(frase)
print(tamanho)

c=0
let = []

for c in range(0,tamanho):
    print(frase[c])
    print(len(frase[c]))
    let.append(frase[c].count('o'))
    c = c + 1
print(let)

soma = 0
for c in let:
    soma = soma + c
print(soma)


#print(frase[0].find('o'))
#print(str(''.join(palavra)))