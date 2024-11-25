# loc and iloc (1)

# Descripción:
# Con `loc` e `iloc` puedes realizar prácticamente cualquier operación de selección de datos en DataFrames.
# - `loc` es basado en etiquetas, lo que significa que debes especificar filas y columnas según sus etiquetas.
# - `iloc` es basado en índices enteros, lo que significa que debes especificar filas y columnas por su posición.

# Instrucciones:
# 1. Usa `loc` o `iloc` para seleccionar la observación correspondiente a Japón como una Serie.
#    - La etiqueta de esta fila es "JPN", el índice es 2.
# 2. Usa `loc` o `iloc` para seleccionar las observaciones de Australia y Egipto como un DataFrame.
#    - Inspecciona el DataFrame para encontrar las etiquetas o índices de estas filas.

# Paso 1: Importar pandas y cargar los datos
import pandas as pd

# Cargar los datos desde un archivo CSV
cars = pd.read_csv('cars.csv', index_col=0)

# Paso 2: Seleccionar la observación correspondiente a Japón como una Serie
# Usando `loc` (basado en etiquetas)
print("Observación para Japón (usando loc):")
print(cars.loc['JPN'])

# Usando `iloc` (basado en índices)
print("\nObservación para Japón (usando iloc):")
print(cars.iloc[2])

# Paso 3: Seleccionar las observaciones de Australia y Egipto como un DataFrame
# Usando `loc` (basado en etiquetas)
print("\nObservaciones para Australia y Egipto (usando loc):")
print(cars.loc[['AUS', 'EG']])

# Usando `iloc` (basado en índices)
print("\nObservaciones para Australia y Egipto (usando iloc):")
print(cars.iloc[[1, 6]])

# Resultado esperado:
# Observación para Japón (usando loc o iloc):
# country         Japan
# drives_right    False
# cars_per_cap      588
# Name: JPN, dtype: object
#
# Observaciones para Australia y Egipto (usando loc o iloc):
#           country  drives_right  cars_per_cap
# AUS     Australia         False          731
# EG          Egypt          True           45