"""Cuando la base es superior a 36, se puede utilizar la representación de los
números en base diez, pero separando cada cifra de la representación del número
en base B mediante un separador convenido, por ejemplo, un punto. Eso es lo que
se usa para expresar, por ejemplo, la dirección IP de un host en una red con IPv4.
Así, por ejemplo, la representación en base 256 de 3000, expresada aquí en base diez,
se escribirá: 11 184256 = 3000diez.
"""
def conversor(numero, base):
    if numero == 0:
        return 0
    else:
        contador = 0
        while numero > base:
            numero -= base
            contador += 1
        print(contador, numero)
print(conversor(3000, 256))