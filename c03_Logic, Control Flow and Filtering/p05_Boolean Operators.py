# Ejercicio
# Operadores booleanos en Python y NumPy

# Descripción:
# En este ejercicio, aprenderás a usar operadores booleanos (`and`, `or`, `not`) y 
# sus equivalentes para arrays de NumPy (`logical_and`, `logical_or`, `logical_not`).
# Se explorarán ejemplos elementales y el uso de NumPy para realizar comparaciones.

# Instrucciones:
# 1. Usa operadores booleanos básicos para realizar comparaciones entre valores.
# 2. Usa los operadores de NumPy (`logical_and`, `logical_or`) para comparar elementos
#    dentro de arrays. Por ejemplo, calcula qué valores de un array están en un rango dado.

# Código en Python:

# 1. Ejemplos básicos de operadores booleanos.
x = 12  # Variable entera
y = 5   # Variable entera

# Usando `and` para comprobar si x está entre 5 y 15.
print(x > 5 and x < 15)  # True: 12 está entre 5 y 15.

# Usando `or` para verificar si y es menor que 7 o mayor que 13.
print(y < 7 or y > 13)  # True: y (5) es menor que 7.

# Usando `not` para negar un valor booleano.
print(not True)  # False: la negación de True es False.

# 2. Uso de NumPy para operaciones con arrays.
import numpy as np  # Importar la biblioteca NumPy.

# Crear un array `bmi` con valores de índice de masa corporal.
bmi = np.array([21.852, 20.975, 21.75, 24.747, 21.441])

# Comparar elementos del array con un rango usando `logical_and`.
bmi_in_range = np.logical_and(bmi > 21, bmi < 22)
print(bmi_in_range)  # [True False True False True]: Elementos dentro del rango.

# Filtrar el array para obtener solo los valores que están en el rango.
bmi_filtered = bmi[bmi_in_range]
print(bmi_filtered)  # [21.852 21.75 21.441]: Valores entre 21 y 22.

# Explicación detallada:
# - Línea 9: Se usa `and` para combinar dos condiciones booleanas.
# - Línea 12: `or` evalúa si al menos una de las dos condiciones es True.
# - Línea 15: `not` invierte un valor booleano.
# - Línea 19: Se define un array de ejemplo `bmi`.
# - Línea 22: `np.logical_and` compara elemento a elemento del array para determinar
#   si los valores están entre 21 y 22.
# - Línea 25: El resultado booleano se usa para filtrar el array `bmi` y obtener
#   únicamente los valores que cumplen con la condición.

# Resultados esperados:
# True
# True
# False
# [True False True False True]
# [21.852 21.75 21.441]