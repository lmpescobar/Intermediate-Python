# Ejercicio
# Simulación de una distribución de pasos finales de un "random walk" (camino aleatorio) tras múltiples simulaciones.

# Instrucciones
# - Simular una caminata aleatoria basada en un juego de lanzamiento de moneda.
# - Repetir la simulación 100, 1,000 y 10,000 veces.
# - Visualizar la distribución de pasos finales utilizando histogramas.

# Código en Python
# Importar las bibliotecas necesarias
import numpy as np  # Para simulaciones y generación de números aleatorios
import matplotlib.pyplot as plt  # Para crear gráficos

# Fijar una semilla para reproducibilidad
np.random.seed(123)

# Inicializar una lista para almacenar los resultados finales de cada simulación
final_steps = []

# Realizar 10,000 simulaciones del camino aleatorio
for i in range(10000):  # Cambia a 100 o 1,000 para simular menos veces.
    # Inicializar la caminata con el primer paso en 0
    random_walk = [0]

    # Simular 100 lanzamientos de dado para construir la caminata aleatoria
    for x in range(100):
        step = random_walk[-1]  # Obtener el paso actual
        dice = np.random.randint(1, 7)  # Generar un número aleatorio entre 1 y 6

        # Determinar el siguiente paso según el valor del dado
        if dice <= 2:
            step = max(0, step - 1)  # No ir por debajo de 0
        elif dice <= 5:
            step = step + 1  # Avanzar un paso
        else:
            step = step + np.random.randint(1, 7)  # Avanzar 1 a 6 pasos adicionales

        # Agregar el paso al camino
        random_walk.append(step)

    # Almacenar el paso final de esta simulación
    final_steps.append(random_walk[-1])

# Crear un histograma para visualizar la distribución de pasos finales
plt.hist(final_steps, bins=10, edgecolor='black')
plt.title('Distribución de pasos finales (10,000 simulaciones)')
plt.xlabel('Pasos finales')
plt.ylabel('Frecuencia')
plt.show()

# Explicación del código:
# 1. `np.random.seed(123)` garantiza que los resultados sean reproducibles.
# 2. El bucle externo (`for i in range(10000)`) simula 10,000 caminatas aleatorias.
# 3. Cada caminata tiene 100 lanzamientos de dados, donde cada lanzamiento determina el siguiente paso.
# 4. Se utiliza `max(0, step - 1)` para evitar que el camino baje por debajo de 0.
# 5. El histograma muestra la distribución de pasos finales, visualizando el comportamiento del camino aleatorio.