#entrada
diastotal = int(input("Digite a quantidade de dias: "))

#processamento 

semanas = diastotal // 7
diasrestantes = diastotal % 7

#saida

print(f"Resultado: {semanas} semana(s) e {diasrestantes} dia(s)")