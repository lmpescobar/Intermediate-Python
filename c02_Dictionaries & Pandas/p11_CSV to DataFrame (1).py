# CSV to DataFrame (1)

# Descripción:
# Poner datos en un diccionario y luego construir un DataFrame funciona, pero no es muy eficiente.
# ¿Qué pasa si estás trabajando con millones de observaciones? En esos casos, los datos suelen estar disponibles 
# como archivos regulares con una estructura bien definida. Uno de esos tipos de archivos es el CSV (Comma-Separated Values).
#
# Para importar archivos CSV a Python como un DataFrame de Pandas, puedes usar la función `read_csv()`.
#
# En este ejercicio, exploraremos esta función usando el mismo conjunto de datos de vehículos (cars) 
# de ejercicios anteriores. Esta vez, sin embargo, los datos están disponibles en un archivo CSV llamado `cars.csv`.

# Instrucciones:
# 1. Importa el paquete `pandas` como `pd`.
# 2. Usa `pd.read_csv()` para importar los datos de `cars.csv` y almacénalos en un DataFrame llamado `cars`.
# 3. Imprime el DataFrame `cars`. ¿Todo se ve correctamente?

# Paso 1: Importar pandas como pd
import pandas as pd

# Paso 2: Importar los datos del archivo cars.csv como un DataFrame
# Asegúrate de que el archivo `cars.csv` esté en tu directorio de trabajo actual.
cars = pd.read_csv("cars.csv")

# Paso 3: Imprimir el DataFrame para verificar los datos
print("Contenido del DataFrame cars:")
print(cars)

# Resultado esperado (formato del archivo cars.csv):
#          country  drives_right  cars_per_cap
# 0  United States          True          809
# 1      Australia         False          731
# 2          Japan         False          588
# 3          India         False           18
# 4         Russia          True          200
# 5        Morocco          True           70
# 6          Egypt          True           45