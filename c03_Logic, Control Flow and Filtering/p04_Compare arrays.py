# Ejercicio
# Comparar arrays con operadores de comparación.

# Descripción
# En este ejercicio, se utilizan operadores de comparación para trabajar
# con arrays de NumPy. Los arrays `my_house` y `your_house` representan 
# las áreas de diferentes habitaciones de dos casas (en metros cuadrados).
# Se realizarán comparaciones entre ellos y con un valor fijo (18 m²).

# Instrucciones
# 1. Genera un array booleano que indique qué áreas en `my_house` son mayores o iguales a 18.
# 2. Compara ambos arrays (`my_house` y `your_house`) elemento por elemento
#    para identificar qué áreas de `my_house` son más pequeñas que las de `your_house`.
# 3. Usa print() para mostrar los resultados de las comparaciones.

# Código en Python
# Importar la biblioteca NumPy
import numpy as np

# Crear el array `my_house` que contiene las áreas de habitaciones de la primera casa.
my_house = np.array([18.0, 20.0, 10.75, 9.50])  # Áreas en m²: cocina, sala, dormitorio, baño.

# Crear el array `your_house` con las áreas de habitaciones de la segunda casa.
your_house = np.array([14.0, 24.0, 14.25, 9.0])  # Áreas en m²: cocina, sala, dormitorio, baño.

# 1. Comparar `my_house` con el valor 18 para identificar las áreas mayores o iguales a 18.
# Esta comparación se realiza elemento por elemento.
print(my_house >= 18)
# Resultado esperado: [ True  True False False ].
# La comparación indica que solo las dos primeras áreas son mayores o iguales a 18.

# 2. Comparar `my_house` con `your_house` para identificar qué áreas son más pequeñas.
# Esta comparación se realiza elemento por elemento entre los dos arrays.
print(my_house < your_house)
# Resultado esperado: [False  True  True False].
# Indica que:
# - La cocina de `my_house` no es más pequeña que la de `your_house`.
# - La sala y el dormitorio de `my_house` sí son más pequeños.
# - El baño de `my_house` no es más pequeño.

# Explicaciones detalladas:
# - Línea 8-9: Se importan las funciones necesarias de NumPy.
# - Línea 12: Se define el array `my_house` con las áreas de las habitaciones.
# - Línea 15: Se define el array `your_house` con las áreas de las habitaciones.
# - Línea 18: La comparación `my_house >= 18` evalúa cada elemento en el array.
#   El resultado es un array booleano que indica qué áreas cumplen la condición.
# - Línea 22: La comparación `my_house < your_house` compara ambos arrays elemento a elemento.
#   Genera un array booleano indicando dónde los elementos de `my_house` son menores.
# - Línea 25-26: Se imprimen los resultados de las comparaciones para su inspección.