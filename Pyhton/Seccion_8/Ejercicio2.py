'''
Ejercicio 2

Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario un número, el que haya ingresado, es la letra que debe imprimir el programa
'''

tuplaAbededario = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"ñ",16:"o",17:"p",18:"q",19:"r",20:"s",21:"t",22:"u",23:"v",24:"w",25:"x",26:"y",27:"z"}

opcionUsuario = input("Elige el numero: ")

if opcionUsuario in tuplaAbededario:
    print(tuplaAbededario[opcionUsuario])
else:
    print("Esa letra no existe en el abecedario")