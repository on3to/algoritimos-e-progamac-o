#entrada

n1 = int(input("Numerador 1: "))
d1 = int(input("Denominador 1: "))
n2 = int(input("Numerador 2: "))
d2 = int(input("Denominador 2: "))

#processamento

numfinal = (n1 * d2) + (n2 * d1)
denfinal = d1 * d2

#saida

print(f"Resultado: {numfinal}/{denfinal}")