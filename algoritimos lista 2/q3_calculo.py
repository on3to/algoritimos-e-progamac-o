def verificar(a, b, c):

    if a > b and a > c:
        return ("o primeiro numero e maior")
    elif b > a and b> c:
        return ("o segundo numero e maior")
    elif c > a and c > b:
        return ("o terceiro numero e maioir")
    else:
        return("os numeros são iguais")
    