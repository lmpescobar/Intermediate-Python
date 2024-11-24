# Ejercicio: Gráficos básicos con Matplotlib

# Descripción del ejercicio:
# En este ejercicio, usarás Matplotlib para crear gráficos de línea y dispersión
# que representen la evolución de la población mundial a lo largo de los años.
# Aprenderás a:
# 1. Crear gráficos básicos.
# 2. Personalizar títulos y etiquetas de los ejes.
# 3. Mostrar los gráficos usando plt.show().

# Código en Python:
# Importar la biblioteca matplotlib.pyplot con el alias plt
import matplotlib.pyplot as plt

# Datos de ejemplo: años y población mundial en miles de millones
year = [1950, 1970, 1990, 2010]  # Lista de años
pop = [2.5, 3.7, 5.3, 7.0]  # Lista de población (en miles de millones)

# Crear un gráfico de línea
plt.plot(year, pop)  # Graficar los años (eje x) vs la población (eje y)
plt.title("Evolución de la población mundial (gráfico de línea)")  # Título del gráfico
plt.xlabel("Año")  # Etiqueta del eje x
plt.ylabel("Población (miles de millones)")  # Etiqueta del eje y
plt.show()  # Mostrar el gráfico de línea

# Crear un gráfico de dispersión
plt.scatter(year, pop)  # Graficar los datos como un gráfico de dispersión
plt.title("Evolución de la población mundial (gráfico de dispersión)")  # Título del gráfico
plt.xlabel("Año")  # Etiqueta del eje x
plt.ylabel("Población (miles de millones)")  # Etiqueta del eje y
plt.show()  # Mostrar el gráfico de dispersión

# Explicación del código:
# 1. Importación:
#    - Se usa `matplotlib.pyplot` como `plt`, que contiene funciones para graficar.
# 2. Gráfico de línea:
#    - `plt.plot(year, pop)` conecta los puntos (años, población) con una línea.
#    - `plt.title`, `plt.xlabel`, y `plt.ylabel` añaden un título y etiquetas a los ejes.
#    - `plt.show()` renderiza y muestra el gráfico.
# 3. Gráfico de dispersión:
#    - `plt.scatter(year, pop)` representa cada punto sin conectarlos con líneas.
#    - Se usan los mismos métodos de personalización de título y ejes.
#    - `plt.show()` muestra este gráfico.

# Practica:
# 1. Extiende los datos para agregar años futuros (ejemplo: 2030, 2050) e imagina
#    escenarios de crecimiento poblacional.
# 2. Cambia colores, estilos de líneas o puntos para explorar opciones de personalización.
# 3. Intenta graficar un histograma u otros gráficos para representar diferentes
#    tipos de datos.

# Notas adicionales:
# - Matplotlib es una herramienta poderosa para crear gráficos personalizados.
# - Cambia los parámetros de las funciones para practicar diferentes estilos.