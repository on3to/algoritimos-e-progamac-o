#entrada

valor = int(input("Valor do saque: R$ "))

#processamento

notas50 = valor // 50
resto = valor % 50

notas10 = resto // 10
resto = resto % 10

notas5 = resto // 5
notas1 = resto % 5

#saida

print(f"Distribuição:")
print(f"{notas50} nota(s) de R$ 50")
print(f"{notas10} nota(s) de R$ 10")
print(f"{notas5} nota(s) de R$ 5")
print(f"{notas1} nota(s) de R$ 1")