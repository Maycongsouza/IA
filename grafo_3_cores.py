import pygame

# Configs da janela (resolução)
LARGURA = 900
ALTURA = 768

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)
VERDE = (50, 168, 82)

# Tamanho dos nodos
RADIO_NO = 30

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.nomes_nos = {}
        self.posicoes_nos = {}

    def definir_nome_no(self, no, nome):
        self.nomes_nos[no] = nome

    def definir_posicao_no(self, no, x, y):
        self.posicoes_nos[no] = (x, y)

    def eh_seguro(self, v, cor, c):
        for i in range(self.V):
            if self.grafo[v][i] == 1 and cor[i] == c:
                return False
        return True

    def ver_coloracao(self, m, cor, v):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.eh_seguro(v, cor, c):
                cor[v] = c
                if self.ver_coloracao(m, cor, v + 1):
                    return True
                cor[v] = 0

    def coloracao_grafo(self, m):
        cor = [0] * self.V
        if not self.ver_coloracao(m, cor, 0):
            print("Não é possível colorir o grafo com", m, "cores.")
            return False

        print("O grafo pode ser colorido com", m, "cores. As atribuições de cores são:")
        for v in range(self.V):
            print("Nó", self.nomes_nos[v], ": Cor", cor[v])

        pygame.init()
        screen = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Coloração de Grafos")

        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            screen.fill(PRETO)

            # Desenhar arestas de forma dinâmica
            for v in range(self.V):
                for u in range(self.V):
                    if self.grafo[v][u] == 1:
                        x1, y1 = self.posicoes_nos[v]
                        x2, y2 = self.posicoes_nos[u]
                        pygame.draw.line(screen, BRANCO, (x1, y1), (x2, y2), 2)

            # Desenhar nós coloridos com letras
            font = pygame.font.Font(None, 30)
            for v in range(self.V):
                x, y = self.posicoes_nos[v]
                if cor[v] == 1:
                    color = AZUL
                elif cor[v] == 2:
                    color = VERMELHO
                elif cor[v] == 3:
                    color = AMARELO
                elif cor[v] == 4:
                    color = VERDE
                else:
                    color = BRANCO
                pygame.draw.circle(screen, color, (x, y), RADIO_NO)
                text = font.render(self.nomes_nos[v], True, BRANCO)
                text_rect = text.get_rect(center=(x, y))
                screen.blit(text, text_rect)

            pygame.display.flip()
            clock.tick(60)



# g = Grafo(7)
g = Grafo(8)

g.definir_nome_no(0, 'A')
g.definir_nome_no(1, 'B')
g.definir_nome_no(2, 'C')
g.definir_nome_no(3, 'D')
g.definir_nome_no(4, 'E')
g.definir_nome_no(5, 'F')
g.definir_nome_no(6, 'G')
g.definir_nome_no(7, 'H')

g.definir_posicao_no(0, 100, 200)
g.definir_posicao_no(1, 200, 200)
g.definir_posicao_no(2, 600, 200)
g.definir_posicao_no(3, 700, 200)
g.definir_posicao_no(4, 400, 400)
g.definir_posicao_no(5, 200, 600)
g.definir_posicao_no(6, 600, 600)
g.definir_posicao_no(7, 700, 700)

# g.grafo = [[1, 1, 0, 0, 0, 0, 0],
#            [1, 1, 1, 0, 0, 0, 0],
#            [0, 1, 1, 1, 1, 0, 0],
#            [0, 0, 1, 1, 0, 0, 0],
#            [0, 1, 1, 0, 1, 1, 1],
#            [0, 0, 0, 0, 1, 1, 1],
#            [0, 0, 0, 0, 1, 1, 1]]

g.grafo = [[1, 1, 0, 0, 0, 0, 0, 0],
           [1, 1, 1, 0, 0, 0, 0, 0],
           [0, 1, 1, 1, 1, 0, 0, 0],
           [0, 0, 1, 1, 0, 0, 0, 0],
           [0, 1, 1, 0, 1, 1, 1, 0],
           [0, 0, 0, 0, 1, 1, 1, 0],
           [0, 0, 0, 1, 1, 1, 1, 0],
           [0, 0, 0, 0, 1, 1, 1, 0]
           ]

# g.coloracao_grafo(3)
g.coloracao_grafo(4)
