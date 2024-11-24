# Ejercicio: Manipulación de diccionarios (Dictionary Manipulation 1)

# Descripción:
# Este ejercicio demuestra cómo agregar nuevos pares clave:valor a un diccionario y cómo verificar
# si una clave específica existe en el diccionario. También practicaremos imprimir el contenido del diccionario.

# Objetivo:
# - Agregar dos nuevos pares clave:valor al diccionario.
# - Verificar si una clave específica está en el diccionario.
# - Imprimir el contenido actualizado del diccionario.

# Código en Python:

# Definición inicial del diccionario: países europeos y sus capitales.
europe = {
    'spain': 'madrid',
    'france': 'paris',
    'germany': 'berlin',
    'norway': 'oslo'
}

# 1. Agregar 'italy' con la capital 'rome' al diccionario.
europe['italy'] = 'rome'

# 2. Verificar si 'italy' ahora está en el diccionario e imprimir un mensaje.
print("¿Italy está en el diccionario 'europe'?", 'italy' in europe)

# 3. Agregar 'poland' con la capital 'warsaw' al diccionario.
europe['poland'] = 'warsaw'

# 4. Imprimir el contenido completo del diccionario actualizado.
print("Contenido actualizado del diccionario 'europe':", europe)

# Reflexión:
# - Los diccionarios permiten agregar pares clave:valor simplemente asignando un valor a una nueva clave.
# - Verificar si una clave existe en un diccionario es rápido y fácil usando el operador `in`.
# - Imprimir el contenido completo de un diccionario ayuda a verificar los cambios realizados.