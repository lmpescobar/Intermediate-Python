# Ejercicio: Personalizaciones adicionales en gráficos de dispersión

# Descripción:
# En este ejercicio, se realizarán personalizaciones adicionales en un gráfico de dispersión. 
# Esto incluye agregar etiquetas específicas para países clave (India y China) con `plt.text()` 
# y una cuadrícula al fondo con `plt.grid(True)` para mejorar la claridad visual.

# Objetivo:
# - Usar `plt.text()` para etiquetar puntos específicos en el gráfico.
# - Añadir una cuadrícula al fondo del gráfico con `plt.grid(True)`.

# Código en Python:

# Importar las bibliotecas necesarias.
import matplotlib.pyplot as plt
import numpy as np

# Datos:
# Lista de PIB per cápita (gdp_cap) en dólares estadounidenses.
gdp_cap = [974.5803384, 5937.029526, 6223.367465, 4797.231267, 12779.37964, 34435.36744, 36126.4927]

# Lista de esperanza de vida (life_exp) en años.
life_exp = [43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829]

# Lista de población (pop) en millones de personas.
pop = [31.889923, 3.600523, 33.333216, 12.420476, 64.221156, 35.653065, 23.301725]

# Lista de continentes correspondiente a cada país.
continent = ['Asia', 'Europe', 'Africa', 'Africa', 'Americas', 'Europe', 'Asia']

# Diccionario que asigna colores a cada continente.
dict = {
    'Asia': 'red',
    'Europe': 'green',
    'Africa': 'blue',
    'Americas': 'yellow',
    'Oceania': 'black'
}

# Crear una lista de colores para cada país basado en el continente usando el diccionario.
col = [dict[cont] for cont in continent]

# Convertir la lista de población a un array de numpy y escalar los valores para ajustar el tamaño de los puntos.
np_pop = np.array(pop) * 2

# Crear un gráfico de dispersión con colores y opacidad personalizados.
plt.scatter(x=gdp_cap, y=life_exp, s=np_pop, c=col, alpha=0.8)

# Personalizaciones previas:
plt.xscale('log')  # Escala logarítmica en el eje x.
plt.xlabel('GDP per Capita [in USD]')  # Etiqueta para el eje x.
plt.ylabel('Life Expectancy [in years]')  # Etiqueta para el eje y.
plt.title('World Development in 2007')  # Título del gráfico.

# Personalizar los ticks del eje x.
plt.xticks([1000, 10000, 100000], ['1k', '10k', '100k'])

# Personalizaciones adicionales:
# Etiquetar puntos específicos (India y China) en el gráfico con `plt.text()`.
plt.text(1550, 71, 'India')  # Etiqueta para India.
plt.text(5700, 80, 'China')  # Etiqueta para China.

# Añadir una cuadrícula al fondo del gráfico.
plt.grid(True)

# Mostrar el gráfico personalizado.
plt.show()

# Reflexión:
# - Etiquetar puntos específicos con `plt.text()` ayuda a identificar países clave en el gráfico.
# - La cuadrícula añadida con `plt.grid(True)` mejora la claridad visual, especialmente para gráficos con múltiples datos.
# - Estas personalizaciones hacen que el gráfico sea más informativo y fácil de interpretar.