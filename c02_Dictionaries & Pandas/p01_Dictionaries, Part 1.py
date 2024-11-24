# Ejercicio: Introducción a los diccionarios en Python

# Descripción:
# En este ejercicio, aprenderemos a usar diccionarios para mapear claves (keys) a valores (values).
# Este tipo de estructura de datos es muy útil para almacenar pares relacionados, como países y sus poblaciones.
# Compararemos cómo realizar esta tarea usando listas paralelas frente al uso de diccionarios.

# Objetivo:
# - Crear un diccionario que relacione países con sus poblaciones.
# - Acceder al valor correspondiente a una clave específica.

# Código en Python:

# Listas paralelas: países y sus poblaciones.
countries = ["afghanistan", "albania", "algeria"]  # Lista de países.
pop = [30.55, 2.77, 39.21]  # Lista de poblaciones en millones.

# Acceso utilizando índices: encontrar la población de Albania.
ind_alb = countries.index("albania")  # Encuentra el índice de Albania.
pop_alb = pop[ind_alb]  # Usa el índice para acceder a la población.
print("Población de Albania (usando listas):", pop_alb, "millones")

# Diccionario: relación directa entre países y poblaciones.
world = {"afghanistan": 30.55, "albania": 2.77, "algeria": 39.21}

# Acceso usando una clave: obtener la población de Albania.
print("Población de Albania (usando diccionario):", world["albania"], "millones")

# Reflexión:
# - Usar listas paralelas requiere encontrar primero el índice de un país y luego usarlo para acceder a la población,
#   lo cual no es conveniente ni intuitivo.
# - Usar diccionarios permite un acceso directo mediante claves, lo que es más eficiente y claro.
# - Los diccionarios son especialmente útiles cuando se trabaja con grandes cantidades de datos relacionados.