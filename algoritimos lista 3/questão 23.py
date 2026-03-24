def main():
    n = int(input("Quantos funcionários serão cadastrados? "))

    for i in range(n):
        codigo = int(input("Código do funcionário: "))
        horas = float(input("Número de horas trabalhadas: "))
        dependentes = int(input("Número de dependentes: "))

        salario_bruto = (horas * 12) + (dependentes * 40)
        desconto_inss = salario_bruto * 0.085
        desconto_ir = salario_bruto * 0.05
        salario_liquido = salario_bruto - desconto_inss - desconto_ir

        print("Funcionário:", codigo)
        print("Desconto INSS:", desconto_inss)
        print("Desconto IR:", desconto_ir)
        print("Salário líquido:", salario_liquido)

main()