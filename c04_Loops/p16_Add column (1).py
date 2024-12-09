# Ejercicio
# Agregar una columna al DataFrame utilizando un bucle `for`

# Descripción:
# Este ejercicio utiliza un bucle `for` y el método `loc` de pandas para añadir
# una nueva columna al DataFrame `cars`. La nueva columna contiene los nombres
# de los países en mayúsculas.

# Código en Python

# Importar el paquete pandas
import pandas as pd

# Cargar los datos del archivo CSV en un DataFrame
cars = pd.read_csv('cars.csv', index_col=0)

# Bucle `for` para agregar la columna `COUNTRY`
for lab, row in cars.iterrows():
    # Asignar la versión en mayúsculas de la columna `country` a la nueva columna `COUNTRY`
    cars.loc[lab, "COUNTRY"] = row["country"].upper()

# Imprimir el DataFrame actualizado
print(cars)

# Explicación:
# 1. **Carga del DataFrame:**
#    - Se utiliza `pd.read_csv()` para cargar el archivo `cars.csv` como un DataFrame.
#    - El parámetro `index_col=0` establece la primera columna como índice (etiqueta de las filas).
# 2. **Uso del bucle `for`:**
#    - `iterrows()` devuelve pares (label, row) en cada iteración.
#    - `lab` almacena la etiqueta de la fila (índice).
#    - `row` almacena los datos de la fila como una Serie de pandas.
# 3. **Creación de la columna `COUNTRY`:**
#    - Se accede al valor de la columna `country` en cada fila con `row["country"]`.
#    - Se convierte a mayúsculas usando el método `.upper()`.
#    - `loc` se usa para asignar este valor a la nueva columna `COUNTRY`.

# Resultado esperado:
# Al ejecutar este código, el DataFrame tendrá una nueva columna `COUNTRY` con los nombres de los países en mayúsculas.

# Nota:
# - Este enfoque funciona bien para DataFrames pequeños.
# - Para conjuntos de datos más grandes, considera usar el método `apply()` de pandas para operaciones vectorizadas.