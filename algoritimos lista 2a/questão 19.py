altura = float(input("Altura (m): "))
peso = float(input("Peso (kg): "))
imc = peso / (altura ** 2)

if imc < 25:
    print("Peso normal")
elif 25 <= imc <= 30:
    print("Obeso")
else:
    print("Obesidade mórbida")