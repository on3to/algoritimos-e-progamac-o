num = int(input("Número entre 1000 e 9999: "))

if 1000 <= num <= 9999:
    parte1 = num // 100
    parte2 = num % 100
    soma = parte1 + parte2
    if soma**2 == num:
        print("Obedece à característica")
    else:
        print("Não obedece")