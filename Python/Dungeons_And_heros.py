import random
import time

a1d = 5
zpgt = 5

vida = 15
fome = 0
sede = 2
sono = 5

cores = {'amarelo': '\033[33m',
         'vermelho': '\033[31m',
         'branco': '\033[30m',
         'magenta': '\033[35m',
         'ciano': '\033[36m',
         'limpa': '\033[m'}

print('\033[35mObrigado por jogar!\033[m\n'
      '\033[33mC\033[31mO\033[30mR\033[35mE\033[32mS\033[m\n'
      '{}Amarelo-Comentarios sobre onde você está\n'
      '{}Vermelho-Quando há perigo\n'
      '{}Branco-Escrituras\n'
      '{}ciano-Criaturas passivas\033[m\n'
      'Cinza-Alternativas\n'.format(cores['amarelo'], cores['vermelho'], cores['branco'], cores['ciano']))

ok = str(input('{}Suas unicas alternativas são 1 e 2,\n'
               'Você, para escolher podera escrever apenas\n'
               '1 ou 2 e apertar enter.\n'
               '{}NÃO APERTE ESPAÇO NO LUGAR QUE ESCOLHE\n'
               '1 OU 2 PARA EVITAR O ACONTECIMENTO DE BUGS!!\n \n \n {}'
               'Digite alguma coisa para ir ao jogo: '
               ''.format(cores['magenta'], cores['vermelho'], cores['limpa'])))

print('{}===========================================================================================================\n'
      '===============================CAPITULO 1 - A CAVERNA OU A FLORESTA?=======================================\n'
      '==========================================================================================================={}\n'
      ''.format(cores['magenta'], cores['limpa']))

a1 = int(input('''\n \n {}Você acorda em uma floresta,
você tem {} de vida, {} de fome,
{} de sede e {} de sono.
A sua direita você vê uma caverna{}.
(1)Entrar lá ou (2)andar para frente \n'''.format(cores['amarelo'], vida, fome, sede, sono, cores['limpa'])))

