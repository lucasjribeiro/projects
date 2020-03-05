import math
angulo = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print ('O valor de Seno é:.    {:.14f}'.format(seno))
print ('O valor de Cosseno é:  {:.14f}'.format(cosseno))
print ('O valor de Tangente é: {:.14f}'.format(tangente))