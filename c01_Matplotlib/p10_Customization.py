# Ejercicio: Personalización de gráficos con datos históricos

# Descripción:
# Este ejercicio muestra cómo personalizar gráficos en Python usando matplotlib para contar una historia clara.
# Agregaremos etiquetas a los ejes, un título, ajustaremos los ticks del eje y y añadiremos datos históricos
# para completar la narrativa sobre el crecimiento poblacional global.

# Objetivo:
# - Crear un gráfico de línea que muestre el crecimiento poblacional global hasta 2100.
# - Personalizar el gráfico con etiquetas, título y ajustes en los ejes.
# - Agregar datos históricos (1800, 1850, 1900) para dar un contexto más completo.

# Código en Python:

# Importar la subbiblioteca pyplot de matplotlib.
import matplotlib.pyplot as plt

# Lista de años clave desde 1950 hasta 2100 (incluye proyecciones).
year = [1950, 1970, 1990, 2010, 2100]
# Lista de población mundial (en miles de millones) correspondiente a los años de la lista anterior.
pop = [2.538, 3.692, 5.263, 6.972, 10.85]

# Agregar datos históricos:
# Datos de población mundial para 1800, 1850 y 1900.
historical_years = [1800, 1850, 1900]
historical_pop = [1.0, 1.262, 1.650]

# Combinar los datos históricos con los datos existentes.
year = historical_years + year  # Extender la lista de años.
pop = historical_pop + pop      # Extender la lista de población.

# 1. Crear el gráfico de línea con los datos actualizados.
plt.plot(year, pop, marker='o', linestyle='-', color='b')

# 2. Personalizar el gráfico:
# Etiquetar los ejes x e y.
plt.xlabel('Año')  # Etiqueta para el eje x.
plt.ylabel('Población (miles de millones)')  # Etiqueta para el eje y.

# Agregar un título al gráfico.
plt.title('Proyecciones de población mundial')

# Ajustar los ticks del eje y:
# Establecer los valores de los ticks (de 0 a 10 en intervalos de 2).
yticks_values = [0, 2, 4, 6, 8, 10]
# Establecer etiquetas para los ticks con "B" que indica "Billones".
yticks_labels = ['0', '2B', '4B', '6B', '8B', '10B']
plt.yticks(yticks_values, yticks_labels)

# 3. Mostrar el gráfico.
plt.show()

# Reflexión:
# - Etiquetar los ejes y agregar un título proporciona contexto y claridad al gráfico.
# - Personalizar los ticks del eje y ayuda a interpretar mejor los valores, especialmente con la unidad "B" (Billones).
# - Agregar datos históricos da un panorama más completo, mostrando el crecimiento exponencial de la población
#   desde el siglo XIX hasta las proyecciones futuras.