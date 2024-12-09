# Ejercicio
# Iterar sobre arreglos de NumPy usando bucles `for`

# Descripción:
# Este ejercicio utiliza dos arreglos de NumPy:
# - `np_height`, un arreglo 1D que contiene las alturas de jugadores de béisbol.
# - `np_baseball`, un arreglo 2D con alturas (primera columna) y pesos (segunda columna).
# Se usan bucles `for` para iterar sobre ambos arreglos y mostrar su contenido.

# Código en Python

# Importar el paquete NumPy
import numpy as np

# Definición de los arreglos
np_height = np.array([74, 72, 71, 69, 68])  # Alturas en pulgadas
np_baseball = np.array([
    [74, 180],
    [72, 215],
    [71, 210],
    [69, 185],
    [68, 180]
])  # Alturas (1ª columna) y pesos (2ª columna)

# Parte 1: Iterar sobre el arreglo 1D `np_height`
print("Alturas de jugadores (en pulgadas):")
for height in np_height:
    print(f"{height} inches")  # Mostrar cada altura con la etiqueta "inches"

# Parte 2: Iterar sobre el arreglo 2D `np_baseball`
print("\nElementos del arreglo 2D `np_baseball`:")
for value in np.nditer(np_baseball):
    print(value)  # Mostrar cada elemento individual del arreglo 2D

# Explicación:
# 1. **Arreglo 1D (`np_height`):**
#    - Un bucle `for` básico itera sobre cada elemento del arreglo.
#    - Cada valor se imprime con el texto "inches" para denotar unidades de medida.
# 2. **Arreglo 2D (`np_baseball`):**
#    - `np.nditer()` permite iterar sobre cada elemento individual en un arreglo multidimensional.
#    - Esto es útil para recorrer cada valor en arreglos 2D o superiores.

# Resultado esperado:
# - Parte 1:
#   74 inches
#   72 inches
#   71 inches
#   69 inches
#   68 inches
#
# - Parte 2:
#   74
#   180
#   72
#   215
#   71
#   210
#   69
#   185
#   68
#   180

# Nota:
# - Iterar sobre arreglos 1D es directo, pero para arreglos 2D necesitas `np.nditer()` para acceder a cada valor individual.
# - `np.nditer()` es especialmente útil para manipular datos en arreglos de varias dimensiones.