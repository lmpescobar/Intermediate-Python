# Importar NumPy y matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

# Semilla para garantizar reproducibilidad
np.random.seed(123)

# Inicializar y llenar la lista all_walks
all_walks = []
for i in range(5):  # Simular 5 caminatas aleatorias
    random_walk = [0]
    for x in range(100):  # Cada caminata tiene 100 pasos
        step = random_walk[-1]  # Última posición
        dice = np.random.randint(1, 7)  # Lanzar dado (1 a 6)
        if dice <= 2:
            step = max(0, step - 1)  # No bajar de 0
        elif dice <= 5:
            step += 1
        else:
            step += np.random.randint(1, 7)  # Avanzar de 1 a 6 pasos
        random_walk.append(step)
    all_walks.append(random_walk)  # Guardar la caminata

# Convertir all_walks a un array de NumPy
np_aw = np.array(all_walks)

# Intentar graficar directamente np_aw
plt.plot(np_aw)
plt.show()  # ¿Funciona? Probablemente no se ve bien.

# Limpiar la figura
plt.clf()

# Transponer np_aw para organizarlo adecuadamente
np_aw_t = np.transpose(np_aw)

# Graficar la versión transpuesta
plt.plot(np_aw_t)
plt.show()  # Ahora sí, la gráfica debe ser clara y representar bien las caminatas.