num = int(input("Número de 4 dígitos: "))

if 1000 <= num <= 9999:
    d12 = num // 100
    d34 = num % 100
    if num**0.5 == (d12 + d34):
        print("É um quadrado perfeito especial")
    else:
        print("Não é o caso")