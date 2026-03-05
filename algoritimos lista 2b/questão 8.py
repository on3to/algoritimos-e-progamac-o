

def main():

    valor_horas = float(input("qual o valor da hora de tabalho:"))
    quant_horas = float(input("quantas horas foram trabalhadas:"))

    salario = valor_horas * quant_horas

    if salario <= 900:
        perdentual = 0
    elif salario <= 1500:
        perdentual = 5
    elif salario <= 2500:
        perdentual =  10
    else:
        perdentual = 20


        ir = salario * (perdentual/100) 
        inss = salario * 0,10
        fgts = salario * 0,11
        sindicato =  salario * (3/100)
        tdesconto = ir + inss + sindicato
        salario_liquido = salario - tdesconto

        print(f"O salario bruto e de {valor_horas}+{quant_horas}:{salario}")
        print(f"o desconto de inposto de renda e de {ir}")
        print(f"O desconto do inss e de {inss}")
        print(f"o desconto de fgts e de {fgts}")
        print(f"O total de desconto e de:{tdesconto}")
        print(f"O salario liquido e de:{salario_liquido}")

main()