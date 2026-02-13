#entrada
quantidadelatao = float(input("Quantidade de latão desejada (kg): "))

#processamento

cobre = quantidadelatao * 0.70
zinco = quantidadelatao * 0.30

#saida

print(f"Para {quantidadelatao}kg de latão, use:")
print(f"- {cobre:.2f}kg de cobre")
print(f"- {zinco:.2f}kg de zinco")