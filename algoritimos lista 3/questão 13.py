def main():
    n = int(input("Quantos números serão digitados? "))

    maior = float(input("Digite um número: "))

    for i in range(1, n):
        numero = float(input("Digite um número: "))
        if numero > maior:
            maior = numero

    print("Maior número:", maior)

main()