dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

valida = False

if 1 <= mes <= 12:
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= dia <= 31:
            valida = True
    elif mes in [4, 6, 9, 11]:
        if 1 <= dia <= 30:
            valida = True
    elif mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if 1 <= dia <= 29:
                valida = True
        elif 1 <= dia <= 28:
            valida = True

if valida:
    print("Data válida")
else:
    print("Data inválida")