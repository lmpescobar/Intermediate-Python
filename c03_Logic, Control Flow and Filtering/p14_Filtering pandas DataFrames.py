# Ejercicio
# Filtrar DataFrames en Pandas

# Descripción:
# En este ejercicio trabajaremos con un DataFrame que contiene información
# sobre países y sus áreas. Vamos a filtrar las filas del DataFrame basándonos
# en ciertas condiciones de la columna `area` usando operadores booleanos.

# Código en Python

# Importar las bibliotecas necesarias
import pandas as pd
import numpy as np

# Crear el DataFrame brics
data = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.1, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252.0, 1357.0, 52.98]
}
brics = pd.DataFrame(data, index=["BR", "RU", "IN", "CH", "SA"])

# Paso 1: Seleccionar la columna `area`
area_column = brics["area"]  # Obtiene la columna como una Serie de Pandas

# Paso 2: Comparar para obtener países con área mayor a 8
is_huge = area_column > 8  # Serie booleana que indica las filas que cumplen la condición

# Paso 3: Filtrar el DataFrame usando la Serie booleana
huge_countries = brics[is_huge]  # Filtrar solo los países con área > 8

# Imprimir el resultado del filtro
print("Países con área mayor a 8 millones de km²:")
print(huge_countries)

# Paso adicional: Usar operadores booleanos para filtrar con múltiples condiciones
# Obtener países con área entre 8 y 10 millones de km²
medium_countries = brics[np.logical_and(brics["area"] > 8, brics["area"] < 10)]

# Imprimir el resultado del filtro
print("\nPaíses con área entre 8 y 10 millones de km²:")
print(medium_countries)

# Explicación:
# - Paso 1: Extraemos la columna `area` del DataFrame, lo cual nos da una Serie.
# - Paso 2: Comparamos la columna `area` con el valor 8 para identificar áreas mayores.
# - Paso 3: Usamos la Serie booleana resultante para filtrar el DataFrame.
# - Adicional: Aplicamos `np.logical_and` para combinar condiciones booleanas,
#   filtrando áreas entre 8 y 10 millones de km².