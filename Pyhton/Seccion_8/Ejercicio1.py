'''
Ejercicio 1

Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla
'''

tuplaMeses = {
    1:"Enero",
    2:"Febrero",
    3:"Marzo",
    4:"Abril",
    5:"Mayo",
    6:"Junio",
    7:"Julio",
    8:"Agosto",
    9:"Septiembre",
    10:"Octubre",
    11:"Noviembre",
    12:"Diciembre"
}

opcionUsuario = int(input("Ingresa el numero de mes que buscas: "))

if opcionUsuario in tuplaMeses:
    print(tuplaMeses[opcionUsuario])
else:
    print("Este numero de mes no existe")