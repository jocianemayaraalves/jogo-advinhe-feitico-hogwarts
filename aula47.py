import random

# Lista de feitiços
feiticos = ['obliviate', 'expelliarmus', 'lumos', 'nox', 'accio', 'wingardium', 'expecto', 'reducto', 'stupefy', 'alohomora']

def iniciar_jogo():
    # Escolhe um feitiço aleatório
    feitico_secreto = random.choice(feiticos)
    palavra_oculta = '*' * len(feitico_secreto)
    tentativas = 0

    print('Olá, estudante de magia e bruxaria de Hogwarts!')
    nome = input('Diga-me... qual é o seu nome? ')
    print(f'Hmmm... {nome}, que nome encantador. Anotado na minha memória mágica!')

    # Interação inicial
    resposta1 = input('Posso te perguntar uma coisa antes de começarmos? (SIM ou NÃO): ').strip().lower()
    resposta2 = input('Você gostaria de jogar um desafio mágico para descobrir um feitiço secreto? (SIM ou NÃO): ').strip().lower()

    if resposta1 != 'sim' or resposta2 != 'sim':
        print('Ah... uma pena! Quando quiser brincar com a magia novamente, estarei por aqui.')
        return

    print('\nMuito bem! Este é um jogo como a forca.')
    print('Você deve adivinhar um feitiço letra por letra, ou arriscar a palavra inteira.')
    print('Cuidado... errar muitas vezes pode atrair os trasgos do castelo! 🧌')
    print('-' * 50)

    # Loop principal do jogo
    while '*' in palavra_oculta:
        mostrar_palavra(palavra_oculta)
        tentativa = input('Digite uma letra ou arrisque a palavra completa: ').lower()

        if tentativa == feitico_secreto:
            palavra_oculta = feitico_secreto
            print(f'\nINCRÍVEL, {nome.upper()}! Você decifrou o feitiço: {feitico_secreto}')
            break
        elif len(tentativa) == 1 and tentativa.isalpha():
            nova_palavra = ''
            acerto = False
            for i in range(len(feitico_secreto)):
                if tentativa == feitico_secreto[i]:
                    nova_palavra += tentativa
                    acerto = True
                else:
                    nova_palavra += palavra_oculta[i]
            palavra_oculta = nova_palavra

            if acerto:
                print('Boa! Essa letra está no feitiço! ✨')
            else:
                print('Hmm... essa letra não está no feitiço. Tente outra!')
        else:
            print('Ops! Tente uma única letra ou o feitiço completo.')

        tentativas += 1

    print(f'\nVocê descobriu o feitiço em {tentativas} tentativa(s)! Parabéns, jovem bruxo(a)! 🧙‍♀️🧙‍♂️')

def mostrar_palavra(palavra):
    print(f'\nFeitiço secreto: {palavra}')

# Inicia o jogo
iniciar_jogo()
