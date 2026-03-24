def main():
    n = int(input("Quantos eleitores votarão? "))

    candidato1 = 0
    candidato2 = 0
    candidato3 = 0
    nulos = 0
    brancos = 0

    for i in range(n):
        voto = int(input("Digite o voto: "))

        if voto == 1:
            candidato1 += 1
        elif voto == 2:
            candidato2 += 1
        elif voto == 3:
            candidato3 += 1
        elif voto == 9:
            nulos += 1
        elif voto == 0:
            brancos += 1

    print("Votos no candidato 1:", candidato1)
    print("Votos no candidato 2:", candidato2)
    print("Votos no candidato 3:", candidato3)
    print("Votos nulos:", nulos)
    print("Votos em branco:", brancos)

    if candidato1 > candidato2 and candidato1 > candidato3:
        print("Vencedor: candidato 1")
    elif candidato2 > candidato1 and candidato2 > candidato3:
        print("Vencedor: candidato 2")
    elif candidato3 > candidato1 and candidato3 > candidato2:
        print("Vencedor: candidato 3")
    else:
        print("Houve empate")

main()