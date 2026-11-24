'''
Ejercicio 1

Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas
'''
listaPrincipal = []
listaPares = []
listaImprares = []

def agregarDatosUsuario():
    while len(listaPrincipal) < 10:
        datosUsuario = int(input("Agrega 10 numeros a la tabla: "))
        listaPrincipal.append(datosUsuario)
    print("Esta es la lista principal\n{}\n".format(listaPrincipal))

def ordenarNumeros ():
    for i in listaPrincipal:
        if i % 2 ==0:
            listaPares.append(i)
        else:
            listaImprares.append(i)
    print("Lista pares: {}".format(listaPares))
    print("Lista impares: {}".format(listaImprares))


agregarDatosUsuario()
ordenarNumeros()

