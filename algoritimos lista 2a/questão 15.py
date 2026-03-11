h1 = float(input("Horas Prof 1: "))
v1 = float(input("Valor/hora Prof 1: "))
h2 = float(input("Horas Prof 2: "))
v2 = float(input("Valor/hora Prof 2: "))

s1 = h1 * v1
s2 = h2 * v2

if s1 > s2:
    print("Professor 1 tem salário maior")
elif s2 > s1:
    print("Professor 2 tem salário maior")
else:
    print("Salários iguais")