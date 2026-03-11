num = int(input("Digite um número menor que 1000: "))

if num < 1000:
    c = num // 100
    d = (num % 100) // 10
    u = num % 10
    
    partes = []
    
    if c > 0:
        partes.append(f"{c} centena" + ("s" if c > 1 else ""))
    if d > 0:
        partes.append(f"{d} dezena" + ("s" if d > 1 else ""))
    if u > 0:
        partes.append(f"{u} unidade" + ("s" if u > 1 else ""))
        
    resultado = ""
    for i in range(len(partes)):
        if i == 0:
            resultado += partes[i]
        elif i == len(partes) - 1:
            resultado += " e " + partes[i]
        else:
            resultado += ", " + partes[i]
            
    print(resultado)