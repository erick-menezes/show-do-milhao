# coding=UTF-8
import os
import time
import random

# área de perguntas.
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Qual é o coletivo de cães?',
        'respostas': {'A': 'Matilha', 'B': 'Rebanho', 'C': 'Alcateia', 'D': 'Manada'},
        'resposta_certa': 'A',
    },
    'Pergunta 2': {
        'pergunta': 'Qual desses NÃO é o nome de um planeta do sistema solar?',
        'respostas': {'A': 'Marte', 'B': 'Saturno', 'C': 'Vênus', 'D': 'Cripta'},
        'resposta_certa': 'D',
    },
    'Pergunta 3': {
        'pergunta': 'Ganhei 65 chocolates, dei 1 para a minha irmã, quantos chocolates eu fiquei?',
        'respostas': {'A': '65', 'B': '64', 'C': '63', 'D': '62'},
        'resposta_certa': 'B',
    },
    'Pergunta 4': {
        'pergunta': 'Qual pássaro é famoso por construir sua própria casa?',
        'respostas': {'A': 'Beija Flor', 'B': 'João de Barro', 'C': 'Pardal', 'D': 'Coruja'},
        'resposta_certa': 'B',
    },
    'Pergunta 5': {
        'pergunta': 'Qual o nome do esporte em que dois atletas se enfretam no ringue e devem acertar socos no adversário da cintura para cima?',
        'respostas': {'A': 'Judô', 'B': 'Muay Thai', 'C': 'Sumô', 'D': 'Boxe'},
        'resposta_certa': 'D',
    },
    'Pergunta 6': {
        'pergunta': 'A sinusite ataca:',
        'respostas': {'A': 'Os olhos', 'B': 'O nariz', 'C': 'O ouvido', 'D': 'O pulmão'},
        'resposta_certa': 'B',
    },
    'Pergunta 7': {
        'pergunta': 'Qual personagem bíblico conhecido por atravessar o mar vermelho?',
        'respostas': {'A': 'Abraão', 'B': 'Moisés', 'C': 'Josué', 'D': 'Elias'},
        'resposta_certa': 'B',
    },
    'Pergunta 8': {
        'pergunta': 'Qual alimento é popularmente conhecido por ser consumido durante filmes?',
        'respostas': {'A': 'Pipoca', 'B': 'Chocolate', 'C': 'Sorvete', 'D': 'Cebola'},
        'resposta_certa': 'A',
    },
    'Pergunta 9': {
        'pergunta': 'Estamos no ano de 2016. Daqui 4 anos será...?',
        'respostas': {'A': '2020', 'B': '2021', 'C': '2025', 'D': '2019'},
        'resposta_certa': 'A',
    },
    'Pergunta 10': {
        'pergunta': 'Quem nasce na Itália é:',
        'respostas': {'A': 'Italiano', 'B': 'Italico ', 'C': 'Italianês', 'D': 'Vaticanense'},
        'resposta_certa': 'A',
    },
    'Pergunta 11': {
        'pergunta': 'Quem dava aula para o Chaves?',
        'respostas': {'A': 'Kiko', 'B': 'Dona Florinda', 'C': 'Seu Madruga', 'D': 'Professor Girafales'},
        'resposta_certa': 'D',
    },
    'Pergunta 12': {
        'pergunta': 'Qual o alimento do gafanhoto?',
        'respostas': {'A': 'Carne', 'B': 'Folhas de plantas', 'C': 'Feijão', 'D': 'Outros animais'},
        'resposta_certa': 'B',
    },
    'Pergunta 13': {
        'pergunta': 'Fiz 500 brigadeiros em 5 dias. Quantos brigadeiros eu fiz por dia?',
        'respostas': {'A': '10', 'B': '15', 'C': '100', 'D': '200'},
        'resposta_certa': 'C',
    },
    'Pergunta 14': {
        'pergunta': 'Qual desses não é um exemplo de energia renovável?',
        'respostas': {'A': 'Fósseis', 'B': 'Ventos', 'C': 'Rios', 'D': 'Solar'},
        'resposta_certa': 'A',
    },
    'Pergunta 15': {
        'pergunta': 'Qual o nome do casal principal da saga Crepúsculo?',
        'respostas': {'A': 'Alice e Emmet', 'B': 'Jasper e Rosalie', 'C': 'Edward e Bella', 'D': 'Victoria e James'},
        'resposta_certa': 'C',
    },
    'Pergunta 16': {
        'pergunta': 'Como é chamada a cidade do Batman?',
        'respostas': {'A': 'Gotham City', 'B': 'Metrópolis', 'C': 'Atlantis', 'D': 'PleasantVille'},
        'resposta_certa': 'A',
    },
    'Pergunta 17': {
        'pergunta': 'O principal sintoma da insônia é:',
        'respostas': {'A': 'Excesso de sono', 'B': 'Falta de apetite', 'C': 'Falta de sono', 'D': 'Frio excessivo'},
        'resposta_certa': 'C',
    },
    'Pergunta 18': {
        'pergunta': 'Qual desses meios de comunicação a distância é o mais antigo?',
        'respostas': {'A': 'Telefone', 'B': 'Fax', 'C': 'E-mail', 'D': 'Carta'},
        'resposta_certa': 'D',
    },
    'Pergunta 19': {
        'pergunta': 'Complete a música: Marcha soldado, cabeça de...',
        'respostas': {'A': 'Papel', 'B': 'Pastel', 'C': 'Papelão', 'D': 'Quartel'},
        'resposta_certa': 'A',
    },
    'Pergunta 20': {
        'pergunta': 'Qual é o símbolo de alumínio?',
        'respostas': {'A': 'AL', 'B': 'A', 'C': 'AM', 'D': 'AO'},
        'resposta_certa': 'A',
    },
    'Pergunta 21': {
        'pergunta': 'Como é chamado o músico que toca trompete?',
        'respostas': {'A': 'Trompetista', 'B': 'Trompeteiro', 'C': 'Trompeador', 'D': 'Tropeiro'},
        'resposta_certa': 'A',
    },
    'Pergunta 22': {
        'pergunta': 'O cipó é uma designação comum a qual tipo de planta?',
        'respostas': {'A': 'Gramínea', 'B': 'Rasteira', 'C': 'Aquática', 'D': 'Trepadeira'},
        'resposta_certa': 'D',
    },
    'Pergunta 23': {
        'pergunta': 'Didi, Dedé, Mussum e Zacarias eram os:',
        'respostas': {'A': 'Doidinhos', 'B': 'Caras de pau', 'C': 'Trapalhões', 'D': 'Atrapalhados'},
        'resposta_certa': 'C',
    },
    'Pergunta 24': {
        'pergunta': 'Como diz o ditado, mas vale estar só do que...',
        'respostas': {'A': 'Junto', 'B': 'Mal acompanhado', 'C': 'Mal valorizado', 'D': 'Namorando'},
        'resposta_certa': 'B',
    },
    'Pergunta 25': {
        'pergunta': 'Em qual palavra a letra "H" está empregada de maneira errada?',
        'respostas': {'A': 'Hóspede', 'B': 'História', 'C': 'Hescola', 'D': 'Habitação'},
        'resposta_certa': 'C',
    },
    'Pergunta 26': {
        'pergunta': 'A respiração pulmonar é realizada:',
        'respostas': {'A': 'Pela pele', 'B': 'Pelos pulmões', 'C': 'Pelas brânquias', 'D': 'Pela traquéia'},
        'resposta_certa': 'B',
    },
    'Pergunta 27': {
        'pergunta': 'Complete a música do Cazuza: "Brasil! Mostra a tua cara, quero ver quem ____ pra gente ficar assim"',
        'respostas': {'A': 'Paga', 'B': 'Rouba', 'C': 'Chega', 'D': 'Pega'},
        'resposta_certa': 'A',
    },
    'Pergunta 28': {
        'pergunta': 'Quem pintou a obra "Auto Retrato com a orelha cortada"?',
        'respostas': {'A': 'Salvador Dalí', 'B': 'Vincent Van Gogh', 'C': 'Paul Cézzane', 'D': 'Claude Monet'},
        'resposta_certa': 'B',
    },
    'Pergunta 29': {
        'pergunta': 'Qual é o grau mais leve de queimaduras na pele?',
        'respostas': {'A': '1°', 'B': '4°', 'C': '3°', 'D': '2°'},
        'resposta_certa': 'A',
    },
    'Pergunta 30': {
        'pergunta': 'Um carteiro tinha 300 cartas. Na parte da manhã ele entregou 150. Quantas cartas sobraram?',
        'respostas': {'A': '100', 'B': '110', 'C': '150', 'D': '111'},
        'resposta_certa': 'C',
    },
    'Pergunta 31': {
        'pergunta': 'Qual destas palavras NÃO é sinônimo de "sossegado"?',
        'respostas': {'A': 'Zen', 'B': 'Quieto', 'C': 'Silencioso', 'D': 'Cidadão'},
        'resposta_certa': 'D',
    },
    'Pergunta 32': {
        'pergunta': 'Qual é o fruto do jiloeiro?',
        'respostas': {'A': 'Jiló', 'B': 'Quiabo', 'C': 'Beterraba', 'D': 'Rabanete'},
        'resposta_certa': 'A',
    },
    'Pergunta 33': {
        'pergunta': 'O que, normalmente, o Professor Girafales entrega para Dona Florinda?',
        'respostas': {'A': 'Flores', 'B': 'Bombom', 'C': 'Café', 'D': 'Vinho'},
        'resposta_certa': 'A',
    },
    'Pergunta 34': {
        'pergunta': 'Qual destas palavras não é sinônimo de "tratar"?',
        'respostas': {'A': 'Cuidar', 'B': 'Proteger', 'C': 'Zelar', 'D': 'Largar'},
        'resposta_certa': 'D',
    },
    'Pergunta 35': {
        'pergunta': 'Qual inseto transmite a doença de chagas?',
        'respostas': {'A': 'Abelha', 'B': 'Barasta', 'C': 'Barbeiro', 'D': 'Pulga'},
        'resposta_certa': 'C',
    },
    'Pergunta 36': {
        'pergunta': 'Como é chamado o benefício concedido mensalmente ao trabalhador depois de encerrar a vida profissional?',
        'respostas': {'A': 'Aposentadoria', 'B': 'Empréstimo', 'C': 'Cachê', 'D': 'Comissão'},
        'resposta_certa': 'A',
    },
    'Pergunta 37': {
        'pergunta': 'Qual é a profissão de Woody Allen?',
        'respostas': {'A': 'Cineasta', 'B': 'Advogado', 'C': 'Artista Plástico', 'D': 'Estilista'},
        'resposta_certa': 'A',
    },
    'Pergunta 38': {
        'pergunta': 'Em que dança os dançarinos utilizam um pequeno guarda-chuva colorido?',
        'respostas': {'A': 'Samba', 'B': 'Quadrilha Junina', 'C': 'Frevo', 'D': 'Catira'},
        'resposta_certa': 'C',
    },
    'Pergunta 39': {
        'pergunta': 'No filme Toy Story, quem é o melhor amigo do xerife Woody?',
        'respostas': {'A': 'Buzz Lightyear', 'B': 'Senhor cabeça de batata', 'C': 'Slink', 'D': 'Barbie'},
        'resposta_certa': 'A',
    },
    'Pergunta 40': {
        'pergunta': 'Como é chamado o processo de queima?',
        'respostas': {'A': 'Combustão', 'B': 'Invasão', 'C': 'Ilusão', 'D': 'Apagão'},
        'resposta_certa': 'A',
    },
    'Pergunta 41': {
        'pergunta': 'Qual o metal mais valioso?',
        'respostas': {'A': 'Bronze', 'B': 'Ferro', 'C': 'Chumbo', 'D': 'Ouro'},
        'resposta_certa': 'D',
    },
    'Pergunta 42': {
        'pergunta': 'O que é a anemia?',
        'respostas': {'A': 'Uma planta', 'B': 'Uma bebida', 'C': 'Uma enfermidade', 'D': 'Uma medida'},
        'resposta_certa': 'C',
    },
    'Pergunta 43': {
        'pergunta': 'Que tipo de instrumento é o trompete?',
        'respostas': {'A': 'Engraçado', 'B': 'Percussão', 'C': 'Corda', 'D': 'Sopro'},
        'resposta_certa': 'D',
    },
    'Pergunta 44': {
        'pergunta': 'Qual planta era usada pelos egípcios para escrever na antiguidade?',
        'respostas': {'A': 'Papiro', 'B': 'Eucalipto', 'C': 'Oliveira', 'D': 'Milho'},
        'resposta_certa': 'A',
    },
    'Pergunta 45': {
        'pergunta': 'Qual o símbolo do Tera?',
        'respostas': {'A': 'A', 'B': 'G', 'C': 'T', 'D': 'B'},
        'resposta_certa': 'C',
    },
    'Pergunta 46': {
        'pergunta': 'Considere que todo mês tem 31 dias, quantos dias há em 9 meses?',
        'respostas': {'A': '278', 'B': '279', 'C': '287', 'D': '281'},
        'resposta_certa': 'B',
    },
    'Pergunta 47': {
        'pergunta': 'Qual dessas cores não compõe um arco-íris?',
        'respostas': {'A': 'Preto', 'B': 'Vermelho', 'C': 'Laranja', 'D': 'Anil'},
        'resposta_certa': 'A',
    },
    'Pergunta 47': {
        'pergunta': 'Qual é a parte que tem a função de fixar a planta?',
        'respostas': {'A': 'Flores', 'B': 'Folhas', 'C': 'Caule', 'D': 'Raiz'},
        'resposta_certa': 'D',
    },
    'Pergunta 48': {
        'pergunta': 'Como diz o ditado popular, não dê um passo maior que as?',
        'respostas': {'A': 'Pernas', 'B': 'Braços', 'C': 'Cabeça', 'D': 'Cérebro'},
        'resposta_certa': 'A',
    }
}
# fim das perguntas.

