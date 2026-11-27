'''
Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:

PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6

Donde: P1, P2, P3 : Practicas

PP: promedio de práctica

PROM: promedio

EP: examen parcial

EF: examen final

'''
print("Calculadora de evaluacion del alumno \n")

P1 = float(input('Ingresa el valor de la EV1:'))
P2 = float(input('Ingresa el valor de la EV2:'))
P3 = float(input('Ingresa el valor de la EV3:'))
EP = float(input('Ingresa el valor del Examen Parcial:'))
EF = float(input('Ingresa el valor del Examen Final:'))


PP = (P1 + P2 + P3) / 3

PROM = (PP + 2*EP + 3*EF) / 6

calificacion = (PP + PROM) / 2

if (calificacion >= 70): 
    print("Sacaste:",calificacion,"pasaste :D ")

else:
    print("Sacaste:",calificacion,"no pasaste D: ")

