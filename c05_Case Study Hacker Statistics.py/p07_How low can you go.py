# Ejercicio: How low can you go?
# Descripción:
# Asegurar que el camino aleatorio no descienda por debajo de 0 utilizando `max()`. 
# Esto es importante para evitar valores negativos en el recorrido.

# Código en Python:

# Importar NumPy y establecer la semilla
import numpy as np
np.random.seed(123)

# Inicializar el camino aleatorio con el primer paso
random_walk = [0]

# Bucle para simular 100 pasos
for x in range(100):  # Iterar 100 veces
    # Obtener el último paso como punto de partida
    step = random_walk[-1]

    # Lanzar el dado
    dice = np.random.randint(1, 7)

    # Determinar el siguiente paso
    if dice <= 2:  # Retroceder un paso, asegurándose de no bajar de 0
        step = max(0, step - 1)
    elif dice <= 5:  # Avanzar un paso
        step = step + 1
    else:  # Avanzar un número aleatorio de pasos
        step = step + np.random.randint(1, 7)

    # Agregar el nuevo paso a la lista
    random_walk.append(step)

# Imprimir el camino aleatorio generado
print("Camino aleatorio generado:", random_walk)

# Explicación del código:
# 1. `max(0, step - 1)`: Asegura que el valor de `step` nunca sea menor que 0.
#    - Si `step - 1` es negativo, `max()` devolverá 0.
#    - Si `step - 1` es positivo, se mantendrá ese valor.
# 2. El resto del código es similar al ejercicio anterior, pero ahora garantiza
#    que `step` no puede bajar por debajo de 0.
# 3. `random_walk.append(step)`: Almacena cada paso calculado en la lista `random_walk`.