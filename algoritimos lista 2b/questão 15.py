kg_morango = float(input("Kg de morango: "))
kg_maca = float(input("Kg de maçã: "))

if kg_morango <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20

if kg_maca <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

total_peso = kg_morango + kg_maca
total_valor = (kg_morango * preco_morango) + (kg_maca * preco_maca)

if total_peso > 8 or total_valor > 25:
    total_valor *= 0.90

print(f"Valor a pagar: R$ {total_valor:.2f}")