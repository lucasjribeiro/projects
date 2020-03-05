'''s=float(input('Salário: '))
ch=int(input('Carga Horária: '))


f=int(input('Números de Faltas: '))
if f != 0:
    ds=int(input('As faltas ocorreram em quantas semanas diferentes? '))
else:
    ds=0
a=int(input('Horas de Atraso: '))


pe=int(input('Tem Periculosidade?\nSe [SIM] Digite [1]:\nSe [NÃO] Digite [0]: '))
if pe == 1:
    pe=30*(s/30*(30-f-ds))/100
else:
    pe=0


insa=int(input('Tem Insalubridade?\nSe [NÃO] Digite [0]:\nSe for [GRAU MÍNIMO] Digite [1]:\nSe for [GRAU MÉDIO] Digite [2]:\nSe for [GRAU MÁXIMO] Digite [3]: '))
if insa == 1:
    insa=10*998/100
if insa == 2:
    insa=20*998/100
if insa == 3:
    insa=40*998/100
if insa == 0:
    insa=0


adnot=float(input('Horas Noturnas trabalhadas: '))
adnot=adnot*60/52.5
adnot=(s+pe+insa)/ch*0.2*adnot


#print('{:.2f}'.format(adnot))

# (gratificação) editar.........


fezhe=int(input('Fez Horas Extras?\n[SIM] Digite [1]:\n[NÃO] Digite [0]: '))
if fezhe == 1:
    hextra=int(input('Horas extras SIMPLES: Digite [0]\nHoras Extras PROPORCIONAIS: Digite [1] '))
    if hextra == 0:
        he=float(input('Horas Extras Realizadas: '))
        porc=float(input('Porcentagem de Acréscimo da Hora Extra: '))
        porc=(porc/100)+1
        he=(s+pe+insa)/ch*porc*he

    if hextra == 1:
        porc=float(input('Porcentagem de Acréscimo da Hora Extra: '))
        porc=(porc/100)+1

        hec=float(input('Horas Extras Realizadas EXCETO no Período das (22h às 5h), Feriados e Finais de Semanas: '))
        hec=(s+pe+insa)/ch*porc*hec

        hefe=float(input('Horas Extras Realizadas SOMENTE em Feriados e Finais de Semanas, EXCETO no Período das (22h às 5h): '))
        hefe=(s+pe+insa)/ch*2*hefe

        henot=float(input('Horas Extras NOTURNAS Realizadas no Período das (22h às 5h), EXCETO nos Feriados e Finais de Semana: '))
        henot=((s+pe+insa)/ch*porc)*0.2*henot

        henotfe=float(input('Horas Extras NOTURNAS Realizadas no Período das (22h às 5h) SOMENTE nos Feriados e Finais de Semana: '))
        henotfe=((s+pe+insa)/ch*2)*0.2*henotfe

        he=hec+hefe+henot+henotfe

if fezhe == 0:
    he=0


du=int(input('Dias Úteis do Mês, Considerando os Sábados: '))
dnu=int(input('Dias NÃO Úteis do Mês, Considerando Domingos e Feriados: '))
dsrhe=he/du*(dnu-ds)
dsradnot=adnot/du*(dnu-ds)


#   Já foi Definido   [Salário,  Carga Horária,  Falta,  DSR,  Atraso,  Periculosidade,  Insalubridade,  Adc. Noturno,  Hora Extra]


#      [DESCONTOS]



dependente=int(input('Número de Dependentes: '))
dependente=189.59*dependente


pensao=int(input('Paga Pensão?\nSe [SIM] Digite [1]:\nSe [NÃO] Digite [0]: '))
if pensao == 1:
    pensao=float(input('Qual o Valor?  R$'))
else:
    pensao=0    '''


vt=int(input('Quantas Passagens você usa para SOMENTE ir ao Trabalho? '))
for c in range(0,vt):
    
    li=float(input('Valor da {} Passagem: '.format(c+1)))
    if li > 0:
        va=li


print(va)
print(ve)
print(vi)

print(li+li)
'''falta=(s+pe+insa)/30*f
dsr=(s+pe+insa)/30*ds
atraso=(s+pe+insa)/ch*a

if f != 0:
    binss=s-falta-dsr-atraso
else:
    binss=s-falta-atraso

if binss <= 1751.81:
    inss=binss*8/100
if binss > 1751.81 and binss <= 2919.72:
    inss=binss*9/100
if binss >= 2919.73 and binss <= 5839.45:
    inss=binss*11/100
if binss > 5839.45:
    inss=5839.45*11/100

birrf=binss-inss-dependente

if birrf <= 1903.98:
    salario=birrf
    ir=0
if birrf >=1903.99 and birrf <=2826.65:
    ir=birrf*7.5/100-142.80
    salario=birrf-ir
if birrf >=2826.66 and birrf <=3751.05:
    ir=birrf*15/100-354.80
    salario=birrf-ir
if birrf >=3751.06 and birrf <=4664.68:
    ir=birrf*22.5/100-636.13
    salario=birrf-ir
if birrf > 4664.68:
    ir=birrf*27.5/100-869.36
    salario=birrf-ir

fgts=binss*8/100

print('\n\n\nPROVENDOS\n  SALÁRIO = R${:.2f}\n\n'.format(s))
print('DESCONTOS\n  {} FALTA = R${:.2f}\n  {} DSR = R${:.2f}\n  {} HORAS DE ATRASO = R${:.2f}\n'.format(f, falta, ds, dsr, a, atraso))
print('  INSS = R${:.2f}\n  IRRF = R${:.2f}\n\n'.format(inss, ir))
print('TOTAL DE DESCONTOS = R${:.2f}\n\n'.format(falta + dsr + atraso + inss + ir))
print('SALÁRIO LÍQUIDO = R${:.2f}\n\n'.format(salario))
print('FGTS = R${:.2f}'.format(fgts))
'''
