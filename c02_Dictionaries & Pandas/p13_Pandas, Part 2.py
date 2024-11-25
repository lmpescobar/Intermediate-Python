# Pandas, Parte 2: Acceso e indexación de datos en DataFrames

# Descripción:
# En el video anterior, creamos un DataFrame llamado `brics` con datos básicos de los países BRICS.
# El código asigna etiquetas adecuadas a las filas y columnas, lo que facilita el acceso a columnas,
# filas y elementos individuales dentro del DataFrame.

# A continuación, se explicarán diferentes formas de indexar y seleccionar datos en un DataFrame,
# utilizando corchetes, y métodos avanzados como `loc` y `iloc`.

# Importar pandas y crear el DataFrame `brics`
import pandas as pd

# Crear el DataFrame desde un diccionario
data = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}
brics = pd.DataFrame(data, index=["BR", "RU", "IN", "CH", "SA"])

# Mostrar el DataFrame inicial
print("DataFrame BRICS:")
print(brics)

# 1. Acceso a columnas con corchetes simples
# Acceso a la columna "country" como un Pandas Series
print("\nColumna 'country' como Series:")
print(brics["country"])
print("Tipo:", type(brics["country"]))  # pandas.core.series.Series

# Acceso a la columna "country" como un DataFrame (dobles corchetes)
print("\nColumna 'country' como DataFrame:")
print(brics[["country"]])
print("Tipo:", type(brics[["country"]]))  # pandas.core.frame.DataFrame

# Acceso a múltiples columnas: "country" y "capital"
print("\nSub-DataFrame con columnas 'country' y 'capital':")
print(brics[["country", "capital"]])

# 2. Acceso a filas con slicing (corchetes simples)
# Seleccionar las filas 1 a 3 (índices 1, 2, 3; el extremo superior es exclusivo)
print("\nFilas 1 a 3 con slicing:")
print(brics[1:4])

# 3. Acceso con `loc` (basado en etiquetas)
# Acceso a la fila de Rusia ("RU") como Series
print("\nFila para Rusia ('RU') como Series con loc:")
print(brics.loc["RU"])

# Acceso a la fila de Rusia como DataFrame (dobles corchetes)
print("\nFila para Rusia ('RU') como DataFrame con loc:")
print(brics.loc[["RU"]])

# Acceso a múltiples filas: Rusia, India y China
print("\nFilas para Rusia, India y China con loc:")
print(brics.loc[["RU", "IN", "CH"]])

# Acceso a filas y columnas específicas con loc
print("\nFilas para Rusia, India y China, columnas 'country' y 'capital':")
print(brics.loc[["RU", "IN", "CH"], ["country", "capital"]])

# Acceso a todas las filas pero solo columnas específicas
print("\nTodas las filas, columnas 'country' y 'capital':")
print(brics.loc[:, ["country", "capital"]])

# 4. Acceso con `iloc` (basado en posiciones)
# Acceso a la fila 1 (segunda fila, posición 0 basada en índice)
print("\nFila para Rusia (posición 1) con iloc:")
print(brics.iloc[1])

# Acceso a filas por posición: 1 a 3
print("\nFilas para Rusia, India y China con iloc:")
print(brics.iloc[1:4])

# Acceso a filas y columnas específicas con iloc
print("\nFilas 1 a 3, columnas 0 y 1 con iloc:")
print(brics.iloc[1:4, [0, 1]])

# Acceso a todas las filas, pero solo columnas 0 y 1
print("\nTodas las filas, columnas 0 y 1 con iloc:")
print(brics.iloc[:, [0, 1]])

# Resumen:
# - Corchetes simples (`[]`) funcionan para seleccionar columnas (Series) o filas (slicing).
# - `loc`: Selección basada en etiquetas para filas, columnas o ambas.
# - `iloc`: Selección basada en posiciones (índices) para filas, columnas o ambas.
# - `loc` y `iloc` ofrecen más versatilidad y control que los corchetes simples.

# ¡A practicar! 😊