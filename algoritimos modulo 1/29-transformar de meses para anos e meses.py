#entrada

mesestotal = int(input("Digite a quantidade de meses: "))

#processamento

anos = mesestotal // 12
meses = mesestotal % 12

#saida

print(f"Resultado: {anos} ano(s) e {meses} mês(es)")