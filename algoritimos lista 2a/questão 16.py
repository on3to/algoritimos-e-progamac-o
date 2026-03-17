n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = (n1 + n2) / 2

if media >= 7.0:
    print("Aprovado")
else:
    exame = float(input("Nota do exame: "))
    media_final = (media + exame) / 2
    if media_final >= 5.0:
        print("Aprovado")
    else:
        print("Reprovado")