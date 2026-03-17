val1 = float(input("Valor 1: "))
val2 = float(input("Valor 2: "))
op = int(input("Operação (1-Soma, 2-Sub, 3-Mult, 4-Div): "))

if op == 1:
    print(val1 + val2)
elif op == 2:
    print(val1 - val2)
elif op == 3:
    print(val1 * val2)
elif op == 4:
    print(val1 / val2 if val2 != 0 else "Erro: Divisão por zero")