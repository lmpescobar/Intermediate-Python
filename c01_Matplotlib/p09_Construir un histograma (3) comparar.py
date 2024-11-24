# Ejercicio: Comparar histogramas (Build a histogram 3: compare)

# Descripción:
# En este ejercicio, compararemos datos de esperanza de vida de dos periodos: 1950 y 2007. 
# Ambos conjuntos de datos contienen información sobre la esperanza de vida (`life_exp` para 2007 y `life_exp1950` para 1950).
# Construiremos histogramas para ambos periodos utilizando el mismo número de bins para observar las diferencias 
# y cómo han cambiado las distribuciones a lo largo del tiempo.

# Objetivo:
# - Construir un histograma de los datos de 2007 (`life_exp`) con 15 bins.
# - Construir un histograma de los datos de 1950 (`life_exp1950`) también con 15 bins.
# - Comparar ambos gráficos para identificar diferencias.

# Código en Python:

# Importar la subbiblioteca pyplot de matplotlib.
import matplotlib.pyplot as plt

# Lista de esperanza de vida (life_exp) para 2007.
life_exp = [43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829, 75.635, 64.062, 79.441,
            56.728, 65.554, 74.852, 50.728, 72.39, 73.005, 52.295, 49.58, 59.723, 72.368]

# Lista de esperanza de vida (life_exp1950) para 1950.
life_exp1950 = [28.801, 55.23, 43.829, 30.02, 62.485, 69.615, 72.39, 37.579, 38.485, 67.946,
                37.176, 42.962, 37.176, 40.931, 50.848, 58.089, 40.41, 39.92, 43.149, 47.452]

# 1. Construir un histograma de `life_exp` con 15 bins.
plt.hist(life_exp, bins=15)

# Mostrar el histograma.
plt.show()

# Limpiar el gráfico para preparar el siguiente.
plt.clf()

# 2. Construir un histograma de `life_exp1950` con 15 bins.
plt.hist(life_exp1950, bins=15)

# Mostrar el histograma.
plt.show()

# Limpiar nuevamente el gráfico para futuros usos.
plt.clf()

# Reflexión:
# - El histograma de `life_exp` (2007) muestra una distribución más concentrada en valores altos, indicando un aumento 
#   generalizado en la esperanza de vida para la mayoría de los países.
# - El histograma de `life_exp1950` está más disperso hacia valores bajos, reflejando una esperanza de vida más corta en esa época.
# - Esta comparación evidencia el progreso en la salud pública y el desarrollo global a lo largo de más de medio siglo.