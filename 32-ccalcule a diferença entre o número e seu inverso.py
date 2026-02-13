#entrada
num = int(input("Digite um número de 3 dígitos: "))

#processamento

centena = num // 100
resto = num % 100
dezena = resto // 10  #OBS:tbm poderia usar int(str(num)[::-1]) para inverter 
unidade = resto % 10

inverso=unidade*100 + dezena*10 + centena

diferenca = num - inverso

#saida 

print(f"Diferença ({num} - {inverso}): {diferenca}")