#entrada
mtotal = int(input("Digite a quantidade de metros: "))

#processamento

km = mtotal // 1000
mrestante = mtotal % 1000

#saida

print(f"Resultado: {km}km e {mrestante}m")