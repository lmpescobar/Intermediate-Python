# Ejercicio: Determinar el próximo movimiento en la apuesta del Empire State Building

# Descripción:
# En este ejercicio, simularemos el lanzamiento de un dado para determinar el siguiente
# movimiento en una apuesta. Dependiendo del número obtenido, se decidirá si se avanza,
# retrocede o se lanzará nuevamente para calcular los pasos a subir.

# Instrucciones:
# 1. Lanzar el dado usando `np.random.randint(1, 7)` y asignarlo a la variable `dice`.
# 2. Usar una estructura `if-elif-else` para determinar:
#    - Si `dice` es 1 o 2, retroceder un paso.
#    - Si `dice` es 3, 4 o 5, avanzar un paso.
#    - Si `dice` es 6, lanzar el dado nuevamente y avanzar ese número de pasos.
# 3. Imprimir el valor de `dice` y la posición actual (`step`).

# Importar numpy y configurar la semilla
import numpy as np
np.random.seed(123)

# Posición inicial
step = 50

# Lanzar el dado
dice = np.random.randint(1, 7)

# Determinar el movimiento según el valor del dado
if dice <= 2:
    # Si el dado muestra 1 o 2, retrocede un paso
    step -= 1
elif dice <= 5:
    # Si el dado muestra 3, 4 o 5, avanza un paso
    step += 1
else:
    # Si el dado muestra 6, lanza nuevamente y avanza ese número de pasos
    step += np.random.randint(1, 7)

# Imprimir el valor del dado y la posición actual
print(f"Dado: {dice}")
print(f"Paso actual: {step}")

# Explicación del código:
# - `dice = np.random.randint(1, 7)`: Simula el lanzamiento de un dado, generando un número entero entre 1 y 6.
# - `if dice <= 2`: Si el valor del dado es 1 o 2, disminuye el paso (`step`).
# - `elif dice <= 5`: Si el valor del dado es 3, 4 o 5, incrementa el paso.
# - `else`: Si el valor del dado es 6, lanza nuevamente el dado y suma el nuevo valor al paso.
# - Finalmente, se imprimen el valor del dado y la posición actual (`step`).

# Resultado esperado:
# Un valor del dado (entre 1 y 6) y una posición actual que refleja el movimiento determinado.