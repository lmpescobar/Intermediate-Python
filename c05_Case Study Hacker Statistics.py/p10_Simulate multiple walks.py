# Importar NumPy y establecer la semilla para reproducibilidad
import numpy as np
np.random.seed(123)

# Inicializar la lista all_walks para almacenar todas las caminatas aleatorias
all_walks = []

# Simular 5 caminatas aleatorias
for i in range(5):  # El bucle externo se ejecuta 5 veces
    # Inicializar una caminata aleatoria
    random_walk = [0]
    
    # Simular una caminata aleatoria de 100 pasos
    for x in range(100):  # El bucle interno se ejecuta 100 veces por cada caminata
        step = random_walk[-1]  # Obtener el último paso
        dice = np.random.randint(1, 7)  # Lanzar el dado (número entre 1 y 6)

        # Decidir el siguiente paso según el valor del dado
        if dice <= 2:  # Si el dado es 1 o 2, bajar un paso (sin ir por debajo de 0)
            step = max(0, step - 1)
        elif dice <= 5:  # Si el dado es 3, 4 o 5, subir un paso
            step = step + 1
        else:  # Si el dado es 6, subir de 1 a 6 pasos adicionales
            step = step + np.random.randint(1, 7)
        
        # Agregar el nuevo paso a la caminata
        random_walk.append(step)
    
    # Agregar la caminata completa a la lista all_walks
    all_walks.append(random_walk)

# Imprimir todas las caminatas
print(all_walks)

# Explicación del código:
# 1. Se utiliza `np.random.seed(123)` para garantizar resultados reproducibles.
# 2. La lista `all_walks` almacena todas las caminatas simuladas.
# 3. El bucle externo (`for i in range(5)`) simula 5 caminatas aleatorias.
# 4. El bucle interno construye cada caminata de 100 pasos basándose en los lanzamientos del dado.
# 5. El valor `max(0, step - 1)` evita que los pasos sean negativos.
# 6. Al final de cada caminata, se agrega la lista `random_walk` a `all_walks`.