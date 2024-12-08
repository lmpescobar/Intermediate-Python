# Ejercicio
# Selección de países con más de 500 carros per cápita en un DataFrame

# Descripción:
# Vamos a usar un DataFrame llamado `cars` para identificar los países
# que tienen un valor de `cars_per_cap` mayor a 500. Luego, filtraremos
# el DataFrame para incluir solo esos países.

# Código en Python

# Importar pandas
import pandas as pd

# Cargar el dataset desde un archivo CSV
cars = pd.read_csv('cars.csv', index_col=0)

# Paso 1: Seleccionar la columna `cars_per_cap` como una Serie
cpc = cars["cars_per_cap"]  # Columna de carros per cápita

# Paso 2: Crear una Serie booleana donde `cars_per_cap > 500`
many_cars = cpc > 500  # True si el país tiene más de 500 carros per cápita

# Paso 3: Filtrar el DataFrame usando la Serie booleana
car_maniac = cars[many_cars]  # Filtrar países con `cars_per_cap > 500`

# Paso 4: Imprimir el resultado
print("Países con más de 500 carros per cápita:")
print(car_maniac)

# Explicación:
# - Paso 1: La columna `cars_per_cap` se extrae como una Serie.
# - Paso 2: Comparamos los valores en esta columna con 500, generando
#   una Serie booleana.
# - Paso 3: Usamos esta Serie para indexar el DataFrame, seleccionando
#   solo las filas que cumplen con la condición.
# - Paso 4: Mostramos el DataFrame filtrado.