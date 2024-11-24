# Ejercicio: Gráfico de línea (Line plot 1)

# Descripción:
# Con Matplotlib, puedes crear una variedad de gráficos en Python. El gráfico más básico es el gráfico de línea.
# Esta herramienta es útil para observar tendencias en los datos a lo largo del tiempo. En este ejercicio,
# utilizaremos listas con años (`year`) y poblaciones correspondientes (`pop`) para representar el crecimiento
# de la población mundial desde 1950 hasta una proyección para 2100.

# Ejemplo general:
# Para generar un gráfico de línea básico con Matplotlib, se utiliza la siguiente estructura:
# import matplotlib.pyplot as plt
# plt.plot(x, y)
# plt.show()

# En este ejercicio, ya tienes cargadas las listas `year` y `pop` en tu espacio de trabajo. La lista `year` contiene
# los años y la lista `pop` contiene las poblaciones correspondientes (en miles de millones).

# Instrucciones:
# 1. Usa `print()` para mostrar el último elemento de las listas `year` y `pop` para ver la población proyectada en 2100.
# 2. Importa la subbiblioteca `pyplot` de Matplotlib como `plt` (abreviatura estándar).
# 3. Usa `plt.plot()` para construir un gráfico de línea donde `year` es el eje horizontal (x) y `pop` el eje vertical (y).
# 4. Usa `plt.show()` para mostrar el gráfico en pantalla.

# Código en Python:

# Lista de años clave desde 1950 hasta 2100.
year = [1950, 1970, 1990, 2010, 2100]  # Años correspondientes a datos reales y estimados.

# Lista de población mundial correspondiente a los años de la lista anterior (en miles de millones).
pop = [2.5, 3.7, 5.3, 7.0, 10.0]  # Datos de población real y estimada.

# 1. Mostrar el último elemento de las listas `year` y `pop` para observar los datos de proyección para 2100.
print("Último año registrado:", year[-1])  # Muestra el último año (2100).
print("Población estimada para el año 2100:", pop[-1])  # Muestra la población estimada para 2100 (10.0 mil millones).

# 2. Importar la subbiblioteca `pyplot` de Matplotlib.
# `pyplot` es la subbiblioteca más usada de Matplotlib y se importa comúnmente como `plt`.
import matplotlib.pyplot as plt

# 3. Crear un gráfico de línea usando `plt.plot()`.
# La función `plt.plot()` genera un gráfico de línea, donde:
# - `year` se usa para el eje horizontal (x).
# - `pop` se usa para el eje vertical (y).
plt.plot(year, pop)

# 4. Mostrar el gráfico con `plt.show()`.
# Esta función es necesaria para renderizar y visualizar el gráfico creado.
plt.show()

# Explicación del código:
# - `year` y `pop`: Son listas que representan los datos del eje x (años) y del eje y (población), respectivamente.
# - `print(year[-1])` y `print(pop[-1])`: Utilizan índices negativos para acceder al último elemento de las listas.
# - `import matplotlib.pyplot as plt`: Importa la biblioteca Matplotlib y su subpaquete `pyplot` como `plt` para abreviar.
# - `plt.plot(year, pop)`: Genera un gráfico de línea conectando los puntos especificados por `year` y `pop`.
# - `plt.show()`: Renderiza y muestra el gráfico en pantalla.

# Notas adicionales:
# - Matplotlib permite personalizar el gráfico agregando títulos, etiquetas en los ejes, colores, leyendas y más.
# - El gráfico resultante mostrará cómo ha cambiado la población mundial desde 1950 y su proyección hasta 2100.
# - Este ejercicio es introductorio, pero sirve como base para crear gráficos más complejos.