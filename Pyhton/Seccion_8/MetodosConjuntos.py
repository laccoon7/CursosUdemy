conjuntoEjemplo = {1,1,2,2, 2 , 3,3,3,3 , 4 ,5,5, 5} # Muestra solo datos unicos, excluyendo los valores repetidos
listaEjemplo = [1,2,2,2,3,4,5] # Imprime la lista como esta, aunque tenga datos repetidos

#print(listaEjemplo)
#print(conjuntoEjemplo)

conjunto = {1,2,3,4,5}
print("Este es el original: {} ".format(conjunto))

conjunto.add(20) # Añade el valor entre los parentesis, siempre es al final
print(conjunto)

conjunto.remove(1) #.discard es lo mismo
print(conjunto)

conjunto.pop() # Elimina un valor aleatorio del conjunto
print(conjunto)

conjunto.update([1,2,3])
print(conjunto)

conjunto.clear()
print(conjunto)