if a1 == 1:
    a1a = int(input('\n{}Você entra na caverna.\n'
                    'dentro da caverna você acha\num papel estranho.{}\n'
                    '(1)Abri-lo (2)não abrilo \n'
                    ''.format(cores['amarelo'], cores['limpa'])))

    if a1a == 1:
        print('\n \033[30m   Quem estiver lendo isso,\n'
              '    aqui fica um aviso, \n'
              '    não se aprofunde na caverna,\033[m\n'
              '    \033[31mou sofra as consequenias\033[m\n')
        a1b = int(input('{}Você fica um pouco assustado com isso.\n'
                        'Você entra mais para fundo da caverna ou sai dela?{}\n'
                        '(1)Adentrar mais a caverna (2)Sair dela\n'
                        ''.format(cores['amarelo'], cores['limpa'])))
        if a1b == 1:
            print('{}Você adentra mais a caverna.\n'
                  'Você se depara com uma escadaria de pedra,\n'
                  'a escadaria estava indo para baixo.{}\n'.format(cores['amarelo'], cores['limpa']))
            a1c = int(input('{}Você desce a escadaria com cuidado,\n'
                            'e vê uma pequena corda esticada no chão,\n'
                            'você imediatamente pença que aquilo pode ser \n'
                            'uma {}armadilha.{} Você a desarma ou pula ela?{}\n'
                            '(1)Desarmar(rolar um dado de 6 lados, se sair 3 ou menos, você morre!)\n'
                            '(2)Pular ela, evitando riscos de ativar a armadilha\n'
                            ''.format(cores['amarelo'], cores['vermelho'], cores['amarelo'], cores['limpa'])))
            dado1a = random.randint(0, 6)
            if a1c == 1:

                if dado1a >= 4:
                    print('{}Você desarmou com sucesso!!\n'
                          'Descendo mais as escadas,\n'
                          'você entra em uma sala, com um bau,\n'
                          'e do lado do bau tem um esqueleto.\n'
                          ''.format(cores['amarelo'], cores['limpa']))
                    a1d = int(input('(1)Você abre o bau\n'
                                    '(2)Você volta a superficie\n'))
                    if a1d == 1:
                        print('{}Você abre o bau e ele explode,\n'
                              'te matando, mas antes de você terminar\n'
                              'de abrir o bau, você lembra do que estava\n'
                              'escrito no papel. VOCÊ MORREU!!\n {}'
                              ''.format(cores['vermelho'], cores['limpa']))

                else:
                    print('{}Saiu no dado o numero {}\n'
                          'VOCÊ MORREU!!{}'.format(cores['vermelho'], dado1a, cores['limpa']))
            else:
                print('{}Você apenas pulou a armadilha.\n'
                      'Descendo mais as escadas, \n'
                      'Você entra em uma sala, com um bau, \n'
                      'e do lado do bau tem um esqueleto.{}\n'
                      ''.format(cores['amarelo'], cores['limpa']))
                a1d = int(input('(1)Você abre o bau\n'
                                '(2)Você volta a superficie\n'))
                if a1d == 1:
                    print('{}Você tenta abrir o bau,\n'
                          ' mas o esqueleto cria vida\n'
                          ' e tenta te atacar{}\n'
                          ''.format(cores['vermelho'], cores['limpa']))
                    a1e = int(input('(1)Você ataca o esqueleto(Rodar um dado de 12 lador e tira 7 ou mais)\n'
                                    '(2)Você corre(E arca com as consequencias de deixa-lo vivo\n'))
                    if a1e == 1:
                        dado12a = random.randint(0, 12)
                        if dado12a >= 7:
                            print('{}Você quebra o esqueleto!\n'
                                  'Você abre o bau ou não?{}\n'
                                  ''.format(cores['amarelo'], cores['limpa']))
                            a1f = int(input('(1)Sim\n'
                                            '(2)Não'))
                            if a1f == 2:
                                a1d = 2
                            if a1f == 1:
                                print('{}Você abre o bau'
                                      'e ele explode, mas'
                                      'antes de você terminar\n'
                                      'de abrir ele, você lembra'
                                      'do que estava escrito no papel.\n'
                                      'VOCÊ MORREU!!{}\n'
                                      ''.format(cores['vermelho'], cores['limpa']))
                        if dado12a <= 6:
                            print('{}Você tirou o número {}\n'
                                  'VOCÊ MORREU!!{}\n'
                                  ''.format(cores['vermelho'], dado12a, cores['limpa']))
                else:
                    print('{}Você corre para se salvar.\n'
                          'Ao subir a escadaria as preças,\n'
                          'esquece da armadilha que você\n'
                          'NÃO DESATIVOU, e acaba tropeçando nela,\n'
                          'instantaneamente, a escasa se abre,\n'
                          'fazendo com que você caia e um buraco\n'
                          'cheio de estacas, te perfurando e\n'
                          'te matando.\n'
                          'VOCÊ MORREU!!{}\n'.format(cores['vermelho'], cores['limpa']))
        else:
            print('{}Ao sair da caverna,\n'
                  'você se depara com um\n'
                  '{}Goblin{}, que ao te ver\n'
                  'parte para cima de você\n'
                  ''.format(cores['amarelo'], cores['vermelho'], cores['amarelo']))
            a1g = int(input('Você decide:'
                            '(1)Voltar a caverna\n'
                            '(2)Infrentar o Goblin\n'))
            if a1g == 1:
                print('{}Você volta para a caverna correndo,\n'
                      'e acaba pisando em uma armadilha sem\n'
                      'ver, que acaba abrindo um alçapão a\n'
                      'baixo de você, te levando para um fim\n'
                      'tragico.\n'
                      '   VOCÊ MORREU!!!{}\n'
                      ''.format(cores['vermelho'], cores['limpa']))
    else:
        print('{}Por não ter lido o que\n'
              'estava escrito no papel, você\n'
              'adentra mais a caverna e\n'
              'descuidosamente acaba pisando\n'
              'em uma armadilha.\n'
              '   VOCÊ MORREU!!{}\n'
              ''.format(cores['vermelho'], cores['limpa']))

