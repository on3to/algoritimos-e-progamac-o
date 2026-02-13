#entrada
horas_total = int(input("Digite a quantidade de horas: "))

#preocessamento

semanas = horas_total // 168  
dias = (horas_total % 168) // 24
horas = horas_total % 24

#saida

print(f"Resultado: {semanas} semana(s), {dias} dia(s) e {horas} hora(s)")