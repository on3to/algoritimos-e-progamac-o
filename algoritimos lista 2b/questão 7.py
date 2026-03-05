
def main():
   salario = float(input("Digite o salário atual do colaborador: "))


   if salario <= 280:
    percentual = 20
   elif salario <= 700:
    percentual = 15
   elif salario <= 1500:
    percentual = 10
   else:
    percentual = 5


    valor_aumento = salario * (percentual / 100)
    novo_salario = salario + valor_aumento
    

    print(f"O salario antes do resjuste era de {salario} com o aumento aplicado de {percentual}% isso e um aumento de {valor_aumento}, com isso o novo salario passa a ser de {novo_salario}")






main()