from q3_calculo import verificar

def main():

    n1 = float(input("qual o primeiro numero:"))
    n2 = float(input("qual o segundo numero:"))
    n3 = float(input("qual o terceiro numero:"))

    resultado = verificar(n1, n2, n3)
    print(resultado)

main()