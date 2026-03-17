v1 = int(input("Valor 1: "))
v2 = int(input("Valor 2: "))
resto = v1 % v2

if resto == 1:
    print(v1 + v2 + resto)
elif resto == 2:
    p1 = "par" if v1 % 2 == 0 else "ímpar"
    p2 = "par" if v2 % 2 == 0 else "ímpar"
    print(f"V1 é {p1} e V2 é {p2}")
elif resto == 3:
    print((v1 + v2) * v1)
elif resto == 4:
    if v2 != 0:
        print((v1 + v2) / v2)
else:
    print(f"Quadrados: {v1**2} e {v2**2}")