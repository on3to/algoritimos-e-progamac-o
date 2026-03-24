def main():
    limite_inferior = int(input("Digite o limite inferior: "))
    limite_superior = int(input("Digite o limite superior: "))

    for num in range(limite_inferior, limite_superior + 1):
        if num > 1:
            primo = True

            for i in range(2, num):
                if num % i == 0:
                    primo = False
                    break

            if primo:
                print(num)

main()