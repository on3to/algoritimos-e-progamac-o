litros = float(input("Quantidade de litros: "))
tipo = input("Tipo (A-álcool, G-gasolina): ").upper()

if tipo == "A":
    preco = 1.90
    desconto = 0.03 if litros <= 20 else 0.05
elif tipo == "G":
    preco = 2.50
    desconto = 0.04 if litros <= 20 else 0.06

valor_total = litros * preco * (1 - desconto)
print(f"Valor a pagar: R$ {valor_total:.2f}")