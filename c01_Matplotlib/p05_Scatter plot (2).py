# Ejercicio: Gráfico de dispersión (Scatter Plot 2)

# Descripción:
# En el ejercicio anterior, se demostró que un mayor PIB per cápita está asociado con una mayor esperanza de vida,
# lo que muestra una correlación positiva. Ahora vamos a explorar si existe una relación similar entre la población
# total de un país y su esperanza de vida promedio.
#
# Detalles de los datos:
# 1. `life_exp` (esperanza de vida):
#    - Representa el promedio de años que se espera que vivan las personas en diferentes países.
# 2. `pop` (población):
#    - Lista que contiene las poblaciones de diferentes países, expresadas en millones de personas.
#
# Objetivo:
# - Construir un gráfico de dispersión que relacione la población (`pop`) en el eje x con la esperanza de vida (`life_exp`)
#   en el eje y.
# - Analizar si existe alguna correlación entre estas dos variables.

# Instrucciones:
# 1. Importa la subbiblioteca `matplotlib.pyplot` como `plt`.
# 2. Usa `plt.scatter()` para construir un gráfico de dispersión:
#    - `pop` en el eje x (población).
#    - `life_exp` en el eje y (esperanza de vida).
# 3. Usa `plt.show()` para mostrar el gráfico generado.
# 4. Reflexiona sobre la relación entre población y esperanza de vida: ¿ves alguna correlación?

# Código en Python:

# 1. Importar la subbiblioteca `pyplot` de Matplotlib como `plt`.
# Matplotlib es la biblioteca estándar para crear gráficos en Python.
import matplotlib.pyplot as plt

# Datos:
# Lista de esperanza de vida (life_exp) en años.
life_exp = [43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829]

# Lista de población (pop) en millones de personas.
pop = [31.889923, 3.600523, 33.333216, 12.420476, 64.221156, 35.653065, 23.301725]

# 2. Crear un gráfico de dispersión.
# `pop` en el eje x (población) y `life_exp` en el eje y (esperanza de vida).
plt.scatter(pop, life_exp)

# Explicación de `plt.scatter()`:
# - `pop` define los valores del eje horizontal (x), que son las poblaciones de los países.
# - `life_exp` define los valores del eje vertical (y), que son las esperanzas de vida.

# 3. Mostrar el gráfico en pantalla.
# `plt.show()` renderiza y muestra el gráfico creado.
plt.show()

# Reflexión:
# - En este gráfico de dispersión, cada punto representa un país, con la población en el eje x y la esperanza de vida
#   en el eje y.
# - Si los puntos no forman un patrón claro (por ejemplo, creciente o decreciente), significa que no hay una relación
#   fuerte entre la población y la esperanza de vida.
# - Esto puede indicar que la población total de un país no está directamente relacionada con la calidad de vida de
#   sus habitantes.