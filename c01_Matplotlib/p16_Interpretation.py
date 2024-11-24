# Ejercicio: Interpretación de un gráfico de dispersión

# Descripción:
# Este ejercicio se enfoca en interpretar un gráfico de dispersión que muestra la relación entre el PIB per cápita 
# (GDP per Capita) y la esperanza de vida (Life Expectancy). Además, utiliza colores para representar diferentes regiones.
# Aquí evaluaremos las características de los países representados en el gráfico, en particular aquellos en azul
# (que corresponden a África), para determinar patrones y correlaciones en los datos.

# Objetivo:
# - Identificar los países con bajo PIB per cápita y baja esperanza de vida (en azul, África).
# - Evaluar la relación entre el PIB per cápita y la esperanza de vida.
# - Responder preguntas sobre la posición de China e India en el gráfico.

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

# Personalizaciones del gráfico:
plt.xscale('log')  # Escala logarítmica en el eje x.
plt.xlabel('GDP per Capita [in USD]')  # Etiqueta para el eje x.
plt.ylabel('Life Expectancy [in years]')  # Etiqueta para el eje y.
plt.title('World Development in 2007')  # Título del gráfico.
plt.xticks([1000, 10000, 100000], ['1k', '10k', '100k'])  # Personalizar los ticks del eje x.

# Etiquetar puntos específicos (India y China) en el gráfico con `plt.text()`.
plt.text(1550, 71, 'India')  # Etiqueta para India.
plt.text(5700, 80, 'China')  # Etiqueta para China.

# Añadir una cuadrícula al gráfico.
plt.grid(True)

# Mostrar el gráfico personalizado.
plt.show()

# Reflexión e interpretación:
# 1. Los países en azul (correspondientes a África) tienen tanto un PIB per cápita bajo como una esperanza de vida baja.
# 2. Existe una correlación positiva entre el PIB per cápita y la esperanza de vida: los países con mayor PIB tienden 
#    a tener una mayor esperanza de vida.
# 3. Comparando China e India:
#    - China tiene un PIB per cápita y una esperanza de vida mayores que India.
# 4. Este gráfico permite identificar patrones globales relacionados con el desarrollo económico y la calidad de vida.