# Ejercicio
# Usar `enumerate()` para obtener índices y valores de una lista

# Descripción:
# Este ejercicio utiliza un bucle `for` con `enumerate()` para iterar sobre una lista.
# Además, en cada iteración, se imprime tanto el índice como el valor correspondiente.

# Código en Python

# Lista `areas` que contiene el área de varias habitaciones
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Bucle `for` con `enumerate()` para obtener índice y valor
print("Áreas de las habitaciones:")
for index, area in enumerate(areas):
    # Imprimir el índice y el área en el formato solicitado
    print(f"room {index}: {area}")

# Explicación:
# 1. **Lista inicial:** `areas` contiene los valores de área de diferentes habitaciones.
# 2. **Uso de `enumerate()`:**
#    - `enumerate(areas)` genera pares de valores `(índice, valor)` para cada elemento de la lista.
#    - `index` almacena el índice del elemento actual.
#    - `area` almacena el valor del área correspondiente.
# 3. **Impresión:** En cada iteración, se imprime el índice y el valor del área en el formato `room x: y`.

# Resultado esperado:
# Al ejecutar este código, se imprimirá:
# room 0: 11.25
# room 1: 18.0
# room 2: 20.0
# room 3: 10.75
# room 4: 9.5

# Nota:
# - `enumerate()` es útil cuando necesitas trabajar con los índices y los valores al mismo tiempo.
# - La función `f"room {index}: {area}"` utiliza una cadena formateada (f-string) para generar el texto.