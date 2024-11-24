# Ejercicio: Construir un histograma (Build a histogram 1)

# Descripción:
# En este ejercicio, utilizaremos datos de `life_exp`, una lista que contiene la esperanza de vida
# para diferentes países en 2007. Nuestro objetivo es explorar cómo están distribuidos estos valores
# creando un histograma. Un histograma es una excelente herramienta para observar patrones en la
# distribución de datos.

# Objetivo:
# Crear un histograma de los valores en `life_exp` usando la función `plt.hist()` de Matplotlib.

# Instrucciones:
# 1. Usa `plt.hist()` para construir un histograma de los valores en la lista `life_exp`.
#    No especifiques el número de bins; Python usará 10 por defecto.
# 2. Usa `plt.show()` para mostrar el histograma en pantalla.
# 3. Observa cuál bin contiene la mayor cantidad de valores.

# Código en Python:

# Importar la subbiblioteca pyplot de matplotlib.
import matplotlib.pyplot as plt

# Lista de esperanza de vida (life_exp) en diferentes países en 2007.
life_exp = [43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829, 75.635, 64.062, 79.441,
            56.728, 65.554, 74.852, 50.728, 72.39, 73.005, 52.295, 49.58, 59.723, 72.368]

# 1. Crear el histograma con `plt.hist()`.
# Usamos los valores de `life_exp` como entrada.
# No especificamos los bins, por lo que se utilizará el valor por defecto (10 bins).
plt.hist(life_exp)

# 2. Mostrar el histograma.
# Renderiza y muestra el gráfico en pantalla.
plt.show()

# Explicación del código:
# - `plt.hist(life_exp)`: Genera un histograma para visualizar la distribución de la lista `life_exp`.
#   - Los valores de `life_exp` se dividen en 10 intervalos (bins) por defecto.
#   - La altura de cada barra corresponde al número de valores que caen dentro de ese bin.
# - `plt.show()`: Renderiza y muestra el histograma.

# Reflexión:
# - Observa el histograma resultante para identificar cuál bin tiene más valores.
# - Un bin más alto indica una mayor concentración de valores en ese rango específico de esperanza de vida.
# - Esto te permite comprender rápidamente la distribución de la esperanza de vida entre los países en el dataset.