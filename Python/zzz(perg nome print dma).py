#x, maior, menor = float
#i, pos_maior, pos_menor, n_troca_maior, n_troca_menor = int
x = float(input('Digite um Número: '))
maior = float(x)
menor = float(x)
i = int(1)
n_troca_maior = int(0)
n_troca_menor = int(0)
pos_maior = int(1)
pos_menor = int(1)
while (x != 9999):
    if (x > maior):
        maior = x
        pos_maior = i
        n_troca_maior = n_troca_maior + 1
    else:
        if (x < menor):
            menor = x
            pos_menor = i
            n_troca_menor = n_troca_menor + 1
    x = float(input('Digite um Número: '))
    i = i + 1
print('\nMaior Elemento = {};  Posição do Maior Elemento = {};  Quantidade de Trocas para achar o Maior Elemento = {}'.format(maior, pos_maior, n_troca_maior))
print('Menor Elemento = {};  Posição do Menor Elemento = {};  Quantidade de Trocas para achar o Menor Elemento = {}'.format(menor, pos_menor, n_troca_menor))