# booleana para sair do jogo, caso a pessoa não queira mais jogar (código no final da estrutura while).
continuar = True

# enquanto a condição for True, ele voltará ao começo do jogo.
while continuar == True:

    # limpa o console.
    os.system('cls' if os.name == 'nt' else 'clear')

    print('╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗')
    print('║                                     $ SEJA BEM-VINDO AO SHOW DO MILHÃO $                                            ║')
    print('╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝')

    print('\nRegras:\n• Serão 16 perguntas de múltipla escolha, sendo a última com o valor de 1 MILHÃO DE REAIS!\n• Você poderá pular perguntas (com o limite de 3 usos) e parar caso seja necessário.\n')
    input('\n>> Aperte ENTER para começar! <<')

    os.system('cls' if os.name == 'nt' else 'clear')

    # variável para a pontuação do jogo.
    total = 0
    # variável para a opção de pulo dentro do jogo.
    pular = 3 
    # lista para perguntas já usadas.
    passe = []

    # função para mostrar o valor que terá caso acerte a pergunta.
    def ganhar():
        if total >= 0 and total < 5000:
            ponto = str(total + 1000)
        elif total == 5000:
            ponto = str(total + 5000)
        elif total > 5000 and total < 50000:
            ponto = str(total + 10000)
        elif total == 50000:
            ponto = str(total + 50000)
        elif total > 50000 and total < 500000:
            ponto = str(total + 100000)
        else:
            ponto = str(total + 500000)

        return ponto

    # função para mostrar o valor que terá caso erre a pergunta.
    def perder():
        if total > 0 and total < 500000:
            ponto = str(round(total / 2))
        else:
            ponto = '0'
        
        return ponto
            
    # iteração feita no dicionário "perguntas", mostrado no início.
    for w, x in perguntas.items():
        # booleana para sair do looping na pergunta atual caso seja True.
        conf = False
        # booleana para sair do jogo caso seja True.
        sair = False
        # selecionando uma pergunta aleatória dentro do dicionário.
        random_menu = random.choice(list(perguntas.values()))

        # impede que perguntas repetidas sejam usadas.
        while random_menu['pergunta'] in passe:
            random_menu = random.choice(list(perguntas.values()))

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
            

# encerra o aplicativo.
input("\nAperte ENTER para sair do programa.")