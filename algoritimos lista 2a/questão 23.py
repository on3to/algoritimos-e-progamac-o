d1, m1, a1 = int(input("Dia 1: ")), int(input("Mês 1: ")), int(input("Ano 1: "))
d2, m2, a2 = int(input("Dia 2: ")), int(input("Mês 2: ")), int(input("Ano 2: "))

if a1 > a2:
    print("Data 1 é mais recente")
elif a2 > a1:
    print("Data 2 é mais recente")
elif m1 > m2:
    print("Data 1 é mais recente")
elif m2 > m1:
    print("Data 2 é mais recente")
elif d1 > d2:
    print("Data 1 é mais recente")
elif d2 > d1:
    print("Data 2 é mais recente")
else:
    print("As datas são iguais")