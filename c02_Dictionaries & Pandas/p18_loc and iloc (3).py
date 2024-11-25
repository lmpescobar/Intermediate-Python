# loc and iloc (3)

# Descripción:
# Es posible seleccionar solo columnas usando `loc` e `iloc`.
# En ambos casos, puedes usar un slice (rebanado) que vaya desde el principio hasta el final antes de la coma.

# Instrucciones:
# 1. Imprime la columna `drives_right` como una Serie usando `loc` o `iloc`.
# 2. Imprime la columna `drives_right` como un DataFrame usando `loc` o `iloc`.
# 3. Imprime tanto la columna `cars_per_cap` como la columna `drives_right` como un DataFrame usando `loc` o `iloc`.

# Paso 1: Importar pandas y cargar los datos
import pandas as pd

# Cargar los datos desde un archivo CSV
cars = pd.read_csv('cars.csv', index_col=0)

# Paso 2: Imprimir la columna `drives_right` como una Serie
# Usando loc
print("Columna 'drives_right' como Serie (usando loc):")
print(cars.loc[:, 'drives_right'])

# Usando iloc
print("\nColumna 'drives_right' como Serie (usando iloc):")
print(cars.iloc[:, 1])

# Paso 3: Imprimir la columna `drives_right` como un DataFrame
# Usando loc
print("\nColumna 'drives_right' como DataFrame (usando loc):")
print(cars.loc[:, ['drives_right']])

# Usando iloc
print("\nColumna 'drives_right' como DataFrame (usando iloc):")
print(cars.iloc[:, [1]])

# Paso 4: Imprimir las columnas `cars_per_cap` y `drives_right` como un DataFrame
# Usando loc
print("\nColumnas 'cars_per_cap' y 'drives_right' como DataFrame (usando loc):")
print(cars.loc[:, ['cars_per_cap', 'drives_right']])

# Usando iloc
print("\nColumnas 'cars_per_cap' y 'drives_right' como DataFrame (usando iloc):")
print(cars.iloc[:, [2, 1]])

# Resultado esperado:
# Columna 'drives_right' como Serie:
# US      True
# AUS    False
# JPN    False
# IN     False
# RU      True
# MOR     True
# EG      True
# Name: drives_right, dtype: bool
#
# Columna 'drives_right' como DataFrame:
#       drives_right
# US            True
# AUS          False
# JPN          False
# IN           False
# RU            True
# MOR           True
# EG            True
#
# Columnas 'cars_per_cap' y 'drives_right' como DataFrame:
#       cars_per_cap  drives_right
# US            809          True
# AUS           731         False
# JPN           588         False
# IN             18         False
# RU            200          True
# MOR            70          True
# EG             45          True