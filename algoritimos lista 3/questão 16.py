def main():
    n = int(input("Digite N: "))

    a = 0
    b = 1

    for i in range(n):
        print(a)
        proximo = a + b
        a = b
        b = proximo

main()