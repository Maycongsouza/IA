# INSTALAR AS LIBS numpy, pathfinding, Grid e AStarFinder
# pip ou pip3 install <nome_da_lib>

import random
import numpy as np
from pathfinding.core.grid import , 
from pathfinding.finder.a_star import AStarFinder

# Dimensões do tabuleiro
largura = 10
altura = 10

# Posição inicial do NPC 1
npc1_pos = [0, 0]

# Posição aleatória do NPC 2
npc2_pos = [random.randint(0, largura - 1), random.randint(0, altura - 1)]

# Posição aleatória do Jogador
J1 = [random.randint(0, largura - 1), random.randint(0, altura - 1)]

# Lista de obstáculos que são gerados pelo cenário aleatoriamente
obstaculos = [[random.randint(0, largura - 1), random.randint(0, altura - 1)],
              [random.randint(0, largura - 1), random.randint(0, altura - 1)],
              [random.randint(0, largura - 1), random.randint(0, altura - 1)]]

# Velocidade dos NPCs
npc_vel = 1
npc2_vel = 2

# Matriz de custos para contornar obstáculos
custo = np.ones((altura, largura))
for obst in obstaculos:
    custo[obst[1], obst[0]] = 99999

# Função que move o personagem jogável pelo cenário
def can_move_to(pos, prox_pos):
    if prox_pos in obstaculos:
        return False
    x1, y1 = pos
    x2, y2 = prox_pos
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if dx > 1 or dy > 1:
        return False
    return True

# Função que move o personagem jogável pelo cenário, verificando se é possível ir para a próxima posição
def find_path(start, end):
    grid = Grid(matrix=custo)
    start_node = grid.node(start[0], start[1])
    end_node = grid.node(end[0], end[1])
    finder = AStarFinder()
    path, _ = finder.find_path(start_node, end_node, grid)
    return path


# Função que move os NPC's
def move_npc(npc_pos, J1):
    path = find_path(npc_pos, J1)
    if len(path) > 1:
        next_step = path[1]
        npc_pos[0] = next_step[0]
        npc_pos[1] = next_step[1]

# Loop master
while True:
    # Imprime o tabuleiro
    for y in range(altura):
        for x in range(largura):
            if [x, y] == npc1_pos:
                print("N1", end="")
            elif [x, y] == npc2_pos:
                print("N2", end="")
            elif [x, y] == J1:
                print("J1", end="")
            elif [x, y] in obstaculos:
                print("#", end="")
            else:
                print(".", end="")
        print()

    # Calcula a distância entre o NPC e o Jogador
    distance = ((npc1_pos[0] - J1[0]) ** 2 + (npc1_pos[1] - J1[1]) ** 2) ** 0.5
    print(f"Distância entre NPC 1 e Jogador: {distance:.2f}")

    # Calcula a distância entre o NPC 2 e o Jogador
    distance = ((npc2_pos[0] - J1[0]) ** 2 + (npc2_pos[1] - J1[1]) ** 2) ** 0.5
    print(f"Distância entre NPC 2 e Jogador: {distance:.2f}")

    # Movimentações do J1
    prox_pos = J1.copy()
    movimentacao = input("Digite sua jogada (WASD): ")

    if movimentacao == "w":
        prox_pos[1] -= 1
    elif movimentacao == "s":
        prox_pos[1] += 1
    elif movimentacao == "a":
        prox_pos[0] -= 1
    elif movimentacao == "d":
        prox_pos[0] += 1

    # Verifica se o jogador pode se mover para a próxima posição
    if not can_move_to(J1, prox_pos):
        print("Movimento inválido!")
        continue

    J1 = prox_pos

    move_npc(npc1_pos, J1)

    move_npc(npc2_pos, J1)

    # Verifica se o NPC alcançou o Jogador
    if npc1_pos == J1 or npc2_pos == J1:
        print("O NPC alcançou o Jogador!")
        print("Fim de jogo!")
        break