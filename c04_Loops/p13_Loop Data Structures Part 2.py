# Ejercicio
# Iterar sobre DataFrames de pandas usando `iterrows()` y `apply()`

# Descripción:
# Este ejercicio explora cómo recorrer un DataFrame de pandas con `iterrows()`
# y cómo realizar operaciones más eficientes utilizando el método `apply()`.

# Código en Python

# Importar el paquete pandas
import pandas as pd

# Crear el DataFrame `brics`
data = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.1, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252.0, 1357.0, 52.98]
}
brics = pd.DataFrame(data, index=["BR", "RU", "IN", "CH", "SA"])

# Parte 1: Iterar sobre las filas del DataFrame usando `iterrows()`
print("Capitales de cada país:")
for lab, row in brics.iterrows():
    # Imprimir la etiqueta de la fila (lab) y la capital del país
    print(f"{lab}: {row['capital']}")

# Parte 2: Agregar una columna con la longitud del nombre del país usando `iterrows()`
for lab, row in brics.iterrows():
    brics.loc[lab, "name_length"] = len(row["country"])

# Mostrar el DataFrame actualizado
print("\nDataFrame con la columna `name_length` añadida:")
print(brics)

# Parte 3: Agregar la columna `name_length` de manera más eficiente con `apply()`
brics["name_length_efficient"] = brics["country"].apply(len)

# Mostrar el DataFrame actualizado con `apply()`
print("\nDataFrame con `name_length` calculado usando `apply()`:")
print(brics)

# Explicación:
# 1. **Parte 1:** 
#    - Se utiliza `iterrows()` para recorrer cada fila del DataFrame.
#    - `lab` contiene la etiqueta de la fila, y `row` contiene los datos de la fila como una Serie.
#    - Esto permite acceder a columnas específicas (por ejemplo, "capital") usando subsetting.
# 2. **Parte 2:**
#    - Se calcula la longitud del nombre del país (`len(row["country"])`) y se agrega como una nueva columna.
#    - `loc` se usa para asignar el valor calculado en la fila y columna apropiadas.
# 3. **Parte 3:**
#    - `apply()` realiza la misma operación pero de manera vectorizada, aplicando `len` a cada elemento
#      de la columna "country".
#    - Es más eficiente y adecuado para DataFrames grandes.

# Resultado esperado:
# - Parte 1: Impresión de las capitales por fila.
#   BR: Brasilia
#   RU: Moscow
#   IN: New Delhi
#   CH: Beijing
#   SA: Pretoria
#
# - Parte 2: DataFrame actualizado con la columna `name_length`:
#         country    capital    area  population  name_length
#   BR    Brazil    Brasilia   8.516      200.40          6
#   RU    Russia    Moscow    17.100      143.50          6
#   IN    India     New Delhi  3.286     1252.00          5
#   CH    China     Beijing    9.597     1357.00          5
#   SA    South Africa Pretoria 1.221      52.98         12
#
# - Parte 3: DataFrame con una columna adicional calculada eficientemente.

# Nota:
# - Usar `iterrows()` es útil para operaciones basadas en filas pequeñas.
# - `apply()` es preferible para operaciones más grandes debido a su eficiencia.