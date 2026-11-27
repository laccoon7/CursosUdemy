diccionario = {1 : 2, 2 : 3, 3 : 4 }
diccionario2 = {4 : 5, 6 : 7}
print(diccionario)

#Concatena ambas variables en una sola, la que esta dentro de los parametros es la que se va a poner en la que se imprime
diccionario.update(diccionario2)
print(diccionario)

#Agrega un nuevo dato al diccionario
diccionario.setdefault(4 , 5)
print(diccionario)

#Regresa la clave que se pide entro del parametro
print(diccionario.get(2))

#Copia el diccionario
diccionario.copy()
print(diccionario)

#Elimina la clave que se da en el parametro
diccionario.pop(1)
print(diccionario)

#Limpia/Elimina el diccionario
diccionario.clear()
print(diccionario)