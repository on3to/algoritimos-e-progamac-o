#entrada
numero = int(input("Digite um número inteiro: "))
#processamento
#centena = math.trunc(numero/100)
centena = numero // 100
resto = numero % 100
dezena = resto // 10
unidade = resto % 10
#saida
soma = centena + dezena + unidade
print(f"A soma dos algarismos é: {soma}")
