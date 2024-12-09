# Ejercicio: Generación de un número flotante aleatorio reproducible

# Descripción:
# En este ejercicio se utiliza NumPy para generar un número flotante aleatorio.
# Se utiliza una semilla para asegurar que los resultados sean reproducibles entre simulaciones.

# Instrucciones:
# 1. Importar el paquete numpy bajo el alias `np`.
# 2. Configurar la semilla con `np.random.seed()`, pasando como argumento el número 123.
# 3. Generar un número flotante aleatorio entre 0 y 1 con `np.random.rand()`.
# 4. Imprimir el número generado para verificar el resultado.

# Código en Python

# Importar el paquete numpy con el alias `np`
import numpy as np

# Establecer la semilla de aleatoriedad para reproducibilidad
np.random.seed(123)

# Generar un número flotante aleatorio entre 0 y 1
random_float = np.random.rand()

# Imprimir el número flotante generado
print(f"Número flotante aleatorio generado: {random_float}")

# Explicación del código:
# - `np.random.seed(123)`: Asegura que la secuencia de números aleatorios generados será siempre la misma.
# - `np.random.rand()`: Genera un número flotante entre 0 y 1.
# - El resultado se imprime para verificar que el código funciona correctamente.