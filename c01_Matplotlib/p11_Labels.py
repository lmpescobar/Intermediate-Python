# Ejercicio: Etiquetas y título en un gráfico de dispersión (Labels)

# Descripción:
# Este ejercicio tiene como objetivo personalizar un gráfico de dispersión utilizando datos de desarrollo mundial.
# El gráfico muestra el PIB per cápita (en escala logarítmica) en el eje x y la esperanza de vida en el eje y.
# Se agregarán etiquetas a los ejes y un título para que el gráfico sea más claro y comprensible.

# Objetivo:
# - Personalizar el gráfico agregando etiquetas a los ejes x e y con `xlabel()` y `ylabel()`.
# - Agregar un título al gráfico con `title()`.
# - Visualizar el gráfico personalizado con `plt.show()`.

# Código en Python:

# Importar la subbiblioteca pyplot de matplotlib.
import matplotlib.pyplot as plt

# Datos ficticios:
# Lista de PIB per cápita (gdp_cap) en dólares estadounidenses.
gdp_cap = [974.5803384, 5937.029526, 6223.367465, 4797.231267, 12779.37964, 34435.36744, 36126.4927]

# Lista de esperanza de vida (life_exp) en años.
life_exp = [43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829]

# Crear un gráfico de dispersión básico.
plt.scatter(gdp_cap, life_exp)

# Escala logarítmica en el eje x.
plt.xscale('log')

# Personalizar etiquetas y título:
# Strings definidos para las etiquetas y el título.
xlab = 'GDP per Capita [in USD]'  # Etiqueta del eje x.
ylab = 'Life Expectancy [in years]'  # Etiqueta del eje y.
title = 'World Development in 2007'  # Título del gráfico.

# Agregar etiquetas a los ejes.
plt.xlabel(xlab)  # Etiqueta para el eje x.
plt.ylabel(ylab)  # Etiqueta para el eje y.

# Agregar título al gráfico.
plt.title(title)

# Mostrar el gráfico personalizado.
plt.show()

# Reflexión:
# - Al agregar etiquetas y un título, el gráfico se vuelve mucho más claro, incluso para personas que lo ven por primera vez.
# - La escala logarítmica en el eje x ayuda a visualizar mejor la amplia variación en los valores de PIB per cápita.
# - Este tipo de personalización es esencial para comunicar datos de manera efectiva.