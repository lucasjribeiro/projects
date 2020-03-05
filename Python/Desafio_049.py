print('TABUADA')
n = int(input('Digite um número: '))
for c in range(0,11):
    print('{} x {:2} = {:2}'.format(n, c, n*c))
