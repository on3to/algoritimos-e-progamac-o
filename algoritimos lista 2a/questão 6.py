a1 = float(input("Ângulo 1: "))
a2 = float(input("Ângulo 2: "))
a3 = float(input("Ângulo 3: "))

if a1 > 0 and a2 > 0 and a3 > 0 and (a1 + a2 + a3 == 180):
    if a1 < 90 and a2 < 90 and a3 < 90:
        print("Triângulo Acutângulo")
    elif a1 == 90 or a2 == 90 or a3 == 90:
        print("Triângulo Retângulo")
    else:
        print("Triângulo Obtusângulo")
else:
    print("Não formam um triângulo válido")