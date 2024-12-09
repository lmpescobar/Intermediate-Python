# Ejercicio: Simular el lanzamiento de un dado

# Descripción:
# En este ejercicio se simula el lanzamiento de un dado utilizando la función `randint()` 
# del paquete `numpy.random`. Esto genera enteros aleatorios dentro de un rango definido.
# Se configuró una semilla previamente para asegurar la reproducibilidad de los resultados.

# Instrucciones:
# 1. Usar `np.random.randint()` para generar un número entero aleatorio entre 1 y 6.
# 2. Imprimir el resultado del primer lanzamiento.
# 3. Repetir el procedimiento para un segundo lanzamiento y también imprimir el resultado.

# Importar el paquete numpy y configurar la semilla
import numpy as np
np.random.seed(123)

# Lanzar el dado por primera vez (genera un número entre 1 y 6)
dice_roll_1 = np.random.randint(1, 7)  # El rango es [1, 7), por lo que 7 no está incluido
print(f"Primer lanzamiento del dado: {dice_roll_1}")

# Lanzar el dado por segunda vez (genera un número entre 1 y 6)
dice_roll_2 = np.random.randint(1, 7)  # Genera un nuevo número aleatorio en el mismo rango
print(f"Segundo lanzamiento del dado: {dice_roll_2}")

# Explicación del código:
# - `np.random.seed(123)`: Configura la semilla para que los resultados sean reproducibles.
# - `np.random.randint(1, 7)`: Genera un número entero aleatorio entre 1 y 6 (incluidos).
# - Los dos resultados se imprimen para observar cómo varían los lanzamientos.