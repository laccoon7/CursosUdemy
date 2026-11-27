'''
Ejercicio 2

Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''
j = int(input("Cual es tu edad? "))
i = 1
while i <= j:
    print("Has cumplido : {} años".format(i))
    i += 1