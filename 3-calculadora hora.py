#entrada
minuto = int(input("Digite o minuto: "))

#processamento 

horas = minuto //60 
minutosfinal = minuto - (horas *60)

#saida
print(f"{horas} horas e {minutosfinal} minutos")