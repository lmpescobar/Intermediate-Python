# CSV to DataFrame (2)

# Descripción:
# En el ejercicio anterior, importamos datos desde un archivo CSV. Sin embargo, las etiquetas de las filas 
# se importaron como otra columna sin nombre. Para solucionar esto, podemos usar el argumento `index_col` 
# en la función `read_csv()` para especificar qué columna debe usarse como etiquetas de las filas.

# Instrucciones:
# 1. Ejecuta el código para ver cómo la primera columna no se usa correctamente como etiquetas de las filas.
# 2. Especifica el argumento `index_col` en `pd.read_csv()` configurándolo en `0`, para que la primera columna
#    se utilice como etiquetas de las filas.
# 3. Imprime el DataFrame `cars` nuevamente para verificar si el problema se solucionó.

# Paso 1: Importar pandas como pd
import pandas as pd

# Paso 2: Importar los datos del archivo cars.csv, configurando index_col=0
# Esto asegura que la primera columna del archivo CSV se use como etiquetas de las filas.
cars = pd.read_csv('cars.csv', index_col=0)

# Paso 3: Imprimir el DataFrame para verificar los datos
print("Contenido del DataFrame cars con las etiquetas de fila correctas:")
print(cars)

# Resultado esperado:
#                country  drives_right  cars_per_cap
# US      United States          True          809
# AUS         Australia         False          731
# JPN             Japan         False          588
# IN              India         False           18
# RU             Russia          True          200
# MOR           Morocco          True           70
# EG              Egypt          True           45