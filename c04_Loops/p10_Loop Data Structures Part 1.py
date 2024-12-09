# Ejercicio
# Iterar sobre diccionarios y arreglos de NumPy

# Descripción:
# Este ejercicio explora cómo iterar sobre dos tipos de estructuras de datos:
# - Diccionarios: Accediendo a claves y valores.
# - Arreglos NumPy: Iterando sobre elementos en 1D y 2D usando `np.nditer()`.

# Código en Python

# Parte 1: Iterar sobre un diccionario
print("Iteración sobre un diccionario:")
world = {
    "afghanistan": 30.55,
    "albania": 2.77,
    "algeria": 39.21
}

# Usar `.items()` para obtener clave y valor
for country, population in world.items():
    print(f"{country} -- {population} millones")

# Parte 2: Iterar sobre un arreglo NumPy 1D
print("\nIteración sobre un arreglo NumPy 1D:")
import numpy as np

bmi = np.array([21.852, 20.975, 21.750, 24.747, 21.441])
for val in bmi:
    print(val)

# Parte 3: Iterar sobre un arreglo NumPy 2D
print("\nIteración sobre un arreglo NumPy 2D:")
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
meas = np.array([np_height, np_weight])

# Usar `np.nditer()` para recorrer todos los elementos
for val in np.nditer(meas):
    print(val)

# Explicación:
# 1. **Diccionario:**
#    - `.items()` genera pares clave-valor para iterar fácilmente.
#    - `country` y `population` almacenan la clave y el valor respectivamente en cada iteración.
# 2. **Arreglo NumPy 1D:**
#    - Un bucle `for` básico itera sobre cada valor del arreglo.
# 3. **Arreglo NumPy 2D:**
#    - `np.nditer()` permite recorrer cada elemento de un arreglo multidimensional.
#    - Sin esto, el bucle iteraría sobre las filas como arreglos completos.

# Resultado esperado:
# - Parte 1: 
#   afghanistan -- 30.55 millones
#   albania -- 2.77 millones
#   algeria -- 39.21 millones
#
# - Parte 2:
#   21.852
#   20.975
#   21.750
#   24.747
#   21.441
#
# - Parte 3:
#   1.73
#   1.68
#   1.71
#   1.89
#   1.79
#   65.4
#   59.2
#   63.6
#   88.4
#   68.7

# Nota:
# - Los diccionarios no mantienen un orden fijo en sus claves (Python < 3.7).
# - `np.nditer()` es esencial para recorrer cada elemento en un arreglo multidimensional.