l1 = float(input("Lado 1: "))
l2 = float(input("Lado 2: "))
l3 = float(input("Lado 3: "))

if l1 > 0 and l2 > 0 and l3 > 0 and (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
    if l1 == l2 == l3:
        print("Triângulo Equilátero")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Não formam um triângulo")