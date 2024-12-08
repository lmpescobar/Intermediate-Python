# Ejercicio
# Operadores booleanos con NumPy

# Descripción:
# Este ejercicio utiliza operadores lógicos en arreglos de NumPy.
# En NumPy, los operadores como `and`, `or`, y `not` no funcionan directamente.
# Por lo tanto, debemos utilizar las funciones específicas de NumPy: `np.logical_and()`,
# `np.logical_or()`, y `np.logical_not()`.

# Instrucciones:
# 1. Crear dos arreglos de NumPy llamados `my_house` y `your_house`.
# 2. Determinar cuáles áreas en `my_house` son mayores a 18.5 o menores que 10.
# 3. Determinar cuáles áreas en ambos arreglos (`my_house` y `your_house`) son menores que 11.
# 4. Asegúrate de envolver ambas respuestas en un comando `print()` para inspeccionar el resultado.

# Código en Python
import numpy as np  # Importar la biblioteca NumPy

# Crear los arreglos
my_house = np.array([18.0, 20.0, 10.75, 9.50])  # Áreas de mi casa
your_house = np.array([14.0, 24.0, 14.25, 9.0])  # Áreas de tu casa

# Evaluar las áreas en `my_house` que son mayores a 18.5 o menores que 10
result1 = np.logical_or(my_house > 18.5, my_house < 10)

# Evaluar las áreas en ambos arreglos que son menores que 11
result2 = np.logical_and(my_house < 11, your_house < 11)

# Imprimir los resultados
print("Áreas en 'my_house' mayores a 18.5 o menores que 10:")
print(result1)  # Resultado booleano para cada elemento

print("\nÁreas menores a 11 en ambos arreglos ('my_house' y 'your_house'):")
print(result2)  # Resultado booleano para cada elemento

# Explicación de los resultados:
# - `result1` muestra un arreglo booleano donde True indica que el área cumple la condición.
# - `result2` muestra un arreglo booleano donde True indica que el área en ambos arreglos cumple la condición.