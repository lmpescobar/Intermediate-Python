# Explicación completa de operadores de comparación en Python.

# Introducción:
# Los operadores de comparación en Python permiten evaluar cómo se relacionan dos valores.
# El resultado siempre será un valor booleano (`True` o `False`).
# Aquí explicaremos su uso con ejemplos detallados.

# 1. Comparaciones Numéricas
# Los operadores de comparación básicos incluyen: 
# - Mayor que (>)
# - Menor que (<)
# - Mayor o igual que (>=)
# - Menor o igual que (<=)
# - Igualdad (==)
# - Desigualdad (!=)

# Ejemplo 1.1: Comparación de enteros
print(2 > 1)  # Verifica si 2 es mayor que 1. Resultado: True
print(2 < 3)  # Verifica si 2 es menor que 3. Resultado: True
print(2 == 2)  # Verifica si 2 es igual a 2. Resultado: True
print(2 != 3)  # Verifica si 2 es diferente de 3. Resultado: True
print(2 >= 2)  # Verifica si 2 es mayor o igual a 2. Resultado: True
print(3 <= 2)  # Verifica si 3 es menor o igual a 2. Resultado: False

# 2. Comparaciones con Variables
# Los operadores de comparación también funcionan con variables que contienen valores.
a = 5
b = 10
print(a < b)  # Verifica si el valor de 'a' es menor que 'b'. Resultado: True

# 3. Comparaciones entre Tipos de Datos Similares
# Python permite comparar valores del mismo tipo, como cadenas de texto o números.

# Ejemplo 3.1: Comparación de cadenas de texto
# En las cadenas, el orden alfabético (según el código ASCII) es la referencia.
print("carl" < "chris")  # Verifica si "carl" viene antes que "chris" alfabéticamente. Resultado: True
print("apple" == "Apple")  # Verifica si "apple" es igual a "Apple" (Python distingue mayúsculas). Resultado: False

# Ejemplo 3.2: Comparación de números flotantes y enteros
x = 5.0
y = 5
print(x == y)  # Verifica si 5.0 (float) es igual a 5 (int). Resultado: True

# 4. Comparaciones entre Tipos Incompatibles
# Comparar tipos diferentes (por ejemplo, cadena con número) genera un error.
# Descomentar el siguiente código para ver el error:
# print(3 < "chris")  # Esto generará un TypeError porque no se puede comparar un número con una cadena.

# 5. Uso de Operadores de Comparación con NumPy
# NumPy permite realizar comparaciones elemento por elemento en arreglos.
import numpy as np

# Creamos un array llamado `bmi` con valores de índice de masa corporal.
bmi = np.array([18.5, 22.0, 24.5, 27.8])

# Comparamos cada elemento del array con el número 23.
# NumPy crea un nuevo array booleano con el resultado de la comparación para cada elemento.
result = bmi > 23
print(result)  # Resultado: [False False  True  True]

# Podemos usar este array booleano para filtrar los valores que cumplen la condición.
filtered_bmi = bmi[result]
print(filtered_bmi)  # Muestra los valores de `bmi` mayores que 23. Resultado: [24.5 27.8]

# 6. Tabla de Operadores de Comparación
# Aquí está la lista completa de operadores de comparación:
# >   : Mayor que
# <   : Menor que
# >=  : Mayor o igual que
# <=  : Menor o igual que
# ==  : Igualdad
# !=  : Desigualdad

# Conclusión:
# Los operadores de comparación son herramientas fundamentales en Python.
# Nos permiten tomar decisiones y trabajar con datos de manera eficiente.
# Practica con diferentes tipos de datos y experimenta con NumPy para aprovechar todo su potencial.