'''
Ejercicio 4

Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares
'''

j = int(input("Digita el primer numero en rango: "))
i = int(input("Digita el segundo numero en rango: "))


for k in range(j, i + 1):
    if k % 2 == 1:
        print(k)