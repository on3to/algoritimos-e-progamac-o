def main():
    n = int(input("Quantos habitantes serão informados? "))

    soma_salario = 0
    soma_filhos = 0
    ate_1000 = 0

    for i in range(n):
        salario = float(input("Salário: "))
        filhos = int(input("Número de filhos: "))

        soma_salario += salario
        soma_filhos += filhos

        if salario <= 1000:
            ate_1000 += 1

    media_salario = soma_salario / n
    media_filhos = soma_filhos / n
    percentual = (ate_1000 / n) * 100

    print("Média de salário:", media_salario)
    print("Média de filhos:", media_filhos)
    print("Percentual com salário até R$ 1000,00:", percentual, "%")

main()