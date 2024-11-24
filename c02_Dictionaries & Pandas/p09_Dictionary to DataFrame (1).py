# Dictionary to DataFrame (1)

# Descripción:
# Pandas es una librería de código abierto que proporciona herramientas de análisis y manipulación de datos de alto rendimiento, fáciles de usar para Python. ¡Prometedor!
# 
# El DataFrame es una de las estructuras de datos más importantes de Pandas. Básicamente, es una forma de almacenar datos tabulares donde puedes etiquetar las filas y las columnas.
# Una forma de construir un DataFrame es a partir de un diccionario.
#
# En este ejercicio, trabajarás con datos de vehículos de diferentes países. Cada observación corresponde a un país y las columnas proporcionan información sobre:
# - El número de vehículos por cada 1000 personas.
# - Si las personas conducen por la derecha o por la izquierda.
# 
# Tres listas están definidas en el script:
# - `names`: Contiene los nombres de los países para los cuales hay datos disponibles.
# - `dr`: Una lista de valores booleanos que indica si las personas conducen por la derecha o por la izquierda en el país correspondiente.
# - `cpc`: El número de vehículos de motor por cada 1000 personas en el país correspondiente.
#
# Cada clave del diccionario será una etiqueta de columna y cada valor será una lista que contiene los elementos de esa columna.

# Instrucciones:
# 1. Importar pandas como pd.
# 2. Usar las listas predefinidas para crear un diccionario llamado `my_dict`.
#    Este diccionario debe tener tres pares clave-valor:
#    - Clave: 'country', Valor: names.
#    - Clave: 'drives_right', Valor: dr.
#    - Clave: 'cars_per_cap', Valor: cpc.
# 3. Usar `pd.DataFrame()` para convertir tu diccionario en un DataFrame llamado `cars`.
# 4. Imprimir el DataFrame `cars` y admirar lo organizado que está.

# Listas predefinidas
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Paso 1: Importar pandas como pd
import pandas as pd

# Paso 2: Crear un diccionario a partir de las listas predefinidas
# Las claves del diccionario representan las columnas y los valores son las listas de datos.
my_dict = {
    "country": names,
    "drives_right": dr,
    "cars_per_cap": cpc
}

# Paso 3: Crear un DataFrame llamado `cars` a partir del diccionario
cars = pd.DataFrame(my_dict)

# Paso 4: Imprimir el DataFrame para verificar los resultados
print("DataFrame generado a partir del diccionario:")
print(cars)

# Resultado esperado:
#          country  drives_right  cars_per_cap
# 0  United States          True          809
# 1      Australia         False          731
# 2          Japan         False          588
# 3          India         False           18
# 4         Russia          True          200
# 5        Morocco          True           70
# 6          Egypt          True           45