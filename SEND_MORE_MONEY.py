def resolucao():
    for S in range(0, 10):
        for E in range(0, 10):
            for N in range(0, 10):
                for D in range(0, 10):
                    for M in range(1, 10):  # M não pode ser zero
                        for O in range(0, 10):
                            for R in range(0, 10):
                                for Y in range(0, 10):
                                    send = S * 1000 + E * 100 + N * 10 + D
                                    more = M * 1000 + O * 100 + R * 10 + E
                                    money = M * 10000 + O * 1000 + N * 100 + E * 10 + Y
                                    if send + more == money:
                                        return (send, more, money)

resultado = resolucao()
if resultado:
    send, more, money = resultado
    print("SEND =", send)
    print("MORE =", more)
    print("MONEY =", money)
else:
    print("Nenhuma solução encontrada.")
