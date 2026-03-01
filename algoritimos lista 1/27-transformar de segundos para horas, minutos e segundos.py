#entrada
segtotal = int(input("Digite a quantidade de segundos: "))

#processamento

horas = segtotal // 3600
minutos = (segtotal % 3600) // 60
segundos = segtotal % 60

#saida 

print(f"Resultado: {horas}h, {minutos}min e {segundos}s")