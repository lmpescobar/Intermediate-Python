# Ejercicio: Gráfico de dispersión (Scatter Plot 1)

# Descripción:
# Los gráficos de dispersión son una herramienta excelente para visualizar correlaciones entre dos variables.
# En este ejercicio, vamos a graficar la relación entre el PIB per cápita (`gdp_cap`) y la esperanza de vida (`life_exp`) 
# de diferentes países utilizando un gráfico de dispersión. Este tipo de gráfico es más adecuado que un gráfico de línea, 
# ya que los datos representan valores independientes y no tienen un orden secuencial lógico.

# Detalles de los datos:
# 1. `gdp_cap`: Lista que contiene el PIB per cápita (en dólares estadounidenses) para varios países.
# 2. `life_exp`: Lista que contiene la esperanza de vida promedio (en años) correspondiente a cada país.

# Objetivo:
# - Crear un gráfico de dispersión para explorar la relación entre la riqueza de un país (PIB per cápita) 
#   y su calidad de vida (esperanza de vida).
# - Usar una escala logarítmica para el eje x (PIB per cápita) para visualizar mejor los datos que abarcan 
#   un rango amplio de valores.

# Instrucciones:
# 1. Cambia el gráfico de línea del código a un gráfico de dispersión usando `plt.scatter()`.
# 2. Aplica una escala logarítmica al eje x con `plt.xscale('log')` para ajustar los datos.
# 3. Finaliza el script con `plt.show()` para mostrar el gráfico.

# Código en Python:

# Lista de PIB per cápita (gdp_cap) en dólares estadounidenses.
gdp_cap = [974.5803384, 5937.029526, 6223.367465, 4797.231267, 12779.37964, 34435.36744, 36126.4927]

# Lista de esperanza de vida (life_exp) en años.
life_exp = [43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829]

# 1. Crear un gráfico de dispersión usando `plt.scatter()`.
# Cambiamos de `plt.plot()` a `plt.scatter()` para mostrar cada punto de datos de forma individual.
import matplotlib.pyplot as plt  # Importamos la subbiblioteca pyplot de Matplotlib.
plt.scatter(gdp_cap, life_exp)  # Crea el gráfico de dispersión.

# 2. Ajustar el eje x a una escala logarítmica.
# Esto es útil porque el PIB per cápita tiene un rango muy amplio y una escala lineal podría dificultar la visualización.
plt.xscale('log')

# 3. Mostrar el gráfico.
# Renderizamos y mostramos el gráfico en pantalla.
plt.show()

# Explicación del código:
# - `plt.scatter(gdp_cap, life_exp)`: Crea un gráfico de dispersión, donde `gdp_cap` es el eje x y `life_exp` es el eje y.
# - `plt.xscale('log')`: Cambia la escala del eje x a logarítmica, lo cual es útil para datos que abarcan un rango muy amplio.
# - `plt.show()`: Renderiza y muestra el gráfico creado.
#
# Reflexión:
# - Un gráfico de dispersión es adecuado porque no implica continuidad entre puntos (como lo hace un gráfico de línea).
# - La escala logarítmica ayuda a visualizar mejor datos desiguales, como el PIB per cápita, ya que ajusta las diferencias extremas.