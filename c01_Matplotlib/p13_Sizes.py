# Ejercicio: Ajustar el tamaño de los puntos en un gráfico de dispersión (Sizes)

# Descripción:
# En este ejercicio, personalizaremos un gráfico de dispersión para que el tamaño de los puntos refleje la población
# de cada país. Esto permite visualizar no solo la relación entre PIB per cápita y esperanza de vida, sino también
# la magnitud de la población de cada país.

# Objetivo:
# - Usar la biblioteca numpy para manipular datos de población.
# - Escalar los valores de población para ajustar el tamaño de los puntos en el gráfico.
# - Incorporar el tamaño de los puntos como un argumento `s` en la función `plt.scatter()`.

# Código en Python:

# Importar las bibliotecas necesarias.
import matplotlib.pyplot as plt
import numpy as np

# Datos ficticios:
# Lista de PIB per cápita (gdp_cap) en dólares estadounidenses.
gdp_cap = [974.5803384, 5937.029526, 6223.367465, 4797.231267, 12779.37964, 34435.36744, 36126.4927]

# Lista de esperanza de vida (life_exp) en años.
life_exp = [43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829]

# Lista de población (pop) en millones de personas.
pop = [31.889923, 3.600523, 33.333216, 12.420476, 64.221156, 35.653065, 23.301725]

# Convertir la lista de población a un array de numpy.
np_pop = np.array(pop)

# Escalar los valores de población para aumentar el tamaño de los puntos.
np_pop = np_pop * 2  # Duplicar los valores de np_pop para que los puntos sean más visibles.

# Crear un gráfico de dispersión con los tamaños de los puntos ajustados.
plt.scatter(gdp_cap, life_exp, s=np_pop)

# Personalizaciones previas:
plt.xscale('log')  # Escala logarítmica en el eje x.
plt.xlabel('GDP per Capita [in USD]')  # Etiqueta para el eje x.
plt.ylabel('Life Expectancy [in years]')  # Etiqueta para el eje y.
plt.title('World Development in 2007')  # Título del gráfico.

# Personalizar los ticks del eje x.
plt.xticks([1000, 10000, 100000], ['1k', '10k', '100k'])

# Mostrar el gráfico personalizado.
plt.show()

# Reflexión:
# - Ajustar el tamaño de los puntos en función de la población permite agregar una tercera dimensión de información
#   al gráfico (PIB per cápita, esperanza de vida y población).
# - Usar numpy facilita la manipulación de datos numéricos y permite aplicar operaciones como escalado de manera eficiente.
# - Este enfoque hace que los gráficos sean más informativos y atractivos para el análisis visual.