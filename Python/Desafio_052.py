print ('É número primo ou não?')
n = int(input('Digite um número: '))

valor = 0
total = 0

for c in range(1, n + 1):
    print (c)
    if n % c == 0:
        valor = valor + 1
        total = total + c
        
print(valor)
print(total)

if valor == 2:
    print('NÚMERO PRIMO')
else:
    print('NÃO PRIMO')
