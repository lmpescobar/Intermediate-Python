# Ejercicio: Acceder a valores en un diccionario (Access dictionary)

# Descripción:
# En este ejercicio aprenderemos cómo acceder a las claves y valores de un diccionario en Python.
# Usaremos un diccionario que mapea países europeos a sus capitales y exploraremos los métodos `keys()` 
# para obtener las claves y el acceso directo mediante una clave específica para obtener un valor.

# Objetivo:
# - Imprimir todas las claves del diccionario usando el método `keys()`.
# - Acceder y mostrar el valor correspondiente a una clave específica ('norway').

# Código en Python:

# Definición del diccionario: países europeos y sus capitales.
europe = {
    'spain': 'madrid',
    'france': 'paris',
    'germany': 'berlin',
    'norway': 'oslo'
}

# 1. Imprimir todas las claves del diccionario usando el método `keys()`.
print("Claves del diccionario 'europe':", europe.keys())

# 2. Acceder y mostrar el valor correspondiente a la clave 'norway'.
capital_norway = europe['norway']  # Acceso al valor mediante la clave.
print("La capital de Norway es:", capital_norway)

# Reflexión:
# - El método `keys()` devuelve una vista de todas las claves del diccionario, útil para explorar los datos.
# - Acceder a un valor mediante una clave es directo, eficiente y evita la necesidad de usar índices como en las listas.
# - Los diccionarios permiten manejar datos relacionados de forma clara y organizada.