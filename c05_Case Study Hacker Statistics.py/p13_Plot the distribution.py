# Importar numpy y matplotlib, y establecer la semilla
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

# Simular caminata aleatoria 500 veces
all_walks = []
for i in range(500):  # Realizar 500 simulaciones
    random_walk = [0]
    for x in range(100):  # Cada caminata tiene 100 pasos
        step = random_walk[-1]
        dice = np.random.randint(1, 7)  # Lanzar el dado (1 a 6)
        if dice <= 2:
            step = max(0, step - 1)  # Mover un paso hacia abajo, sin bajar de 0
        elif dice <= 5:
            step = step + 1  # Mover un paso hacia arriba
        else:
            step = step + np.random.randint(1, 7)  # Subir de 1 a 6 pasos adicionales

        # Implementar tropiezo (probabilidad del 0.1%)
        if np.random.rand() <= 0.001:
            step = 0  # Reiniciar el paso a 0 en caso de tropiezo

        random_walk.append(step)  # Agregar el nuevo paso a la caminata actual

    all_walks.append(random_walk)  # Almacenar la caminata completa en all_walks

# Convertir la lista de listas a un arreglo de NumPy y transponer
np_aw_t = np.transpose(np.array(all_walks))

# Seleccionar la última fila de np_aw_t (los puntos finales)
ends = np_aw_t[-1, :]  # Última fila contiene los puntos finales de todas las caminatas

# Graficar un histograma de los puntos finales
plt.hist(ends, bins=20, edgecolor='black')
plt.title('Distribución de los pasos finales')
plt.xlabel('Paso final')
plt.ylabel('Frecuencia')
plt.show()