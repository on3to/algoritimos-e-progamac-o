lados = []
lados.append(float(input("Lado 1: ")))
lados.append(float(input("Lado 2: ")))
lados.append(float(input("Lado 3: ")))

lados.sort(reverse=True)

print(f"Hipotenusa: {lados[0]}")
print(f"Catetos: {lados[1]} e {lados[2]}")