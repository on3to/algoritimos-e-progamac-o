#entrada
anos = int(input("Anos fumando: "))
cigarrosdia = int(input("Cigarros por dia: "))
precocarteira = float(input("Preço da carteira (20 cigarros): "))

#processamento

totalcigarros = anos * 365 * cigarrosdia
carteirasconsumidas = totalcigarros / 20
gastototal = carteirasconsumidas * precocarteira

#saida

print(f"O valor total gasto foi: R$ {gastototal:.2f}")