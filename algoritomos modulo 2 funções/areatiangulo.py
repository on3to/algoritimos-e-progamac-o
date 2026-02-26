import math

def area_triangulo(a, b, c):
    
    a + b > c and a +c > b and b + c > a
    s = (a + b + c)/2

    area = math.sqrt (s * (s - a) * (s - b) * (s - c))