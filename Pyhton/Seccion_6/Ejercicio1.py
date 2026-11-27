'''
Ejercicio 1

En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

[20, 50, "Curso", 'Python', 3.14]
'''
lista = [20, 50, "Curso", 'Python', 3.14]
print("Esta es la lista actual:\n{}".format(lista))

print("Ingresa los datos por los cuales se sustituiran el primer y segundo lugar: ")

dato1 = input("Ingresa el primer dato: ")
dato2 = input("Ingresa el segundo dato: ")


lista[0] = dato1
lista[1] = dato2

print("Esta es tu nueva lista:\n{}".format(lista))