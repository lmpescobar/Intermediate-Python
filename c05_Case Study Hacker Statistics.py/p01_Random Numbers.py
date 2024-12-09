# Ejercicio: Caminata Aleatoria en el Empire State Building
# Este código simula un juego de 100 tiradas de dado para calcular la probabilidad de alcanzar 60 pasos.

# Instrucciones:
# 1. Importar las bibliotecas necesarias.
# 2. Configurar un generador de números pseudoaleatorios.
# 3. Implementar la lógica del juego, incluyendo las reglas y la condición de caída.
# 4. Repetir la simulación múltiples veces para estimar la probabilidad.

import numpy as np

# Configurar la semilla para garantizar reproducibilidad
np.random.seed(123)

# Definir el número de simulaciones
num_simulaciones = 10000

# Lista para registrar los resultados
resultados = []

# Simular múltiples caminatas
for _ in range(num_simulaciones):
    pasos = 0  # Iniciar en el paso 0
    for _ in range(100):  # 100 lanzamientos de dado
        dado = np.random.randint(1, 7)  # Lanzar un dado de 6 caras
        if dado <= 2:
            pasos = max(0, pasos - 1)  # No bajar de 0
        elif dado <= 5:
            pasos += 1
        else:  # dado == 6
            pasos += np.random.randint(1, 7)
        
        # Probabilidad de caer
        if np.random.rand() < 0.001:
            pasos = 0  # Reiniciar a 0

    # Guardar el resultado de esta caminata
    resultados.append(pasos >= 60)

# Calcular la probabilidad de ganar la apuesta
probabilidad_ganar = sum(resultados) / num_simulaciones

# Imprimir el resultado
print(f"Probabilidad de alcanzar 60 pasos: {probabilidad_ganar:.4f}")