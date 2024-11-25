# Dictionary to DataFrame (2)

# Descripción:
# El código Python que resuelve el ejercicio anterior ya está incluido en el script.
# Observa que las etiquetas de las filas (es decir, las etiquetas para las diferentes observaciones) 
# se configuran automáticamente como enteros del 0 al 6.
#
# Para resolver esto, se ha creado una lista `row_labels`. Puedes usar esta lista para especificar
# las etiquetas de las filas del DataFrame `cars`. Esto se hace configurando el atributo `index` 
# de `cars`, que puedes acceder como `cars.index`.

# Instrucciones:
# 1. Ejecuta el código para ver que, en efecto, las etiquetas de las filas no están configuradas correctamente.
# 2. Especifica las etiquetas de las filas configurando `cars.index` igual a `row_labels`.
# 3. Imprime `cars` nuevamente para verificar si las etiquetas de las filas son correctas esta vez.

# Importar pandas
import pandas as pd

# Construcción del DataFrame cars
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}
cars = pd.DataFrame(cars_dict)

# Imprimir el DataFrame inicial
print("DataFrame inicial con índices automáticos:")
print(cars)

# Definición de row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Configurar las etiquetas de las filas usando row_labels
cars.index = row_labels

# Imprimir el DataFrame actualizado
print("\nDataFrame con etiquetas de fila personalizadas:")
print(cars)

# Resultado esperado:
# DataFrame inicial con índices automáticos:
#          country  drives_right  cars_per_cap
# 0  United States          True          809
# 1      Australia         False          731
# 2          Japan         False          588
# 3          India         False           18
# 4         Russia          True          200
# 5        Morocco          True           70
# 6          Egypt          True           45

# DataFrame con etiquetas de fila personalizadas:
#          country  drives_right  cars_per_cap
# US  United States          True          809
# AUS     Australia         False          731
# JPN         Japan         False          588
# IN          India         False           18
# RU         Russia          True          200
# MOR       Morocco          True           70
# EG          Egypt          True           45