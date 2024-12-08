# Ejercicio
# Optimizar el código para filtrar un DataFrame en una sola línea

# Descripción:
# Este ejercicio elimina la variable intermedia `dr` utilizada anteriormente
# y coloca directamente la condición booleana dentro de los corchetes para filtrar el DataFrame.

# Código en Python
import pandas as pd

# Cargar el dataset desde un archivo CSV
cars = pd.read_csv('C:/Intermediate Python/c03_Logic, Control Flow and Filtering/cars2.csv', index_col=0)

# Filtrar directamente donde `drives_right` es True (código optimizado en una línea)
sel = cars[cars['drives_right']]

# Imprimir el resultado
print(sel)

# Explicación:
# - En lugar de crear una variable intermedia (`dr`), la condición `cars['drives_right']`
#   se coloca directamente en los corchetes para filtrar las filas del DataFrame.
# - Esto hace el código más conciso y directo.