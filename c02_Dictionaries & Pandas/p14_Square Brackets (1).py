# Square Brackets (1)

# Descripción:
# En el video, aprendimos que puedes indexar y seleccionar datos en un DataFrame de Pandas de diferentes maneras.
# La forma más simple, aunque no la más poderosa, es usar corchetes (`[]`).
# En este ejercicio, usaremos corchetes para acceder a columnas de un DataFrame.

# Notas importantes:
# - Usar un solo par de corchetes (`[]`) devuelve una Serie de Pandas.
# - Usar un doble par de corchetes (`[[]]`) devuelve un DataFrame de Pandas.

# Instrucciones:
# 1. Usa corchetes simples para imprimir la columna `country` como una Pandas Series.
# 2. Usa doble par de corchetes para imprimir la columna `country` como un DataFrame.
# 3. Usa doble par de corchetes para imprimir un DataFrame con las columnas `country` y `drives_right`.

# Paso 1: Importar pandas y los datos desde un archivo CSV
import pandas as pd

# Cargar el archivo CSV con index_col=0 para usar la primera columna como etiquetas de las filas
cars = pd.read_csv('cars.csv', index_col=0)

# Paso 2: Imprimir la columna `country` como una Pandas Series
print("Columna 'country' como Pandas Series:")
print(cars['country'])  # Usar corchetes simples

# Paso 3: Imprimir la columna `country` como un DataFrame
print("\nColumna 'country' como Pandas DataFrame:")
print(cars[['country']])  # Usar doble par de corchetes

# Paso 4: Imprimir un DataFrame con las columnas `country` y `drives_right`
print("\nSub-DataFrame con columnas 'country' y 'drives_right':")
print(cars[['country', 'drives_right']])  # Usar doble par de corchetes para múltiples columnas

# Resultado esperado:
# Columna 'country' como Pandas Series:
# US       United States
# AUS          Australia
# JPN              Japan
# IN               India
# RU              Russia
# MOR            Morocco
# EG               Egypt
# Name: country, dtype: object
#
# Columna 'country' como Pandas DataFrame:
#           country
# US  United States
# AUS     Australia
# JPN         Japan
# IN          India
# RU         Russia
# MOR       Morocco
# EG          Egypt
#
# Sub-DataFrame con columnas 'country' y 'drives_right':
#           country  drives_right
# US  United States          True
# AUS     Australia         False
# JPN         Japan         False
# IN          India         False
# RU         Russia          True
# MOR       Morocco          True
# EG          Egypt          True