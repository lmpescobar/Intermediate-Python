# Ejercicio
# Iterar sobre un DataFrame de pandas usando `iterrows()`

# Descripción:
# Este ejercicio utiliza el método `iterrows()` para recorrer fila por fila un DataFrame.
# Se imprime la etiqueta de cada fila (row label) y el contenido completo de la fila.

# Código en Python

# Importar el paquete pandas
import pandas as pd

# Cargar los datos del archivo CSV en un DataFrame
cars = pd.read_csv('cars.csv', index_col=0)

# Bucle `for` para iterar sobre las filas del DataFrame
print("Contenido del DataFrame:")
for lab, row in cars.iterrows():
    # Imprimir la etiqueta de la fila
    print(f"Etiqueta de fila: {lab}")
    # Imprimir el contenido completo de la fila
    print(row)

# Explicación:
# 1. **Carga del DataFrame:**
#    - Se utiliza `pd.read_csv()` para cargar el archivo `cars.csv` como un DataFrame.
#    - El parámetro `index_col=0` indica que la primera columna del CSV debe usarse como índice.
# 2. **Iteración con `iterrows()`:**
#    - `iterrows()` devuelve pares (label, row) en cada iteración.
#    - `lab` almacena la etiqueta de la fila (índice).
#    - `row` almacena el contenido de la fila como una Serie de pandas.
# 3. **Impresión:**
#    - En cada iteración, se imprimen la etiqueta y el contenido de la fila.

# Resultado esperado:
# Al ejecutar este código, para cada fila en el DataFrame, se imprimirá:
# Etiqueta de fila: <nombre_de_la_etiqueta>
# <contenido_completo_de_la_fila>

# Nota:
# - Este método es útil para recorrer DataFrames pequeños. En DataFrames grandes, puede no ser eficiente.
# - Para operaciones complejas o grandes cantidades de datos, considera usar métodos vectorizados como `apply()` o funciones nativas de pandas.