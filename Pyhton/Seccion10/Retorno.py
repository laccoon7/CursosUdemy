''' EJEMPLO DE LO QUE ES UNA FUNCION
def <nombre de la funcion>():
    <sentencias>
    <sentencias>
    <sentencias>
'''

def entero():
    print("Este es un dato entero: ")
    return 10

def decimal():
    print("Este es un dato decimal")
    return 90.99

def frase():
    return "Mi nombre es Lacc"

def asignacion():
    return 1 , 2 , 3 , 4 , 5

print(entero())
print(decimal())
print(frase())

a,b,c,d,e = asignacion()