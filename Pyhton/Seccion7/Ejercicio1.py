'''
Ejercicio 1

En el siguiente diccionario se encuentran capitales de los paises en el mundo, debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se encuentra.

{"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
'''
'''
diccPaises = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Tegucigalpa","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}


paisUsuario = input("Ingresa el pais que quieras buscar: ")

if paisUsuario.capitalize() in diccPaises:
    print("La capital de {paisUsuario} es {diccPaises[paisUsuario.capitalize()]}")
else:
   print("La capital de {paisUsuario} es {diccPaises[paisUsuario.capitalize()]}")

'''

paises = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua",
"Costa Rica": "San Jose","Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota","Venezuela": "Caracas",
"España": "Madrid"}
 
 
solicitud = input("Porfavor ingresa un pais para saber si se encuentra en el diccionario: ").title()
 
if solicitud in paises:
    print(f"La capital de {solicitud} es {paises.get(solicitud)}")
else:
    print(f"{solicitud} no esta registrado en este diccionario")