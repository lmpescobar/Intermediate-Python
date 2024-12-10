# Ejercicio: Random Walk - The Next Step
# Descripción:
# Extender el código anterior para simular un camino aleatorio (random walk) 
# utilizando un bucle `for` para realizar 100 iteraciones.
# En cada iteración, se lanza un dado y se determina el siguiente paso 
# en función de las reglas dadas.

# Instrucciones:
# 1. Inicializa una lista `random_walk` que contenga el primer paso como el número entero 0.
# 2. Completa el bucle `for` para iterar 100 veces:
#    a) Calcula `step` como el último elemento de `random_walk`.
#    b) Lanza un dado con `np.random.randint(1, 7)`.
#    c) Determina el siguiente paso usando un condicional:
#       - Si el dado es 1 o 2, retrocede un paso.
#       - Si el dado es 3, 4 o 5, avanza un paso.
#       - Si el dado es 6, avanza un número aleatorio de pasos adicionales.
#    d) Asegúrate de que `step` no sea menor que 0.
#    e) Agrega el nuevo paso a `random_walk`.
# 3. Imprime la lista completa al final.

# Código en Python:

# Importar NumPy y establecer la semilla
import numpy as np
np.random.seed(123)

# Inicializar el camino aleatorio con el primer paso
random_walk = [0]

# Completar el bucle para generar 100 pasos
for x in range(100):  # Iterar 100 veces
    # Obtener el último paso como punto de partida
    step = random_walk[-1]

    # Lanzar el dado
    dice = np.random.randint(1, 7)

    # Determinar el siguiente paso
    if dice <= 2:  # Retroceder un paso
        step = step - 1
    elif dice <= 5:  # Avanzar un paso
        step = step + 1
    else:  # Avanzar un número aleatorio de pasos
        step = step + np.random.randint(1, 7)

    # Asegurarse de que el paso no sea menor que 0
    if step < 0:
        step = 0

    # Agregar el nuevo paso a la lista
    random_walk.append(step)

# Imprimir el camino aleatorio generado
print("Camino aleatorio generado:", random_walk)

# Explicación del código:
# 1. `random_walk = [0]`: La lista comienza con el paso inicial en 0.
# 2. `for x in range(100)`: Realiza 100 iteraciones, simulando 100 lanzamientos de dado.
# 3. `step = random_walk[-1]`: Obtiene el último paso registrado como punto de partida.
# 4. `dice = np.random.randint(1, 7)`: Lanza un dado generando un número entre 1 y 6.
# 5. `if dice <= 2`: Retrocede un paso.
# 6. `elif dice <= 5`: Avanza un paso.
# 7. `else`: Avanza un número aleatorio de pasos adicionales.
# 8. `if step < 0`: Asegura que `step` nunca sea negativo.
# 9. `random_walk.append(step)`: Agrega el paso calculado a la lista del camino.