# Ejercicio
# Filtrar observaciones con valores entre 100 y 500 en una columna de un DataFrame

# Descripción:
# Este ejercicio utiliza operadores booleanos avanzados (`np.logical_and`) para
# seleccionar un rango de valores en la columna `cars_per_cap` de un DataFrame.

# Código en Python

# Importar las bibliotecas necesarias
import pandas as pd
import numpy as np

# Cargar el dataset desde un archivo CSV
cars = pd.read_csv('cars.csv', index_col=0)

# Paso 1: Seleccionar la columna `cars_per_cap`
cpc = cars["cars_per_cap"]  # Extraer la columna `cars_per_cap`

# Paso 2: Usar `np.logical_and` para obtener los valores entre 100 y 500
between = np.logical_and(cpc > 100, cpc < 500)  # Serie booleana

# Paso 3: Filtrar el DataFrame usando la Serie booleana
medium = cars[between]  # Filtrar las observaciones que cumplen la condición

# Paso 4: Imprimir el resultado
print("Países con valores de `cars_per_cap` entre 100 y 500:")
print(medium)

# Explicación:
# - Paso 1: Extraemos la columna `cars_per_cap` como una Serie.
# - Paso 2: Aplicamos `np.logical_and` para combinar dos condiciones: `cpc > 100` y `cpc < 500`.
#   Esto genera una Serie booleana con `True` donde se cumplen ambas condiciones.
# - Paso 3: Usamos esta Serie booleana para filtrar el DataFrame, seleccionando solo las filas
#   donde `cars_per_cap` está en el rango deseado.
# - Paso 4: Mostramos el DataFrame resultante.