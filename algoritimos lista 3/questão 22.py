def main():
    n = int(input("Quantos bois serão cadastrados? "))

    id_magro = 0
    peso_magro = 0
    id_gordo = 0
    peso_gordo = 0

    for i in range(n):
        identificacao = int(input("Número de identificação: "))
        nome = input("Nome do boi: ")
        peso = float(input("Peso do boi (kg): "))

        if i == 0:
            id_magro = identificacao
            peso_magro = peso
            id_gordo = identificacao
            peso_gordo = peso
        else:
            if peso < peso_magro:
                id_magro = identificacao
                peso_magro = peso

            if peso > peso_gordo:
                id_gordo = identificacao
                peso_gordo = peso

    print("Boi mais magro:")
    print("Identificação:", id_magro)
    print("Peso:", peso_magro)

    print("Boi mais gordo:")
    print("Identificação:", id_gordo)
    print("Peso:", peso_gordo)

main()