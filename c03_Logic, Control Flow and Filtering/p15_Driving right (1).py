# Ejercicio
# Filtrar un DataFrame en Pandas con base en una columna booleana

# Descripción:
# Este ejercicio utiliza un DataFrame llamado `cars` que contiene información
# sobre la densidad de automóviles y si las personas conducen por la derecha.
# Vamos a extraer las observaciones donde `drives_right` es True.

# Código en Python

# Importar pandas
import pandas as pd

# Cargar el dataset desde un archivo CSV
# (Nota: el archivo 'cars.csv' debe estar en el mismo directorio que este script)
cars = pd.read_csv('cars.csv', index_col=0)

# Paso 1: Extraer la columna `drives_right` como una Serie
dr = cars["drives_right"]  # Extraer la columna como Pandas Series

# Paso 2: Usar la Serie `dr` para filtrar el DataFrame
sel = cars[dr]  # Filtrar el DataFrame donde `drives_right` es True

# Paso 3: Imprimir el resultado
print("Filtrar observaciones donde `drives_right` es True:")
print(sel)

# Explicación:
# - Paso 1: La columna `drives_right` se extrae como una Serie booleana (`dr`).
# - Paso 2: Se utiliza esta Serie para indexar el DataFrame, seleccionando las filas
#   donde el valor de `drives_right` es True.
# - Paso 3: El DataFrame resultante (`sel`) contiene solo las observaciones
#   que cumplen la condición.

# Nota adicional:
# Este enfoque es útil para filtrar observaciones en base a una condición booleana específica.