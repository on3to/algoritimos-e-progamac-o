def main():
    n = int(input("Digite N: "))
    s = 0

    for i in range(1, n + 1):
        termo = i / (n - i + 1)

        if i % 2 == 0:
            s -= termo
        else:
            s += termo

    print("S =", s)

main()