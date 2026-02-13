#entrada

valor_mercadoria = float(input("Valor da mercadoria: R$ "))

#processamento

prestacao = int(valor_mercadoria // 3)

entrada = valor_mercadoria - (2 * prestacao)

#saida

print(f"Entrada: R$ {entrada:.2f}")
print(f"Duas prestações de: R$ {prestacao:.2f}")