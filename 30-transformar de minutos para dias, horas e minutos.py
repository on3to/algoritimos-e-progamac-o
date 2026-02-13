#entrada
minutostotal = int(input("Digite a quantidade de minutos: "))

#processamento

dias = minutostotal // 1440 
horas = (minutostotal % 1440) // 60
minutos = minutostotal % 60

#saida 

print(f"Resultado: {dias} dia(s), {horas} hora(s) e {minutos} minuto(s)")