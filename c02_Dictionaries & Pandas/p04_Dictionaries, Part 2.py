# Ejercicio: Manipulación de diccionarios (Dictionaries, Part 2)

# Descripción:
# En este ejercicio exploraremos cómo agregar, actualizar y eliminar elementos en un diccionario. 
# También analizaremos las diferencias clave entre listas y diccionarios, y cuándo es apropiado usar cada uno.

# Objetivo:
# - Agregar una nueva clave y valor al diccionario.
# - Actualizar el valor de una clave existente.
# - Eliminar una clave y su valor del diccionario.
# - Comparar el uso de listas y diccionarios.

# Código en Python:

# Diccionario inicial: población mundial (en millones).
world = {
    'afghanistan': 30.55,
    'albania': 2.77,
    'algeria': 39.21
}

# 1. Agregar un nuevo par clave:valor.
# Agregar 'sealand' con una población de 0.000027 millones (27 habitantes).
world['sealand'] = 0.000027
print("Después de agregar Sealand:", world)

# 2. Comprobar si 'sealand' está en el diccionario.
print("¿Sealand está en el diccionario?", 'sealand' in world)

# 3. Actualizar el valor de 'sealand' a 0.000028 millones (28 habitantes).
world['sealand'] = 0.000028
print("Después de actualizar Sealand:", world)

# 4. Eliminar la clave 'sealand' del diccionario.
del world['sealand']
print("Después de eliminar Sealand:", world)

# Reflexión:
# - Las claves en un diccionario deben ser únicas. Si intentas agregar un valor con una clave existente,
#   el valor será actualizado en lugar de crear una nueva entrada.
# - Las claves deben ser tipos inmutables, como cadenas, enteros o tuplas. Las listas no pueden usarse como claves.

# Comparación: Lista vs Diccionario
# - Listas: Una secuencia ordenada de valores indexados numéricamente.
#   Útil cuando el orden importa o cuando se necesita seleccionar subconjuntos de datos.
population_list = [30.55, 2.77, 39.21]

# - Diccionarios: Una colección de pares clave:valor, indexados por claves únicas.
#   Útil para búsquedas rápidas y cuando se necesita asociar datos relacionados.
population_dict = {
    'afghanistan': 30.55,
    'albania': 2.77,
    'algeria': 39.21
}

# Ejemplo:
# Acceso en una lista requiere índices.
print("Población de Albania (lista):", population_list[1])

# Acceso en un diccionario usa claves.
print("Población de Albania (diccionario):", population_dict['albania'])

# Reflexión adicional:
# - Usa listas cuando necesites preservar el orden o acceder a subconjuntos.
# - Usa diccionarios cuando necesites una estructura de búsqueda rápida con claves únicas.