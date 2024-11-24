# Ejercicio: Construir un histograma con diferentes bins (Build a histogram 2)

# Descripción:
# En este ejercicio, exploraremos cómo cambiar el número de bins afecta la visualización de un histograma.
# Los bins (o contenedores) determinan la cantidad de intervalos en los que se divide el rango de datos.
# Si hay muy pocos bins, se simplifica demasiado la realidad, perdiendo detalles. Si hay demasiados, 
# se sobrecarga el gráfico y puede ser difícil identificar tendencias generales.

# Objetivo:
# Construir dos histogramas:
# 1. El primero con 5 bins.
# 2. El segundo con 20 bins.
# Comparar ambos gráficos para analizar cuál representa mejor la distribución de los datos.

# Código en Python:

# Importar la subbiblioteca pyplot de matplotlib.
import matplotlib.pyplot as plt

# Lista de esperanza de vida (life_exp) en diferentes países en 2007.
life_exp = [43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829, 75.635, 64.062, 79.441,
            56.728, 65.554, 74.852, 50.728, 72.39, 73.005, 52.295, 49.58, 59.723, 72.368]

# 1. Construir un histograma con 5 bins.
# Esto divide los datos en 5 intervalos grandes.
plt.hist(life_exp, bins=5)

# Mostrar el histograma.
# `plt.show()` renderiza el gráfico.
plt.show()

# Limpiar el gráfico para evitar que se sobrepongan elementos con el próximo histograma.
# `plt.clf()` limpia el espacio de trabajo de pyplot.
plt.clf()

# 2. Construir un histograma con 20 bins.
# Esto divide los datos en intervalos más pequeños, mostrando más detalles.
plt.hist(life_exp, bins=20)

# Mostrar el histograma.
plt.show()

# Limpiar nuevamente el gráfico para evitar interferencias en futuros gráficos.
plt.clf()

# Reflexión:
# - El histograma con 5 bins proporciona una visión general de la distribución, pero puede ocultar detalles importantes.
# - El histograma con 20 bins muestra más detalles sobre la distribución de los valores, pero puede resultar más
#   difícil de interpretar debido al exceso de información.
# - El número ideal de bins depende del contexto y del objetivo del análisis.