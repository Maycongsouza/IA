# Para executar o código, é preciso instalar a biblioteca pycuber
from pycuber import *
from pycuber.solver import CFOPSolver

# Formamos o cubo
cubo = Cube()

# Para gerar posições aleatórias no cubo, chamamos a classe Formula
cubo_aleatorio = Formula()

# Dentro da classe, chamamos a função random, que irá misturar o cubo
random_alg = cubo_aleatorio.random()
cubo(cubo_aleatorio)

# Função para exibir o cubo com as cores
def exibe_cubo():
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
    resolver = CFOPSolver(cubo)
    solucao = resolver.solve(suppress_progress_messages=True)
    print("Passo a passo da Solução:\n", solucao)
    print("\nCubo resolvido:\n")
    print(exibe_cubo())

# Looping contínuo até o cubo ser resolvido
while True:
    exibe_cubo()
    print("Dê um comando para mover (ou escreva 'solucao' para solucionar o cubo):")
    mover = input(">>> ")
    if mover == "solucao":
        resolver_cubo()
        break
    else:
        rodar_cubo(mover)
