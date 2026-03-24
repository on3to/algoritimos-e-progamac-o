def main():
    n = int(input("Quantos números serão digitados? "))
    soma = 0

    for i in range(n):
        numero = float(input("Digite um número: "))
        soma += numero

    media = soma / n

    print("Soma:", soma)
    print("Média:", media)

main()