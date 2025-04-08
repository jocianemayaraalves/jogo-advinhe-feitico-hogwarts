# Palavra Secreta
feitico_novo = 'obliviate'

# Pergunta para dar início no game
pergunta = input('Olá, estudante de magia e bruxaria de Hogwarts, qual o seu nome? ')
print(f'Hmmm... {pergunta} não é? Que nome singular, eu prometo que vou lembrar de você!')

# Perguntas para alimentar o jogo
pergunta_2 = input('Posso te perguntar uma coisa, antes de começarmos? Por favor, responda com SIM ou NÃO! ')
pergunta_3 = input('Você gostaria de participar de um jogo para descobrir um feitiço novo? Diga SIM ou NÃO: ')

# Condição para verificar a resposta "não"
if pergunta_2.lower() == 'não' or pergunta_3.lower() == 'não':
    print('Que pena, então em uma próxima vez te ensino algo novo. Até mais!')
else:
    # Inicializa o estado da palavra, substituindo todas as letras por '*'
    palavra_oculta = '*' * len(feitico_novo)

    # Função para mostrar a palavra atual com as letras reveladas
    def mostrar_palavra(palavra_oculta):
        print(f'A palavra secreta é: {palavra_oculta}')

    # Condições interagindo com as perguntas
    if pergunta_2.lower() == 'sim' and pergunta_3.lower() == 'sim':
        print('Esse jogo vai ser como uma forca, você diz a letra e eu te mostro se tem ou se não tem ela na palavra.')

        # Loop para o jogo continuar até o usuário adivinhar a palavra inteira
        tentativas = 0
        while '*' in palavra_oculta:
            letra_usuario = input('Digite uma letra ou a palavra inteira: ').lower()

            # Verifica se o usuário digitou a palavra inteira
            if len(letra_usuario) == len(feitico_novo) and letra_usuario.isalpha():
                if letra_usuario == feitico_novo:
                    palavra_oculta = feitico_novo  # A palavra foi adivinhada corretamente
                    print(f'Parabéns! Você adivinhou a palavra: {palavra_oculta}')
                    break
                else:
                    print('Essa não é a palavra correta. Tente novamente!')
            else:
                # Atualiza a palavra oculta com as letras certas
                palavra_oculta = ''.join([letra_usuario if letra_usuario == feitico_novo[i] else palavra_oculta[i] for i in range(len(feitico_novo))])

                # Mostra o estado atual da palavra oculta
                mostrar_palavra(palavra_oculta)

            # Aumenta o contador de tentativas
            tentativas += 1

        if palavra_oculta == feitico_novo:
            print(f'BRILHANTE! Você adivinhou o feitiço em {tentativas} tentativa, meus parabéns... Guarde esse conhecimento com você, pode ser importante!')

        
