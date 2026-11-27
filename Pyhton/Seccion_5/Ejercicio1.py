'''
Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal
'''

vocal = input("Ingrese una letra: ")

if vocal.lower() in "aeiou":
    print("ES vocal")
else:
    print("NO es vocal")