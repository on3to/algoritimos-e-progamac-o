angulo = float(input("Ângulo (0-360): "))

if 0 <= angulo <= 90:
    print("Primeiro quadrante")
elif 90 < angulo <= 180:
    print("Segundo quadrante")
elif 180 < angulo <= 270:
    print("Terceiro quadrante")
elif 270 < angulo <= 360:
    print("Quarto quadrante")