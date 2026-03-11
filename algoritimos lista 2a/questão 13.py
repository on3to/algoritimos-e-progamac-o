numeros = []
for i in range(5):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))

print(f"Maior: {max(numeros)}")
print(f"Menor: {min(numeros)}")