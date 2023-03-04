"""El algoritmo que permite determinar el máximo común divisor de dos números
 enteros también se estudia en el capítulo «Recursividad», durante el estudio del tipoFRACCIÓN. 
1. Dar una versión iterativa del algoritmo de Euclides para el cálculo del mcd
 de dos números enteros.
2. Estudiar una versión iterativa que calcula el mcd haciendo solo sumas o restas.
"""
def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def mcd_solo_sumas_y_restas(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
print(mcd(1500, 3000))
print(mcd_solo_sumas_y_restas(98, 140))