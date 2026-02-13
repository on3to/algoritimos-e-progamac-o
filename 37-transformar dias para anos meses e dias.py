#entradad

diastotal = int(input("Digite a idade em dias: "))

#processamento

anos = diastotal // 365
meses = (diastotal % 365) // 30
dias = (diastotal % 365) % 30

#saida

print(f"Resultado: {anos} ano(s), {meses} mês(es) e {dias} dia(s)")