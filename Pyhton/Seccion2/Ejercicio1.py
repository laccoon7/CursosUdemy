cadena = 'Te quiero solo como amigo'
#tamaño de la cadena: 25

#Imprimir los primeros dos caracteres
print(cadena[0:2])

#Imprimir los tres ultimos caracteres
print(cadena[-3: ])

#Imprimir la cadena cada dos caracteres // Ej.: Si la cadena fuera “recta” debería imprimir rca
print(cadena[ : : 2])

#La cadena en sentido inverso
print(cadena[ : : -1])

#La cadena en sentido normal y luego inverso
print(cadena + cadena[: : -1])