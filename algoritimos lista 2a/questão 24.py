a = float(input("Coeficiente A: "))
b = float(input("Coeficiente B: "))
c = float(input("Coeficiente C: "))

if a != 0:
    delta = b**2 - 4*a*c
    if delta >= 0:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        print(f"Raízes: {x1} e {x2}")
    else:
        print("Não existem raízes reais")
else:
    print("A deve ser diferente de 0")