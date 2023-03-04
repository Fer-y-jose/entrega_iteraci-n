"""Se quiere conservar el historial de los movimientos mensuales en una cuenta corriente.
1. Modificar el tipo CUENTA definido en el capítulo «Estructuras elementales» para conservar el rastro
de los movimientos en una cuenta durante un mes.
2. Establecer el saldo a final de mes de una cuenta dada.
El saldo ya no es un atributo de la cuenta. Se obtiene recorriendo el historial mensual y anual que
registra el importe del saldo de la cuenta para cada mes.
3. Rehacer las definiciones anteriores.
Una tabla clientes contiene las cuentas corrientes de un conjunto de clientes.
4. Determinar los clientes para los que la media de los importes de los movimientos es superior a una suma dada.
El ejercicio siguiente se resolverá por completo en el capítulo «Edición de un número»."""
Cuentas = {
    "Cuenta1": {"Nombre": "Juan", "Saldo": 1000, "Movimientos": [100, 200, 300, 400, 500]},
    "Cuenta2": {"Nombre": "Pedro", "Saldo": 2000, "Movimientos": [ 500, 600, 700, 800, 900, 1000]},
    "Cuenta3": {"Nombre": "Maria", "Saldo": 3000, "Movimientos": [400, 500, 600, 800, 900, 1000]},
}
print(Cuentas)
def CrearCuenta (): # Esta funcion crea las cuentas con los valores, nombre, saldo y movimientos
    while True: 
        continuar2 = input ("¿Desea crear una cuenta? ")
        if continuar2 == "No":
            break
        else:
            numeroCuenta = input ("Introduzca el numero de cuenta: ")
            nombre = input ("Introduzca el nombre del cliente: ")
            saldo = input ("Introduzca el saldo de la cuenta: ")
            movimientosTotales = []
            while True:
                movimientos = input ("Introduzca los movimientos de la cuenta: ")
                movimientosTotales.append(movimientos)
                continuar = input ("¿Desea introducir otro movimiento?: ")
                if continuar == "No":
                    break
                else:
                    continue
            Cuentas[numeroCuenta] = {"Nombre": nombre, "Saldo": saldo, "Movimientos": movimientosTotales}
def movimientosFinalDeMes():
    dinero = 0
    while True:
        movimiento = input("Introduzca los movimientos de la cuenta: ")
        continuar = input("¿Desea introducir otro movimiento?: ")
        if continuar == "No":
            dinero += int(movimiento)
            break
        else:
            continue
    for cuenta in Cuentas:
        cuenta["Movimientos"] = dinero
def establecerSaldo():
    saldos = {}
    numero = 0
    for cuenta in Cuentas:
        numero +=1
        adde = {}
        saldo = Cuentas[cuenta]["Saldo"]
        for movimiento in Cuentas[cuenta]["Movimientos"]:
            saldo += int(movimiento)
        Cuentas[cuenta]["Saldo"] = saldo
        adde["Nombre"] = Cuentas[cuenta]["Nombre"]
        adde["Saldo"] = Cuentas[cuenta]["Saldo"]
        saldos[numero] = adde
    print(saldos)
print(establecerSaldo())
print(Cuentas)
