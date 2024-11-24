# ### Transcripción y explicación detallada del video y los textos relacionados con Pandas, Parte 1

# Introducción a Pandas

# Pandas es una herramienta poderosa para manejar y analizar datos tabulares.
# Como científico de datos, trabajarás con grandes volúmenes de datos que suelen tener
# una estructura tabular (similar a una hoja de cálculo). Pandas facilita la manipulación de este tipo de datos.

# Ejemplos de datos tabulares:
# - **Datos de mediciones**: En una planta química, cada fila puede representar una observación o medición, y cada columna una variable como temperatura, fecha o ubicación.
# - **Datos de países BRICS**: Una tabla que contiene:
#   - Nombre del país.
#   - Capital.
#   - Área en millones de kilómetros cuadrados.
#   - Población en millones.

# Aunque las matrices 2D de NumPy pueden manejar datos tabulares, no son ideales para manejar múltiples tipos de datos.
# Por ejemplo, en el caso de BRICS:
# - `Área` y `Población` son de tipo float.
# - `País` y `Capital` son de tipo string.
# Para trabajar con diferentes tipos de datos, usamos **Pandas**, una herramienta de alto nivel basada en NumPy.

# Objetos principales de Pandas: DataFrame
# El `DataFrame` de Pandas almacena datos tabulares:
# - Las filas representan observaciones.
# - Las columnas representan variables.
# - Cada fila tiene una etiqueta única.
# - Cada columna tiene un nombre (etiqueta).

# Ejemplo visual del DataFrame BRICS:
#          country    capital    area  population
# BR        Brazil   Brasilia   8.516      200.40
# RU        Russia     Moscow  17.100      143.50
# IN         India  New Delhi   3.286     1252.00
# CH         China    Beijing   9.597     1357.00
# SA  South Africa   Pretoria   1.221       52.98

# --- Cómo crear un DataFrame en Pandas ---

# Importar pandas
import pandas as pd

# 1. Crear un DataFrame desde un diccionario
# Creamos un diccionario con los datos. Cada clave será el nombre de una columna, y los valores serán los datos.
data = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}

# Convertir el diccionario en un DataFrame
brics = pd.DataFrame(data)

# Ver el DataFrame
print("DataFrame inicial:")
print(brics)

# 2. Asignar etiquetas a las filas
# Por defecto, las filas tienen índices automáticos (0, 1, 2, etc.). Podemos asignar etiquetas personalizadas.
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Ver el DataFrame actualizado
print("\nDataFrame con etiquetas de fila personalizadas:")
print(brics)

# 3. Importar un DataFrame desde un archivo CSV
# Si trabajamos con grandes volúmenes de datos, es mejor importarlos desde archivos externos.

# Supongamos que el archivo brics.csv tiene el siguiente contenido:
# ,country,capital,area,population
# BR,Brazil,Brasilia,8.516,200.4
# RU,Russia,Moscow,17.10,143.5
# IN,India,New Delhi,3.286,1252
# CH,China,Beijing,9.597,1357
# SA,South Africa,Pretoria,1.221,52.98

# Guardamos este archivo como ejemplo
brics.to_csv("brics.csv")

# Importar datos desde un archivo CSV
# Aquí usamos index_col=0 para especificar que la primera columna será utilizada como índice.
brics_from_csv = pd.read_csv("brics.csv", index_col=0)

# Ver el DataFrame cargado desde el archivo CSV
print("\nDataFrame cargado desde el archivo CSV:")
print(brics_from_csv)

# Conclusión
# - Los DataFrames pueden crearse manualmente o cargarse desde archivos externos como CSV.
# - Pandas permite trabajar con datos tabulares de manera flexible, eficiente y escalable.