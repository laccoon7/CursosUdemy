'''
Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:

Te llamas: <nombre>

Tu edad es: <edad>

Eres: <sexo>
'''
print("Datos")

nombre = input("Ingresa tu nombre:")
edad = int(input("Ingresa tu edad:"))
sexo = input("Ingresa tu sexo:")

print("Tu nombre es: {}\nTu Edad es: {}\nTu sexo es: {}".format(nombre,edad,sexo))