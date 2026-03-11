num = float(input("Digite um número: "))
inteiro = int(num)
fracao = num - inteiro

if fracao >= 0.5:
    print(inteiro + 1)
else:
    print(inteiro)