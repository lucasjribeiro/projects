a = int(input('Comprimento da Reta 1: '))
b = int(input('Comprimento da Reta 2: '))
c = int(input('Comprimento da Reta 3: '))
if a <= b + c and b <= a + c and c <= a + b:
    print('Forma um Triângulo ',end='')
    if a == b and a == c and b == c:
        print('EQUILÁTERO')
    if a == b != c or a == c != b or b == c != a:
        print('ISÓSCELES')
    if a != b and a != c and b!= c:
        print('ESCALENO')
else:
    print('Não forma um Triângulo')
