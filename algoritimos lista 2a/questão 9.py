num = int(input("Digite um número entre 0 e 100: "))

if 0 <= num <= 100:
    if num < 2:
        print("Não é primo")
    else:
        primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                primo = False
                break
        if primo:
            print("É primo")
        else:
            print("Não é primo")
else:
    print("Fora do intervalo permitido")