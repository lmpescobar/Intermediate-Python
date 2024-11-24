# Ejercicio: Motivación para el uso de diccionarios

# Descripción:
# Este ejercicio muestra cómo acceder a datos relacionados utilizando listas paralelas. Aquí tenemos una lista
# de países europeos (`countries`) y una lista de sus capitales (`capitals`). Utilizaremos el método `index()` 
# para encontrar el índice de un país específico y acceder a su capital correspondiente desde la lista de capitales.

# Objetivo:
# - Usar el método `index()` para encontrar la posición de 'germany' en la lista `countries`.
# - Usar este índice para acceder a la capital de Alemania desde la lista `capitals` y mostrarla.

# Código en Python:

# Definición de listas: países europeos y sus capitales.
countries = ['spain', 'france', 'germany', 'norway']  # Lista de países.
capitals = ['madrid', 'paris', 'berlin', 'oslo']      # Lista de capitales correspondientes.

# 1. Obtener el índice de 'germany' en la lista de países usando el método `index()`.
ind_ger = countries.index('germany')  # Encuentra la posición de 'germany'.

# 2. Usar el índice encontrado para acceder a la capital de Alemania en la lista `capitals`.
capital_ger = capitals[ind_ger]  # Accede al elemento correspondiente en `capitals`.

# 3. Mostrar la capital de Alemania.
print("La capital de Alemania es:", capital_ger)

# Reflexión:
# - Aunque este enfoque con listas paralelas funciona, puede ser complicado y propenso a errores, 
#   especialmente si hay cambios en los datos o inconsistencias entre las listas.
# - Usar un diccionario sería una solución más directa y eficiente, donde los países serían las claves
#   y las capitales los valores. Esto se explorará más adelante.