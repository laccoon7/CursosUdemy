'''
Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas
'''

print("Coloque una vocal miniscula y una mayuscula")

vocalMinus = input("Ingresa la vocal minuscula:")

letraMayus = input("Ingresa la vocal mayuscula:")


if (vocalMinus in "aeiou") and (letraMayus.isupper()):
    print("Tu vocal minuscula ahora es mayuscula:{}".format(vocalMinus.swapcase()))
    print("Tu letra mayuscula ahora es minuscula:{}".format(letraMayus.swapcase()))
    print(vocalMinus.swapcase() + letraMayus.swapcase())
else:
    print("Entrada invalida. Revisa los datos ingresados.")