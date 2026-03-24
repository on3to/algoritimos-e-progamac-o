def main():
    n = int(input("Digite N: "))

    maior_quadrado = 0

    for i in range(1, n + 1):
        if i * i <= n:
            maior_quadrado = i * i
        else:
            break

    print("Maior quadrado menor ou igual a N:", maior_quadrado)

main()