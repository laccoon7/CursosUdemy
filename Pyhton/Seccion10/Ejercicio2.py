'''
Ejercicio 2

Escribir una función que reciba un número entero positivo y devuelva su factorial.
'''

import math

def numeroEntPosAFactorial():
    datoUsuario = int(input("Ingresa un numero positivo para saber su factorial: "))
    if datoUsuario > 0:

        print("Tu factorial de tu numero es: {}".format(math.factorial(datoUsuario)))
    else:
        print("Tu numero no es positivo")

numeroEntPosAFactorial()


numeroEntPosAFactorial()