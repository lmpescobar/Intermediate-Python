# loc and iloc (2)

# Descripción:
# Las funciones `loc` e `iloc` permiten seleccionar tanto filas como columnas de un DataFrame.
# - `loc`: Basado en etiquetas para filas y columnas.
# - `iloc`: Basado en índices enteros para filas y columnas.

# Instrucciones:
# 1. Imprime el valor de la columna `drives_right` de la fila correspondiente a Marruecos (etiqueta: "MOR").
# 2. Imprime un sub-DataFrame que contenga las observaciones de Rusia y Marruecos, 
#    y las columnas `country` y `drives_right`.

# Paso 1: Importar pandas y cargar los datos
import pandas as pd

# Cargar los datos desde un archivo CSV
cars = pd.read_csv('cars.csv', index_col=0)

# Paso 2: Imprimir el valor de la columna `drives_right` de Marruecos
# Usando `loc`
print("Valor de 'drives_right' para Marruecos (usando loc):")
print(cars.loc['MOR', 'drives_right'])

# Usando `iloc`
print("\nValor de 'drives_right' para Marruecos (usando iloc):")
print(cars.iloc[5, 1])

# Paso 3: Imprimir un sub-DataFrame con las observaciones de Rusia y Marruecos
# y las columnas `country` y `drives_right`
# Usando `loc`
print("\nSub-DataFrame para Rusia y Marruecos, columnas 'country' y 'drives_right' (usando loc):")
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

# Usando `iloc`
print("\nSub-DataFrame para Rusia y Marruecos, columnas 'country' y 'drives_right' (usando iloc):")
print(cars.iloc[[4, 5], [0, 1]])

# Resultado esperado:
# Valor de 'drives_right' para Marruecos:
# True
#
# Sub-DataFrame para Rusia y Marruecos:
#       country  drives_right
# RU     Russia          True
# MOR   Morocco          True