if a1 == 2:
    print('{}Você começa a andar para frente\n'
          'e ve um {}Goblin{} vindo em sua \n'
          'direção.{}\n'
          ''.format(cores['amarelo'], cores['vermelho'], cores['amarelo'], cores['limpa']))
    a11 = int(input('(1)Você infrenta ele(rolar um dado de 12 lados e tirar 8 ou mais\n'
                    '(2)Você corre para dentro da caverna\n'))
    if a11 == 1:
        dado12b = random.randint(0, 12)
        if dado12b >= 8:
            print('{}Você mata o {}Goblin{}, mas com medo\n'
                  'do que poderia vir, você corre para\n'
                  'dentro da caverna.\n'
                  ''.format(cores['amarelo'], cores['vermelho'], cores['amarelo']))
            a1a = int(input('\n{}Você entra na caverna.\n'
                            'dentro da caverna você acha\num papel estranho.{}\n'
                            '(1)Abri-lo (2)não abrilo \n'
                            ''.format(cores['amarelo'], cores['limpa'])))

            if a1a == 1:
                print('\n \033[30m   Quem estiver lendo isso,\n'
                      '    aqui fica um aviso, \n'
                      '    não se aprofunde na caverna,\033[m\n'
                      '    \033[31mou sofra as consequenias\033[m\n')
                a1b = int(input('{}Você fica um pouco assustado com isso.\n'
                                'Você entra mais para fundo da caverna ou sai dela?{}\n'
                                '(1)Adentrar mais a caverna (2)Sair dela\n'
                                ''.format(cores['amarelo'], cores['limpa'])))
                if a1b == 1:
                    print('{}Você adentra mais a caverna.\n'
                          'Você se depara com uma escadaria de pedra,\n'
                          'a escadaria estava indo para baixo.{}\n'.format(cores['amarelo'], cores['limpa']))
                    a1c = int(input('{}Você desce a escadaria com cuidado,\n'
                                    'e vê uma pequena corda esticada no chão,\n'
                                    'você imediatamente pença que aquilo pode ser \n'
                                    'uma {}armadilha.{} Você a desarma ou pula ela?{}\n'
                                    '(1)Desarmar(rolar um dado de 6 lados, se sair 3 ou menos, você morre!)\n'
                                    '(2)Pular ela, evitando riscos de ativar a armadilha\n'
                                    ''.format(cores['amarelo'], cores['vermelho'], cores['amarelo'], cores['limpa'])))
                    dado1a = random.randint(0, 6)
                    if a1c == 1:

                        if dado1a >= 4:
                            print('{}Você desarmou com sucesso!!\n'
                                  'Descendo mais as escadas,\n'
                                  'você entra em uma sala, com um bau,\n'
                                  'e do lado do bau tem um esqueleto.\n'
                                  ''.format(cores['amarelo'], cores['limpa']))
                            a1d = int(input('(1)Você abre o bau\n'
                                            '(2)Você volta a superficie\n'))
                            if a1d == 1:
                                print('{}Você abre o bau e ele explode,\n'
                                      'te matando, mas antes de você terminar\n'
                                      'de abrir o bau, você lembra do que estava\n'
                                      'escrito no papel. VOCÊ MORREU!!\n {}'
                                      ''.format(cores['vermelho'], cores['limpa']))

                        else:
                            print('{}Saiu no dado o numero {}\n'
                                  'VOCÊ MORREU!!{}'.format(cores['vermelho'], dado1a, cores['limpa']))
                    else:
                        print('{}Você apenas pulou a armadilha.\n'
                              'Descendo mais as escadas, \n'
                              'Você entra em uma sala, com um bau, \n'
                              'e do lado do bau tem um esqueleto.{}\n'
                              ''.format(cores['amarelo'], cores['limpa']))
                        a1d = int(input('(1)Você abre o bau\n'
                                        '(2)Você volta a superficie\n'))
                        if a1d == 1:
                            print('{}Você tenta abrir o bau,\n'
                                  ' mas o esqueleto cria vida\n'
                                  ' e tenta te atacar{}\n'
                                  ''.format(cores['vermelho'], cores['limpa']))
                            a1e = int(input('(1)Você ataca o esqueleto(Rodar um dado de 12 lador e tira 7 ou mais)\n'
                                            '(2)Você corre(E arca com as consequencias de deixa-lo vivo\n'))
                            if a1e == 1:
                                dado12a = random.randint(0, 12)
                                if dado12a >= 7:
                                    print('{}Você quebra o esqueleto!\n'
                                          'Você abre o bau ou não?{}\n'
                                          ''.format(cores['amarelo'], cores['limpa']))
                                    a1f = int(input('(1)Sim\n'
                                                    '(2)Não'))
                                    if a1f == 2:
                                        a1d = 2
                                    if a1f == 1:
                                        print('{}Você abre o bau'
                                              'e ele explode, mas'
                                              'antes de você terminar\n'
                                              'de abrir ele, você lembra'
                                              'do que estava escrito no papel.\n'
                                              'VOCÊ MORREU!!{}\n'
                                              ''.format(cores['vermelho'], cores['limpa']))
                                if dado12a <= 6:
                                    print('{}Você tirou o número {}\n'
                                          'VOCÊ MORREU!!{}\n'
                                          ''.format(cores['vermelho'], dado12a, cores['limpa']))
                        else:
                            print('{}Você corre para se salvar.\n'
                                  'Ao subir a escadaria as preças,\n'
                                  'esquece da armadilha que você\n'
                                  'NÃO DESATIVOU, e acaba tropeçando nela,\n'
                                  'instantaneamente, a escasa se abre,\n'
                                  'fazendo com que você caia e um buraco\n'
                                  'cheio de estacas, te perfurando e\n'
                                  'te matando.\n'
                                  'VOCÊ MORREU!!{}\n'.format(cores['vermelho'], cores['limpa']))
                else:
                    print('{}Ao sair da caverna,\n'
                          'você se depara com um\n'
                          '{}Goblin{}, que ao te ver\n'
                          'parte para cima de você\n'
                          ''.format(cores['amarelo'], cores['vermelho'], cores['amarelo']))
                    a1g = int(input('Você decide:'
                                    '(1)Voltar a caverna\n'
                                    '(2)Infrentar o Goblin\n'))
                    if a1g == 1:
                        print('{}Você volta para a caverna correndo,\n'
                              'e acaba pisando em uma armadilha sem\n'
                              'ver, que acaba abrindo um alçapão a\n'
                              'baixo de você, te levando para um fim\n'
                              'tragico.\n'
                              '   VOCÊ MORREU!!!{}\n'
                              ''.format(cores['vermelho'], cores['limpa']))
            else:
                print('{}Por não ter lido o que\n'
                      'estava escrito no papel, você\n'
                      'adentra mais a caverna e\n'
                      'descuidosamente acaba pisando\n'
                      'em uma armadilha.\n'
                      '   VOCÊ MORREU!!{}\n'
                      ''.format(cores['vermelho'], cores['limpa']))

        if dado12b <= 7:
            print('{}Você tirou {}\n'
                  'O Goblin com sua marreta\n'
                  'te esmaga de dilacerando\n.'
                  '   VOCÊ MORREU!!!'.format(cores['vermelho'], dado12b))

if a1d == 2:
    print('\n{}Você acha aquele bau muito suspeito,\n'
          'e decide apenas voltar a superficie\n'
          'e andar pela floresta para ver se\n'
          'encontra alguma coisa que lhe ajude,\n'
          'já que a caverna não tinha mais nada.\n'
          ''.format(cores['amarelo'], cores['limpa']))
    zpgt = 1000

if zpgt == 1000:
    print('{}========================================================================================================\n'
          '===================================CAPITULO 2 - FLORESTA FECHADA========================================\n'
          '========================================================================================================{}\n'
          ''.format(cores['magenta'], cores['limpa']))

    time.sleep(2)

    ok2 = int(input('{}Você acaba de entrar no capitulo 2,\n'
                    'preste bastante atenção,\n'
                    '{}OU SUA MORTE SERA RAPIDA!{}\n'
                    'Capitulo incompleto'.format(cores['magenta'], cores['vermelho'], cores['limpa'])))
