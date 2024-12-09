# Ejercicio
# Iterar sobre una lista con un bucle `for`

# Descripción:
# Este ejercicio utiliza un bucle `for` para recorrer e imprimir
# los elementos de una lista llamada `areas`, que representa el área de diferentes habitaciones.

# Código en Python

# Lista `areas` que contiene el área de varias habitaciones
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Bucle `for` para iterar sobre los elementos de la lista
print("Áreas de las habitaciones:")
for area in areas:
    print(area)  # Imprimir cada área

# Explicación:
# 1. **Lista inicial:** La lista `areas` contiene cinco valores flotantes, cada uno representando el área de una habitación.
# 2. **Estructura del bucle `for`:** 
#    - `area` es una variable temporal que toma el valor de cada elemento de `areas` en cada iteración.
#    - En cada iteración, el valor de `area` se imprime.
# 3. **Finalización:** El bucle termina automáticamente después de recorrer todos los elementos de la lista.

# Resultado esperado:
# Al ejecutar este código, se imprimirá:
# Áreas de las habitaciones:
# 11.25
# 18.0
# 20.0
# 10.75
# 9.5

# Nota:
# - El bucle `for` facilita iterar sobre cada elemento de una lista sin necesidad de usar índices.
# - Es importante usar la indentación correcta para el bloque de código dentro del bucle.