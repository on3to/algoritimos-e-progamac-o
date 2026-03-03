from q5_calculo import cal_preço
def main():

    p1 = float(input("qual o valor do promeiro produto:"))
    p2 = float(input("qual o valor do segundo produto:"))
    p3 = float(input("qual o valor do terceiro produto:"))

    resultado = cal_preço(p1, p2, p3)
    print(resultado)
main()    