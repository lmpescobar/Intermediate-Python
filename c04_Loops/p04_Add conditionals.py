# Ejercicio
# Añadir condicionales dentro de un ciclo `while` para manejar valores positivos y negativos

# Descripción:
# Este ejercicio corrige un bucle infinito que ocurre cuando `offset` es negativo.
# Se utiliza un ciclo `while` con una estructura `if-else` para ajustar correctamente
# el valor de `offset` hacia 0, sin importar si comienza como un número positivo o negativo.

# Código en Python

# Inicializar la variable `offset` con un valor inicial negativo
offset = -6

# Ciclo `while` que se ejecuta mientras `offset` no sea igual a 0
while offset != 0:
    # Imprimir un mensaje indicando que se está corrigiendo el offset
    print("correcting...")
    
    # Condicional para ajustar el valor de `offset`
    if offset > 0:
        # Si `offset` es positivo, reducir su valor en 1
        offset = offset - 1
    else:
        # Si `offset` es negativo, aumentar su valor en 1
        offset = offset + 1
    
    # Imprimir el valor actual de `offset` para observar los cambios
    print(f"Offset: {offset}")

# Explicación:
# 1. **Inicialización:** `offset` comienza con un valor de -6 (negativo).
# 2. **Condición del ciclo:** El bucle se ejecuta mientras `offset` no sea igual a 0.
# 3. **Cuerpo del ciclo:**
#    - Si `offset > 0`, se reduce su valor en 1.
#    - Si `offset <= 0`, se aumenta su valor en 1.
#    - Esto asegura que `offset` siempre se acerque a 0.
# 4. **Finalización:** El ciclo termina cuando `offset` es igual a 0, lo que hace que la condición del `while` sea falsa.

# Resultado esperado:
# La consola imprimirá:
# correcting...
# Offset: -5
# correcting...
# Offset: -4
# ...
# correcting...
# Offset: 0

# Nota:
# - Si no se utiliza la estructura `if-else`, es posible que el ciclo se vuelva infinito,
#   ya que `offset` podría alejarse de 0 en lugar de acercarse.
# - Este enfoque garantiza que el valor de `offset` siempre converge hacia 0.