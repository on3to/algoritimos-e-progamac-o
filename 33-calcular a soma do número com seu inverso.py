#entrada
num = int(input("Digite um número de 3 dígitos: "))

#processamento 

centena = num // 100
resto = num % 100
dezena = resto // 10  
unidade = resto % 10

inverso=unidade*100 + dezena*10 + centena

soma = num + inverso

#saida

print(f"Soma ({num} + {inverso}): {soma}")