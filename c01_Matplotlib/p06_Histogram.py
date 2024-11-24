# Ejercicio: Introducción a los histogramas

# Descripción:
# Un histograma es un tipo de visualización que se utiliza para explorar la distribución de los datos. 
# Divide los valores en intervalos iguales llamados "bins" (o contenedores) y representa cuántos valores caen 
# dentro de cada intervalo. Es muy útil para observar patrones, como la concentración de valores o la dispersión.

# Concepto de un histograma:
# - Se parte de una serie de datos.
# - Se define cuántos bins tendrá el histograma (por ejemplo, 3 bins con un ancho de 2 cada uno).
# - Se cuenta cuántos valores caen en cada bin.
# - Se representa esta frecuencia como barras cuya altura corresponde al número de datos en el bin.

# Objetivo:
# Crear un histograma en Python usando la función `hist` de `matplotlib`.

# Código en Python:

# 1. Importar la biblioteca pyplot de matplotlib.
import matplotlib.pyplot as plt

# 2. Crear una lista de valores de ejemplo para el histograma.
# Estos valores representan datos distribuidos entre 0 y 6.
values = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 1.0, 2.0, 3.0, 4.0, 5.0, 0.0]

# 3. Construir un histograma.
# `bins=3` divide los datos en 3 intervalos iguales.
plt.hist(values, bins=3)

# 4. Mostrar el histograma.
plt.show()

# Explicación del código:
# - `plt.hist(values, bins=3)`: Crea un histograma a partir de la lista `values`.
#   - El argumento `values` contiene los datos.
#   - `bins=3` divide los datos en tres intervalos.
# - `plt.show()`: Muestra el gráfico generado en pantalla.

# Ejemplo de aplicación: Pirámide poblacional
# Para crear una visualización más compleja como una pirámide poblacional, puedes usar histogramas horizontales.
# Los datos representarían las distribuciones de edades por género.

# Datos simulados para pirámide poblacional:
# Distribución de población masculina y femenina por grupo de edad.
male_population = [-10, -9, -8, -7, -6, -5]  # Negativo para graficar a la izquierda.
female_population = [10, 9, 8, 7, 6, 5]     # Positivo para graficar a la derecha.
age_groups = [0, 10, 20, 30, 40, 50]        # Grupos de edad.

# Crear un gráfico de barras horizontales para pirámide poblacional.
plt.barh(age_groups, male_population, color='blue', label='Hombres')  # Población masculina.
plt.barh(age_groups, female_population, color='pink', label='Mujeres')  # Población femenina.

# Agregar etiquetas y título.
plt.xlabel('Población (millones)')
plt.ylabel('Edad')
plt.title('Pirámide poblacional (Ejemplo)')
plt.legend()

# Mostrar el gráfico.
plt.show()

# Reflexión:
# - Los histogramas son herramientas poderosas para observar la distribución de datos.
# - En aplicaciones como la pirámide poblacional, se puede usar para observar cambios demográficos a lo largo del tiempo.
# - En el caso de histogramas verticales, como los de distribución de datos, son útiles para ver concentraciones y patrones.