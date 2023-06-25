import random

# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
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

# Função para gerar um jogo de Sudoku aleatório
def gerar_sudoku():
    tabuleiro = [[0 for _ in range(9)] for _ in range(9)]
    resolver_sudoku(tabuleiro)
    vazios = random.randint(40, 60)  # Quantidade de espaços vazios no tabuleiro
    while vazios > 0:
        linha = random.randint(0, 8)
        coluna = random.randint(0, 8)
        if tabuleiro[linha][coluna] != 0:
            tabuleiro[linha][coluna] = 0
            vazios -= 1
    return tabuleiro

# Função para resolver o Sudoku
def resolver_sudoku(tabuleiro):
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

# Função auxiliar para verificar se um número é válido em uma determinada posição
def numero_valido(tabuleiro, numero, posicao):
    # Verifica a linha
    for i in range(len(tabuleiro[0])):
        if tabuleiro[posicao[0]][i] == numero and posicao[1] != i:
            return False

    # Verifica a coluna
    for i in range(len(tabuleiro)):
        if tabuleiro[i][posicao[1]] == numero and posicao[0] != i:
            return False

    # Verifica o bloco 3x3
    bloco_x = posicao[1] // 3
    bloco_y = posicao[0] // 3

    for i in range(bloco_y * 3, bloco_y * 3 + 3):
        for j in range(bloco_x * 3, bloco_x * 3 + 3):
            if tabuleiro[i][j] == numero and (i, j) != posicao:
                return False

    return True

# Função auxiliar para encontrar uma posição vazia no tabuleiro
def encontrar_vazio(tabuleiro):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[0])):
            if tabuleiro[i][j] == 0:
                return (i, j)
    return None

# Função para verificar se o jogador venceu o jogo
def tabuleiro_completo(tabuleiro):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[0])):
            if tabuleiro[i][j] == 0:
                return False
    return True

# Função principal do jogo de Sudoku
def jogar_sudoku():
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

        dica = input("Digite 'dica' para obter uma dica ou pressione Enter para continuar: ")
        if dica.lower() == "dica":
            resolver_sudoku(tabuleiro)
            imprimir_tabuleiro(tabuleiro)
            print("")

# Iniciar o jogo
jogar_sudoku()
