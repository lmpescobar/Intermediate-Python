# Ejercicio
# Ajustar los índices del bucle `for` para que comiencen desde 1

# Descripción:
# Este ejercicio utiliza un bucle `for` con `enumerate()` para iterar sobre una lista.
# Se ajusta el índice de las habitaciones para que comience desde 1 en lugar de 0.

# Código en Python

# Lista `areas` que contiene el área de varias habitaciones
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Bucle `for` con `enumerate()` para obtener índice y valor
print("Áreas de las habitaciones:")
for index, area in enumerate(areas, start=1):  # `start=1` hace que los índices comiencen desde 1
    print(f"room {index}: {area}")  # Imprimir el índice ajustado y el valor del área

# Explicación:
# 1. **Lista inicial:** `areas` contiene los valores de área de diferentes habitaciones.
# 2. **Uso de `enumerate(areas, start=1)`:**
#    - Por defecto, `enumerate()` comienza en 0.
#    - El argumento `start=1` indica que los índices deben comenzar desde 1.
# 3. **Impresión:** En cada iteración, se imprime el índice (ajustado) y el valor del área en el formato `room x: y`.

# Resultado esperado:
# Al ejecutar este código, se imprimirá:
# room 1: 11.25
# room 2: 18.0
# room 3: 20.0
# room 4: 10.75
# room 5: 9.5

# Nota:
# - `start=1` en `enumerate()` es útil para ajustar los índices y hacerlos más comprensibles para usuarios no programadores.
# - El uso de f-strings (`f"room {index}: {area}"`) facilita la creación de cadenas formateadas.