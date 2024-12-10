# Ejercicio: Visualizar un camino aleatorio
# Descripción:
# Generar un camino aleatorio de 100 pasos y graficarlo utilizando la librería `matplotlib`.

# Código en Python:

# Importar las librerías necesarias
import numpy as np  # Para generar números aleatorios
import matplotlib.pyplot as plt  # Para crear gráficos

# Establecer la semilla para reproducibilidad
np.random.seed(123)

# Inicializar el camino aleatorio
random_walk = [0]  # Comienza en la posición 0

# Generar 100 pasos aleatorios
for x in range(100):
    # Obtener el último paso
    step = random_walk[-1]
    # Lanzar el dado
    dice = np.random.randint(1, 7)

    # Determinar el siguiente paso
    if dice <= 2:  # Retroceder un paso
        step = max(0, step - 1)  # Evitar que baje de 0
    elif dice <= 5:  # Avanzar un paso
        step = step + 1
    else:  # Avanzar un número aleatorio de pasos
        step = step + np.random.randint(1, 7)

    # Agregar el nuevo paso al camino aleatorio
    random_walk.append(step)

# Graficar el camino aleatorio
plt.plot(random_walk)  # Crear un gráfico de línea con los datos de random_walk
plt.title("Camino Aleatorio")  # Título del gráfico
plt.xlabel("Número de pasos")  # Etiqueta del eje x
plt.ylabel("Posición")  # Etiqueta del eje y

# Mostrar el gráfico
plt.show()

# Explicación del código:
# 1. `np.random.seed(123)`: Establece la semilla para que los números aleatorios sean reproducibles.
# 2. `random_walk = [0]`: Inicializa el camino aleatorio en la posición 0.
# 3. `for x in range(100)`: Itera 100 veces para generar 100 pasos.
# 4. `np.random.randint(1, 7)`: Simula el lanzamiento de un dado de 6 caras.
# 5. `max(0, step - 1)`: Asegura que la posición no sea menor a 0.
# 6. `plt.plot(random_walk)`: Grafica el camino aleatorio como una línea.
# 7. `plt.show()`: Muestra el gráfico en pantalla.