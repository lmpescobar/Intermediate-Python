# Ejercicio: Random Walk
# Descripción del ejercicio:
# Simularemos un "Random Walk" (camino aleatorio) utilizando lanzamientos de una moneda.
# Cada lanzamiento determinará si avanzamos, retrocedemos o mantenemos nuestra posición
# en el camino. Este concepto es ampliamente usado en ciencias, finanzas y modelado de procesos aleatorios.

# Instrucciones:
# 1. Usa numpy para generar números aleatorios y simular lanzamientos de una moneda.
# 2. Crea una lista inicial con el valor 0 para representar el punto de inicio del camino.
# 3. Utiliza un bucle `for` para generar 10 pasos aleatorios.
#    - Si el lanzamiento de la moneda es cara (0), mantén la posición.
#    - Si el lanzamiento de la moneda es cruz (1), incrementa el valor del último paso.
#    - Registra cada posición en la lista.
# 4. Imprime la lista al final para observar el camino generado.

# Código en Python:

# Importar el paquete numpy
import numpy as np

# Establecer la semilla para reproducibilidad
np.random.seed(123)

# Lista para almacenar los pasos del camino aleatorio, comenzando desde 0
random_walk = [0]

# Bucle para simular 10 pasos del camino aleatorio
for i in range(10):
    # Generar un número aleatorio (0 o 1) para simular el lanzamiento de la moneda
    coin = np.random.randint(0, 2)
    
    # Determinar el siguiente paso en función del resultado del lanzamiento
    if coin == 0:  # Cara: Mantener la posición actual
        random_walk.append(random_walk[-1])
    else:  # Cruz: Avanzar un paso
        random_walk.append(random_walk[-1] + 1)

# Imprimir el camino generado
print("Camino aleatorio:", random_walk)

# Explicación del código:
# 1. `np.random.seed(123)`: Fija la semilla del generador de números aleatorios para
#    asegurar que los resultados sean reproducibles.
# 2. `random_walk = [0]`: Inicia el camino en el paso 0.
# 3. `for i in range(10)`: Repite el proceso 10 veces para simular 10 pasos.
# 4. `coin = np.random.randint(0, 2)`: Genera un número aleatorio (0 o 1) para simular
#    el lanzamiento de la moneda.
# 5. `random_walk.append(random_walk[-1])`: Si es cara (0), el valor se mantiene.
# 6. `random_walk.append(random_walk[-1] + 1)`: Si es cruz (1), avanza un paso.
# 7. `print(random_walk)`: Muestra la lista completa del camino aleatorio generado.