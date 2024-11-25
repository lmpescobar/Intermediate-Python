# Square Brackets (2)

# Descripción:
# Los corchetes no solo se utilizan para seleccionar columnas, también se pueden usar
# para obtener filas u observaciones de un DataFrame.
# En este ejercicio, usaremos slicing (rebanado) para seleccionar subconjuntos de filas del DataFrame `cars`.

# Nota importante:
# - Solo puedes seleccionar filas utilizando slicing si especificas un rango (slice) como `0:3`.
# - Aquí usamos los índices enteros de las filas, no las etiquetas de las filas.

# Instrucciones:
# 1. Selecciona las primeras 3 observaciones de `cars` y imprímelas.
# 2. Selecciona la cuarta, quinta y sexta observación, correspondientes a los índices 3, 4 y 5, y imprímelas.

# Paso 1: Importar pandas y cargar los datos
import pandas as pd

# Cargar los datos desde un archivo CSV (asegúrate de que cars.csv esté en el mismo directorio)
cars = pd.read_csv('cars.csv', index_col=0)

# Paso 2: Seleccionar las primeras 3 observaciones
print("Primeras 3 observaciones:")
print(cars[0:3])  # Seleccionar filas con slicing (índices 0, 1 y 2)

# Paso 3: Seleccionar la cuarta, quinta y sexta observación
print("\nCuarta, quinta y sexta observación:")
print(cars[3:6])  # Seleccionar filas con slicing (índices 3, 4 y 5)

# Resultado esperado:
# Primeras 3 observaciones:
#           country  drives_right  cars_per_cap
# US  United States          True          809
# AUS     Australia         False          731
# JPN         Japan         False          588
#
# Cuarta, quinta y sexta observación:
#           country  drives_right  cars_per_cap
# IN          India         False           18
# RU         Russia          True          200
# MOR       Morocco          True           70