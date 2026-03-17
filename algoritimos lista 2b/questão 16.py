tipo = int(input("Tipo (1-File, 2-Alcatra, 3-Picanha): "))
quantidade = float(input("Quantidade (Kg): "))
cartao = input("Cartão Tabajara? (S/N): ").upper()

if tipo == 1:
    nome_carne = "File"
    preco_unit = 4.90 if quantidade <= 5 else 5.80
elif tipo == 2:
    nome_carne = "Alcatra"
    preco_unit = 5.90 if quantidade <= 5 else 6.80
else:
    nome_carne = "Picanha"
    preco_unit = 6.90 if quantidade <= 5 else 7.80

preco_total = quantidade * preco_unit
desconto = preco_total * 0.05 if cartao == "S" else 0
valor_pagar = preco_total - desconto

print("\n--- CUPOM FISCAL ---")
print(f"Tipo: {nome_carne}")
print(f"Quantidade: {quantidade} Kg")
print(f"Preço Total: R$ {preco_total:.2f}")
print(f"Pagamento: {'Cartão Tabajara' if cartao == 'S' else 'Dinheiro/Outro'}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a Pagar: R$ {valor_pagar:.2f}")