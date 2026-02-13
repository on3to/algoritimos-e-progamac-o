#entrada
custofabrica = float(input("Digite o custo de fábrica do carro: "))

#processamento

distribuidor = custofabrica * 0.28
impostos = custofabrica * 0.45
custoconsumidor = custofabrica + distribuidor + impostos

#saida

print(f"O custo ao consumidor é: R$ {custoconsumidor:.2f}")