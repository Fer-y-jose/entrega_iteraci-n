"""Un número entero natural es un cuadrado perfecto si es el cuadrado de un número entero.
 Así, 0 = 02, 1 = 12, 4 = 22, 16 = 42 son cuadrados perfectos.

1. Hacer un algoritmo que establezca la lista de los cuadrados perfectos inferiores a un límite dado.
 El algoritmo no debe hacer multiplicaciones.

La raíz cuadrada entera de un número entero n ≥ 0 es el único número entero r ≥ 0 definido por:

r2 ≤ n < (r + 1)2 
2. Escribir el algoritmo de cálculo de la raíz cuadrada entera de un número entero."""
lista = []
def calculador_de_cuadrados_perfectos(n):
    valor = ("{}^2 =".format(n), n ** 2)
    return valor
def main(n):
    calculador_de_cuadrados_perfectos(n)
    if n > 0:
            main(n-1)
            lista.append(calculador_de_cuadrados_perfectos(n-1))
    return lista
print(main(8))
def raiz_cuadrada(n):
    valor2 = ("{}^2 <= {} < {}". format(n, n ** 2, (n + 1) ** 2))
    return valor2
def main2(n):
    raiz_cuadrada(n)
    if n > 0:
        main2(n-1)
        lista.append(raiz_cuadrada(n-1))
    return lista
print(main2(8))