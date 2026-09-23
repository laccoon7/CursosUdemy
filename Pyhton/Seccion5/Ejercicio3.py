'''
Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
'''

palabra1 = input("Ingresa tu primera palabra: ")
palabra2 = input("Ingresa tu segunda palabra: ")

if palabra1[-3:0] == palabra2[-3:0]:
    print("Las palabras riman!!")
elif palabra1[-2:0] == palabra2[-2:0]:
    print("Las palabras solo un poquito..")
else:
    print("Las palabras no riman LOL")