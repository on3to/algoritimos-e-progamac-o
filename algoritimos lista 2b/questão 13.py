respostas = []
respostas.append(input("Telefonou para a vítima? (S/N): ").upper())
respostas.append(input("Esteve no local do crime? (S/N): ").upper())
respostas.append(input("Mora perto da vítima? (S/N): ").upper())
respostas.append(input("Devia para a vítima? (S/N): ").upper())
respostas.append(input("Já trabalhou com a vítima? (S/N): ").upper())

sim = respostas.count("S")

if sim == 2:
    print("Suspeita")
elif 3 <= sim <= 4:
    print("Cúmplice")
elif sim == 5:
    print("Assassino")
else:
    print("Inocente")