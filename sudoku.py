import random

def imprimir_tabuleiro(tabuleiro):
    """
        Função que gera o tabuleiro para ser exibido no terminal
    """
    for i in range(len(tabuleiro)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(tabuleiro[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(tabuleiro[i][j])
            else:
                print(str(tabuleiro[i][j]) + " ", end="")

def gerar_sudoku():
    """
        Aqui o jogo é gerado aleatórimanete de acordo com alguns parâmetros.
        1 - É criado o tabuleiro
        2 - Ele resolve o tabuleiro preenchendo os espaços vazios com números diferentes
        3 - Altera o tabuleiro substituindo aleatoriamente os números de um tabuleiro resolvido por 0
    """
    tabuleiro = [[0 for _ in range(9)] for _ in range(9)]
    resolver_sudoku(tabuleiro)
    vazios = random.randint(50, 60)  # Quantidade de espaços vazios no tabuleiro Ex: Terá entre x e x espaços vazios
    while vazios > 0:
        linha = random.randint(0, 8)
        coluna = random.randint(0, 8)
        if tabuleiro[linha][coluna] != 0:
            tabuleiro[linha][coluna] = 0
            vazios -= 1
    return tabuleiro

def resolver_sudoku(tabuleiro):
    """
        Essa função tem como objetivo resolver o jogo.
        Ela faz uma varredura no tabuleiro verificando linha e coluna e adicionando os números.
    """
    vazio = encontrar_vazio(tabuleiro)
    if not vazio:
        return True
    else:
        linha, coluna = vazio

    for numero in range(1, 10):
        if numero_valido(tabuleiro, numero, (linha, coluna)):
            tabuleiro[linha][coluna] = numero

            if resolver_sudoku(tabuleiro):
                return True

            tabuleiro[linha][coluna] = 0

    return False

def numero_valido(tabuleiro, numero, posicao):
    """
        Essa é a função que verifica se a posição da linha e coluna não tem o número
        repetido, de acordo com a entrada do jogador.
    """

    # Verifica linha
    for i in range(len(tabuleiro[0])):
        if tabuleiro[posicao[0]][i] == numero and posicao[1] != i:
            return False

    # Verifica a coluna
    for i in range(len(tabuleiro)):
        if tabuleiro[i][posicao[1]] == numero and posicao[0] != i:
            return False

    """
    A variável bloco_x representa a coluna do bloco 3x3 em que a posição se encontra,
    e é calculada dividindo a coluna da posição por 3 (usando divisão inteira //).
    Da mesma forma funciona a variável bloco_y representa a linha do bloco 3x3 em que a posição se encontra, 
    e é calculada dividindo a linha da posição por 3 (usando divisão inteira //).
    """

    bloco_x = posicao[1] // 3
    bloco_y = posicao[0] // 3

    for i in range(bloco_y * 3, bloco_y * 3 + 3):
        for j in range(bloco_x * 3, bloco_x * 3 + 3):
            if tabuleiro[i][j] == numero and (i, j) != posicao:
                return False

    return True

def encontrar_vazio(tabuleiro):
    """
        Encontra espaços vazios no tabuleiro, ou seja, posições com número 0.
        Caso não encontre nenhuma, retorna que None, ou seja, não existem
        espaços com número zero (vazios) no tabuleiro
    """
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[0])):
            if tabuleiro[i][j] == 0:
                return (i, j)
    return None

def tabuleiro_completo(tabuleiro):
    """
         Função que verifica se não existem mais espaços com número zero.
         Essa função, declara se o jogador, venceu o jogo ou não.
    """
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[0])):
            if tabuleiro[i][j] == 0:
                return False
    return True


def jogar_sudoku():
    """
        Essa é a função principal do jogo.
        1 - Geramos o tabuleiro aleatóriamente
        2 - Depois, chamamos a função que vai imprimir o tabuleiro no terminal
        3 - No looping while, é onde o jogador poderá realizar as entradas de linha, coluna e valor a ser inserido.
        4 - Também é possível digitar "resolver" para terminar o jogo.
    """
    tabuleiro = gerar_sudoku()
    print("Bem-vindo ao jogo de Sudoku! Digite 'dica' a qualquer momento para obter uma dica.")
    imprimir_tabuleiro(tabuleiro)
    print("")

    while True:
        linha = int(input("Digite o número da linha (0-8): "))
        coluna = int(input("Digite o número da coluna (0-8): "))
        if linha < 0 or linha > 8 or coluna < 0 or coluna > 8:
            print("Entrada inválida. Digite os números da linha e coluna novamente.")
            continue

        if tabuleiro[linha][coluna] != 0:
            print("Esta posição já está preenchida. Digite outra posição.")
            continue

        valor = int(input("Digite o número para inserir (1-9): "))
        if valor < 1 or valor > 9:
            print("Número inválido. Digite um número entre 1 e 9.")
            continue

        if numero_valido(tabuleiro, valor, (linha, coluna)):
            tabuleiro[linha][coluna] = valor
            imprimir_tabuleiro(tabuleiro)
            print("")

            if tabuleiro_completo(tabuleiro):
                print("Parabéns! Você venceu o jogo!")
                break
        else:
            print("Movimento inválido. Tente novamente.")

        resolver = input("Digite 'resolver' para preencher todas as posições automaticamente: ")
        if resolver.lower() == "resolver":
            resolver_sudoku(tabuleiro)
            imprimir_tabuleiro(tabuleiro)
            print("")

# Iniciando o jogo
jogar_sudoku()
