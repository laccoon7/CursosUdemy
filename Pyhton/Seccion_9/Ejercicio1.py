'''
Ejercicio 1

Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero
'''

j = int(input("Ingresa el numero que deses: "))
i = 0

while i < 10:
    i += 1
    resultado = j * i
    
    print("{} x {} = {}".format(j,i,resultado))