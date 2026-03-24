def main():
    s = 0
    numerador = 1

    for denominador in range(1, 51):
        s += numerador / denominador
        numerador += 2

    print("S =", s)

main()