# -*- coding: utf-8 -*-
import os
import time
import random
from gameConfig import Game

# função para mostrar o valor que terá caso acerte a pergunta.
def ganhar():
    if total >= 0 and total < 5000:
        ponto = total + 1000
    elif total == 5000:
        ponto = total + 5000
    elif total > 5000 and total < 50000:
        ponto = total + 10000
    elif total == 50000:
        ponto = total + 50000
    elif total > 50000 and total < 500000:
        ponto = total + 100000
    else:
        ponto = total + 500000

    return str(ponto)

# função para mostrar o valor que terá caso erre a pergunta.
def perder():
    if total > 0 and total < 500000:
        ponto = round(total / 2)
    else:
        ponto = '0'
    
    return str(ponto)

start = Game()
# booleana para sair do jogo, caso a pessoa não queira mais jogar (código no final da estrutura while).
continuar = True

try:
# enquanto a condição for True, ele voltará ao começo do jogo.
    while continuar == True:

        # limpa o console.
        os.system('cls' if os.name == 'nt' else 'clear')

        print('╔' + '═'*117 + '╗')
        print('║' + '$ SEJA BEM-VINDO AO SHOW DO MILHÃO $'.center(110) + '║'.rjust(8))
        print('╚' + '═'*117 + '╝')

        print('\nRegras:\n• Serão 16 perguntas de múltipla escolha, sendo a última com o valor de 1 MILHÃO DE REAIS!\n• Você poderá pular perguntas (com o limite de 3 usos) e parar caso seja necessário.\n')
        input('\n>> Aperte ENTER para começar! <<')

        os.system('cls' if os.name == 'nt' else 'clear')

        # variável para a pontuação do jogo.
        total = 0
        # variável para a opção de pulo dentro do jogo.
        pular = 3 
        # lista para perguntas já usadas.
        passe = []
                
        # iteração feita no dicionário "perguntas", mostrado no início.
        for w, x in start.perguntas.items():
            # booleana para sair do looping na pergunta atual caso seja True.
            conf = False
            # booleana para sair do jogo caso seja True.
            sair = False
            # selecionando uma pergunta aleatória dentro do dicionário.
            random_menu = random.choice(list(start.perguntas.values()))

            # impede que perguntas repetidas sejam usadas.
            while random_menu['pergunta'] in passe:
                random_menu = random.choice(list(start.perguntas.values()))

            if random_menu['pergunta'] not in passe:
                passe.append(random_menu['pergunta'])
                
            # repete a pergunta atual até a condição sair de False.
            while conf == False:
                os.system('cls' if os.name == 'nt' else 'clear')
                # placar do topo.
                print(f'► Pontuação: R${total} | ERRAR: R$ {perder()}   PARAR: R${total}    ACERTAR: R${ganhar()}')
                if total == 500000:
                    print('\n(ÚLTIMA PERGUNTA)')
                print()
                
                # a pergunta aleatória.
                print(f'» {random_menu["pergunta"]}')
                print()
                # as opções de respostas para cada pergunta aleatória.
                for y, z in random_menu['respostas'].items():
                    print(f'[{y}]: {z}')
                # barra de opções.
                print(f'\n► Opções: PULAR - {pular}x (P) | PARAR (S)')
                print()
                # área de respostas.
                resp = input()
                # filtro de respostas.
                if resp.upper() != 'A' and resp.upper() != 'B' and resp.upper() != 'C' and resp.upper() != 'D' and  resp.upper() != 'P' and resp.upper() != 'S':
                    print('\nEscolha inválida, tente as opções citadas acima.')
                    time.sleep(1.5)
                else:
                    # confirmação da resposta.
                    op = input('\nEstá certo disso? (s/n) ')
                    if op.lower() == 's':
                        # caso acerte, ganha pontos de acordo com a pontuação atual.
                        if resp.upper() == random_menu["resposta_certa"]:
                            print('\nACERTOU!')
                            time.sleep(1.5)
                            if total >= 0 and total < 5000:
                                total += 1000
                            elif total == 5000:
                                total += 5000
                            elif total > 5000 and total < 50000:
                                total += 10000
                            elif total == 50000:
                                total += 50000
                            elif total > 50000 and total < 500000:
                                total += 100000
                            elif total == 500000:
                                total += 500000
                            else:
                                total += 1000000
                            conf = True
                        # caso pule, gasta 1 dos 3 pulos, quando gasta os 3, bloqueia o uso.
                        elif resp.upper() == 'P':
                            if pular == 0:
                                print('\nVocê não possui mais "PULAR".')
                                time.sleep(1.5)
                            else:
                                pular -= 1
                                conf = True
                        # caso pare, termina o jogo com a pontuação atual.
                        elif resp.upper() == 'S':
                            conf = True
                            sair = True
                        # caso erre, vai direto para a tela de fim com a metade do dinheiro ganho (caso esteja na pergunta de 1 milhão, perde tudo).
                        else:
                            print('\nERROU!')
                            time.sleep(1.5)
                            if total > 0 and total < 500000:
                                total = str(round(total / 2))
                            else:
                                total = 0
                            sair = True
                            conf = True
                    # caso não esteja certo da resposta, volta até às opções.
                    elif op.lower() == 'n':
                        conf = conf
                    # se não for nenhum dos dois, emite um alerta e volta às opções.
                    else:
                        print('\nEscolha inválida, voltando à pergunta.')
                        time.sleep(1.5)
                    # caso a pontuação atinja 1 milhão, acaba o jogo.
                    if total == 1000000:
                        sair = True
            # booleana para sair do jogo em caso de True.
            if sair == True:
                break

        opcao = False
        
        while opcao == False:

            os.system('cls' if os.name == 'nt' else 'clear')

            # tela final do jogo.
            print(f'XXX FIM DE JOGO! XXX \n\n► Pontuação total: R${str(total)}')
            if total == 1000000:
                print('\nPARABÉNS, MILIONÁRIO(A)!')
            rematch = input('\nJogar de novo? (s/n) ')

            # a primeira opção faz voltar ao jogo do começo, a segunda sai do jogo de vez e encerra o aplicativo com o input() abaixo.
            if rematch.lower() == 's':
                continuar = continuar
                opcao = True
            elif rematch.lower() == 'n':
                continuar = False
                opcao = True
            else:
                print('\nEscolha inválida, tente novamente.')
                time.sleep(1.5)
                opcao = opcao
except KeyboardInterrupt:
    print('Encerrando o jogo...')            

# encerra o aplicativo.
input("\nAperte ENTER para sair do programa.")