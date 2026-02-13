#entrada

anos = int(input("Anos: "))
meses = int(input("Meses: "))
dias = int(input("Dias: "))

#processamento 

totaldias = (anos * 365) + (meses * 30) + dias

#saida

print(f"A idade total em dias é: {totaldias}")
