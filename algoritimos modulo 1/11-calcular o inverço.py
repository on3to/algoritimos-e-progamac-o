#entrada 
numero= int(input("Digite um número inteiro: "))

#processamento
centena = numero // 100
resto = numero % 100
dezena = resto // 10
unidade = resto % 10

#saida 
resultado=unidade*100 + dezena*10 + centena

print(f"O numero {numero} convertido e: {resultado}")
