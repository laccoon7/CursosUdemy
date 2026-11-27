'''
Ejercicio 4

Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
'''

facturaUsuario = int(input("Ingresa del producto que vas a comprar: "))

iva = int(input("Ingresa el valor del IVA: "))

def factura():
    if iva != 0:
        if iva > 0:
            totalPagar = ((facturaUsuario * iva) / 100) + facturaUsuario
            return totalPagar
        else: 
            print("El monto de IVA es negativo. Ingrese un IVA valido")
    else:
        totalPagar = (facturaUsuario * 0.21) + facturaUsuario
        return totalPagar


print("El total de su factura es:", factura())