# Mi solucion
'''
print("Programa para calcular la formula general")

a = float(input('Ingresa el valor "a" '))
b = float(input('Ingresa el valor "b" '))
c = float(input('Ingresa el valor "c" '))

print(a)
print(b)
print(c)

x1 = ( (-b) + (((b**2) - (4(a*c)))**0.5)) / (2(a))

x2 = ( (-b) - (((b**2) - (4*(a*c))**0.5)) / (2(a)))

print('Los resultados son "+" = {x1} y "-" ={x2}')
'''
#Solucion clase

from math import sqrt

a = float(input('Ingresa el valor "a" '))
b = float(input('Ingresa el valor "b" '))
c = float(input('Ingresa el valor "c" '))
x1 = 0
x2 = 0

if ((b**2) - (4*a*c)) <0:
    print("No se puede realizar porque no se puede scar la raiz cuadrada de un numero negativo")
else:
    x1 = (-b + sqrt(((b**2)-(4*a*c))))/(2*a)
    x2 = (-b - sqrt(((b**2)-(4*a*c))))/(2*a)
    print("La solucion es: \nx1=",x1, "\nx2=",x2)