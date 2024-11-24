# Ejercicio: Gráfico de línea (Line plot 3)

# Descripción:
# En este ejercicio, trabajaremos con datos recopilados en 2007 que el profesor Hans Rosling utilizó para
# construir su famoso gráfico de burbujas. Este gráfico explora la relación entre la riqueza de un país (medida
# a través del PIB per cápita) y la calidad de vida (medida por la esperanza de vida promedio). 
# Estos datos son importantes para comprender patrones globales en la economía y salud pública.
#
# Detalles de los datos:
# 1. `gdp_cap` (PIB per cápita):
#    - Significa Producto Interno Bruto por persona.
#    - Se calcula dividiendo el PIB total de un país entre su población.
#    - Se expresa en dólares estadounidenses para estandarizar los valores entre países.
#    - Indica el promedio de ingreso económico por persona en un país.
#
# 2. `life_exp` (esperanza de vida):
#    - Mide el promedio de años que se espera que viva una persona en un país.
#    - Es un indicador de salud pública y calidad de vida.
#
# Objetivo:
# Construiremos un gráfico de línea que relaciona el PIB per cápita con la esperanza de vida de diferentes países.
# Aunque un gráfico de línea no es el mejor tipo de visualización para estos datos, este ejercicio tiene como
# propósito aprender los fundamentos de cómo construir gráficos con Matplotlib.

# Instrucciones:
# 1. Usa `print()` para mostrar el último elemento de las listas `gdp_cap` y `life_exp`.
#    Esto corresponde a los datos para Zimbabue, un país con un PIB per cápita muy bajo y una baja esperanza de vida.
# 2. Utiliza `plt.plot()` para construir un gráfico de línea, donde:
#    - El eje x muestra `gdp_cap` (PIB per cápita).
#    - El eje y muestra `life_exp` (esperanza de vida).
# 3. Termina con `plt.show()` para mostrar el gráfico.
# 4. Reflexiona: ¿Es un gráfico de línea adecuado para representar esta relación entre países?

# Código en Python:

# Lista de PIB per cápita (gdp_cap) en dólares estadounidenses para diferentes países.
gdp_cap = [974.5803384, 5937.029526, 6223.367465, 4797.231267, 12779.37964, 34435.36744, 36126.4927]

# Lista de esperanza de vida (life_exp) en años correspondientes a los países de `gdp_cap`.
life_exp = [43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829]

# 1. Mostrar el último elemento de las listas `gdp_cap` y `life_exp`.
# Esto nos da información sobre Zimbabue, que tiene el valor más bajo en ambas listas.
print("PIB per cápita en Zimbabue:", gdp_cap[-1])  # Último valor en la lista `gdp_cap`.
print("Esperanza de vida en Zimbabue:", life_exp[-1])  # Último valor en la lista `life_exp`.

# Explicación de `print()`:
# - `gdp_cap[-1]` accede al último elemento de la lista `gdp_cap`, que representa el PIB per cápita de Zimbabue.
# - `life_exp[-1]` accede al último elemento de la lista `life_exp`, que representa la esperanza de vida en Zimbabue.

# 2. Importar la subbiblioteca `pyplot` de Matplotlib como `plt`.
# Matplotlib es una biblioteca de Python utilizada para crear gráficos de alta calidad. La subbiblioteca `pyplot`
# se utiliza para generar gráficos fácilmente.
import matplotlib.pyplot as plt

# 3. Crear un gráfico de línea usando `plt.plot()`.
# En el eje x usaremos `gdp_cap` (PIB per cápita).
# En el eje y usaremos `life_exp` (esperanza de vida).
plt.plot(gdp_cap, life_exp)

# Explicación de `plt.plot()`:
# - El primer argumento (`gdp_cap`) define los valores del eje x.
# - El segundo argumento (`life_exp`) define los valores del eje y.
# - Matplotlib conectará los puntos en el orden en que aparecen en las listas, creando un gráfico de línea.

# 4. Mostrar el gráfico con `plt.show()`.
# Esta función renderiza y muestra el gráfico en pantalla. Sin este comando, el gráfico no aparecerá.
plt.show()

# Reflexión:
# - El gráfico de línea conecta los puntos en el orden en que aparecen las listas. En este caso, no tiene sentido,
#   ya que los datos no están relacionados de manera secuencial. Por ejemplo, el PIB per cápita de un país no está
#   relacionado con el del siguiente.
# - Un gráfico de dispersión (`plt.scatter()`) sería más adecuado, ya que muestra cada punto individualmente,
#   lo que permite observar correlaciones entre el PIB per cápita y la esperanza de vida.