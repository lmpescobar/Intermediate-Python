# Ejercicio: Personalización de ticks en el eje x (Ticks)

# Descripción:
# En este ejercicio, aprenderemos cómo personalizar los ticks en el eje x de un gráfico utilizando matplotlib.
# Los ticks ayudan a que el gráfico sea más legible al mostrar valores significativos con etiquetas personalizadas.
# Aquí, trabajaremos con un gráfico de dispersión que muestra el PIB per cápita (eje x) frente a la esperanza
# de vida (eje y) y personalizaremos los ticks del eje x para hacerlos más claros.

# Objetivo:
# - Ajustar los ticks del eje x para mostrar valores en una escala más legible (e.g., "1k", "10k", "100k").
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

# Personalizaciones previas:
plt.xscale('log')  # Escala logarítmica en el eje x.
plt.xlabel('GDP per Capita [in USD]')  # Etiqueta del eje x.
plt.ylabel('Life Expectancy [in years]')  # Etiqueta del eje y.
plt.title('World Development in 2007')  # Título del gráfico.

# Definición de valores y etiquetas de los ticks en el eje x.
tick_val = [1000, 10000, 100000]  # Valores numéricos de los ticks.
tick_lab = ['1k', '10k', '100k']  # Etiquetas correspondientes en formato legible.

# Adaptar los ticks del eje x usando plt.xticks().
plt.xticks(tick_val, tick_lab)

# Mostrar el gráfico personalizado.
plt.show()

# Reflexión:
# - Cambiar los ticks del eje x a un formato más legible (e.g., "1k" en lugar de "1000") facilita la interpretación del gráfico.
# - La escala logarítmica en el eje x ayuda a visualizar mejor las grandes variaciones en el PIB per cápita.
# - Esta personalización es especialmente útil cuando se presentan datos a audiencias no técnicas, mejorando la comunicación.