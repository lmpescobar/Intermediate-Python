# Importar librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

# Establecer semilla para reproducibilidad
np.random.seed(123)

# Limpiar la figura para evitar acumulación de gráficos
plt.clf()

# Simular caminata aleatoria 20 veces
all_walks = []  # Lista para almacenar todas las caminatas
for i in range(20):  # Realizar 20 simulaciones
    random_walk = [0]  # Comenzar cada caminata desde el paso 0
    for x in range(100):  # Cada caminata tiene 100 pasos
        step = random_walk[-1]  # Obtener el último paso
        dice = np.random.randint(1, 7)  # Lanzar el dado (1 a 6)
        if dice <= 2:
            step = max(0, step - 1)  # Mover un paso hacia abajo, sin bajar de 0
        elif dice <= 5:
            step = step + 1  # Mover un paso hacia arriba
        else:
            step = step + np.random.randint(1, 7)  # Subir de 1 a 6 pasos adicionales

        # Implementar tropiezo (probabilidad del 0.5%)
        if np.random.rand() <= 0.005:
            step = 0  # Reiniciar el paso a 0 en caso de tropiezo

        random_walk.append(step)  # Agregar el nuevo paso a la caminata actual

    all_walks.append(random_walk)  # Almacenar la caminata completa en all_walks

# Convertir la lista de listas a un arreglo de NumPy y transponer
np_aw_t = np.transpose(np.array(all_walks))

# Graficar todas las caminatas
plt.plot(np_aw_t)
plt.show()