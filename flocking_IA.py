import random
import math

# Definindo a classe do agente de acordo com as solicitações do exercício
class Agente:
    def __init__(self, linha, coluna, peso):
        self.linha = linha
        self.coluna = coluna
        self.peso = peso
# Cria uma lista de agentes com posições e pesos aleatórios para serem testados
agentes = [Agente(random.randint(0, 4), random.randint(0, 4), random.uniform(0.5, 2)) for i in range(5)]

# Cria uma matriz usando N para representar o tamanho do tabuleiro e preenche com asteriscos
tabuleiro = [["*" for j in range(5)] for i in range(5)]
for agente in agentes:
    tabuleiro[agente.linha][agente.coluna] = "A"
# Escolhe aleatoriamente um dos agentes da lista para ser o líder
lider = random.choice(agentes)

# Para cada agente, calcula a distância até o líder e move o agente em direção ou longe
# do líder, dependendo da distância e dos pesos dos agentes
for agente in agentes:
    if agente == lider:
        continue

    # Calcula a diferença entre as coordenadas x e y do agente e do líder
    x = lider.coluna - agente.coluna
    y = lider.linha - agente.linha

    # Calcula a distância entre o agente e o líder usando a equação da distância euclidiana
    distancia = math.sqrt(x**2 + y**2)

    # Calcula a distância mínima com base nos pesos dos agentes
    distancia_minima = lider.peso + agente.peso
    if distancia < distancia_minima:
        # Se a distância atual for menor que a distância mínima, move o agente para longe
        # do líder, reduzindo a distância entre eles para a distância mínima
        direcao_x = x / distancia
        direcao_y = y / distancia
        agente.linha -= int(round(direcao_y * distancia_minima))
        agente.coluna -= int(round(direcao_x * distancia_minima))
    else:
        # Se não, move o agente em direção ao líder
        direcao_x = x / distancia
        direcao_y = y / distancia
        agente.linha += int(round(direcao_y))
        agente.coluna += int(round(direcao_x))
    # Limita a posição somente aos limites da matriz
    agente.linha = max(min(agente.linha, 4), 0)
    agente.coluna = max(min(agente.coluna, 4), 0)

# Atualiza a matriz com as novas posições dos agentes
for i in range(5):
    for j in range(5):
        if tabuleiro[i][j] != "A":
            for agente in agentes:
                if agente.linha == i and agente.coluna == j:
                    tabuleiro[i][j] = "A"
                    break
# Marca a posição do líder na matriz com "AL"
tabuleiro[lider.linha][lider.coluna] = "AL"
# Imprime a matriz resultante na tela
for linha in tabuleiro:
    print(" ".join(linha))
