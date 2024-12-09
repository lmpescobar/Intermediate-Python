# Ejercicio
# Iterar sobre un DataFrame de pandas y formatear la salida

# Descripción:
# Este ejercicio utiliza el método `iterrows()` para recorrer un DataFrame
# y extraer valores específicos de las filas, formateando la salida según lo indicado.

# Código en Python

# Importar el paquete pandas
import pandas as pd

# Cargar los datos del archivo CSV en un DataFrame
cars = pd.read_csv('cars.csv', index_col=0)

# Bucle `for` para iterar sobre las filas del DataFrame
print("Datos de los países:")
for lab, row in cars.iterrows():
    # Construir la salida formateada
    country_info = f"{lab}: {row['cars_per_cap']}"
    print(country_info)

# Explicación:
# 1. **Carga del DataFrame:**
#    - Se utiliza `pd.read_csv()` para cargar el archivo `cars.csv` como un DataFrame.
#    - El parámetro `index_col=0` establece la primera columna como índice (etiqueta de las filas).
# 2. **Iteración con `iterrows()`:**
#    - `iterrows()` devuelve pares (label, row) en cada iteración.
#    - `lab` almacena la etiqueta de la fila (índice).
#    - `row` almacena los datos de la fila como una Serie de pandas.
# 3. **Extracción y formato:**
#    - Se accede al valor de la columna `cars_per_cap` en cada fila con `row['cars_per_cap']`.
#    - Se construye una cadena formateada con f-strings para mostrar la etiqueta del país y el número de autos por persona.

# Resultado esperado:
# Al ejecutar este código, para cada fila en el DataFrame, se imprimirá:
# US: 809
# AUS: 731
# JPN: 588
# IND: 18
# BRA: 42
# RUS: 200
# CHN: 70

# Nota:
# - Este ejercicio muestra cómo acceder a valores específicos en cada fila usando subsetting.
# - El uso de f-strings (`f"{lab}: {row['cars_per_cap']}"`) facilita la creación de cadenas formateadas.