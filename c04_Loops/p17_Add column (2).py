# Ejercicio
# Agregar una columna al DataFrame utilizando .apply()

# Descripción:
# Este ejercicio reemplaza el uso de `iterrows()` con el método `.apply()` para aplicar
# el método `str.upper` a todos los valores de una columna y crear una nueva columna.

# Código en Python

# Importar el paquete pandas
import pandas as pd

# Cargar los datos del archivo CSV en un DataFrame
cars = pd.read_csv('cars.csv', index_col=0)

# Usar .apply(str.upper) para crear la columna "COUNTRY"
cars["COUNTRY"] = cars["country"].apply(str.upper)

# Imprimir el DataFrame actualizado
print(cars)

# Explicación:
# 1. **Carga del DataFrame:**
#    - Se utiliza `pd.read_csv()` para cargar el archivo `cars.csv` como un DataFrame.
#    - El parámetro `index_col=0` establece la primera columna como índice (etiqueta de las filas).
# 2. **Uso de `.apply()`:**
#    - Se accede a la columna `"country"` del DataFrame.
#    - Se utiliza `.apply(str.upper)` para aplicar el método `str.upper` a cada valor de la columna.
#    - `str.upper` convierte cada string en mayúsculas.
#    - El resultado se asigna como una nueva columna `"COUNTRY"`.
# 3. **Impresión:**
#    - Se imprime el DataFrame actualizado con la nueva columna.

# Resultado esperado:
# Al ejecutar este código, el DataFrame tendrá una nueva columna `"COUNTRY"` con los nombres de los países en mayúsculas.

# Nota:
# - Usar `.apply()` es más eficiente que un bucle `for` con `iterrows()`, especialmente para DataFrames grandes.
# - `.apply()` aplica la función especificada (en este caso, `str.upper`) de manera vectorizada, mejorando la velocidad y eficiencia.