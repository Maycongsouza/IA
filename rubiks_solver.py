# Para executar o código, é preciso instalar a biblioteca pycuber
from pycuber import *
from pycuber.solver import CFOPSolver

# Formamos o cubo
cubo = Cube()
cubo_solve = cubo.copy()
# Para gerar posições aleatórias no cubo, chamamos a classe Formula
passos_aleatorios = Formula()

# Dentro da classe, chamamos a função random, que irá misturar o cubo
random = passos_aleatorios.random()
# Passamos as passos aleatórios para o cubo
cubo(random)

# Mostrando os passos aleatórios para a geração do cubo
print(random)

# Função para exibir o cubo com as cores
def exibe_cubo(cubo):
    # Fizemos um dict para visualizar cada face do cubo
    faces = {
        "U": cubo.get_face("U"),
        "D": cubo.get_face("D"),
        "F": cubo.get_face("F"),
        "B": cubo.get_face("B"),
        "L": cubo.get_face("L"),
        "R": cubo.get_face("R"),
    }

    # A ordem da visualização é ---> ULFRBD
    """
        U: Upper (superior)
        D: Down (inferior)
        F: Front (frontal)
        B: Back (traseira)
        R: Right (direita)
        L: Left (esquerda)
    """

    print("             {}".format(faces["U"][0]))
    print("             {}".format(faces["U"][1]))
    print("             {}".format(faces["U"][2]))

    print('')

    print("{} {} {} {}".format(
        faces["L"][0],
        faces["F"][0],
        faces["R"][0],
        faces["B"][0],
    ))
    print("{} {} {} {}".format(
        faces["L"][1],
        faces["F"][1],
        faces["R"][1],
        faces["B"][1],
    ))
    print("{} {} {} {}".format(
        faces["L"][2],
        faces["F"][2],
        faces["R"][2],
        faces["B"][2],
    ))

    print('')

    print("             {}".format(faces["D"][0]))
    print("             {}".format(faces["D"][1]))
    print("             {}".format(faces["D"][2]))

# Função que usamos para o cubo ser rotacionado,
# ela recebe como parâmetro a variável mover, que contém a entrada do usuário
def rodar_cubo(mover):
    # Se tiver ' na entrada, significa que foi movido no sentido anti-horário
    if "'" in mover:
        cubo(mover)
        print("Cubo movido no sentido anti-horário: ", mover.upper())
    # Se não, foi movido no sentido horário
    else:
        mover = mover.lower()
        cubo(mover)
        print("Cubo movido no sentido horário: ", mover.upper())

# Função que resolve o cubo através do método CFOP para Cubos Mágicos
def resolver_cubo():
    cubo_solve = cubo.copy()
    exibe_cubo(cubo_solve)
    resolver = CFOPSolver(cubo)
    solucao = resolver.solve(suppress_progress_messages=True)
    for i in solucao:
        cubo_solve(i)
        print(i)
        print(exibe_cubo(cubo_solve))
    print("Passo a passo da Solução:\n", solucao)
    print("\nO cubo foi resolvido!\n")

# Looping contínuo até o cubo ser resolvido
while True:
    # Entradas aceitas
    """
        * Um giro no sentido horário de 90 graus: R, U, F, D, B e L.
        * Um giro no sentido anti-horário de 90 graus: R', U', F', D', B' e L'.
        * Um giro de 180 graus: R2, U2, F2, D2, B2 e L2.
    """
    exibe_cubo(cubo)
    print("Dê um comando para mover (ou escreva 'solucao' para solucionar o cubo):")
    mover = input(">>> ")
    if mover == "solucao":
        resolver_cubo()
        break
    else:
        try:
            rodar_cubo(mover)
        except:
            print('Entrada inválida')
