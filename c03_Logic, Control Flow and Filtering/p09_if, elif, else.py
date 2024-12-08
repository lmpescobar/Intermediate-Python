# Ejercicio
# Uso de control de flujo en Python: if, elif y else

# Descripción:
# Este ejercicio explica cómo usar las estructuras de control en Python.
# Incluye ejemplos con la declaración `if`, `else` y `elif` para cambiar
# el flujo del programa según condiciones específicas.

# Código en Python

# Ejemplo 1: Usando `if`
z = 4  # Variable inicial
if z % 2 == 0:  # Verificar si `z` es divisible por 2
    print("z es par")  # Este mensaje se imprime si la condición es True

# Ejemplo 2: Usando `if` con múltiples expresiones
z = 4  # Redefiniendo la variable
if z % 2 == 0:  # Verificar si `z` es divisible por 2
    print(f"Verificando {z}")  # Línea adicional dentro del bloque `if`
    print("z es par")  # Este mensaje se imprime si la condición es True

# Ejemplo 3: Usando `else`
z = 5  # Redefiniendo la variable
if z % 2 == 0:  # Verificar si `z` es divisible por 2
    print("z es par")
else:
    print("z es impar")  # Este mensaje se imprime si la condición es False

# Ejemplo 4: Usando `elif`
z = 3  # Redefiniendo la variable
if z % 2 == 0:  # Verificar si `z` es divisible por 2
    print("z es divisible por 2")
elif z % 3 == 0:  # Verificar si `z` es divisible por 3
    print("z es divisible por 3")
else:
    print("z no es divisible ni por 2 ni por 3")

# Ejemplo 5: Priorización de condiciones con `if` y `elif`
z = 6  # Redefiniendo la variable
if z % 2 == 0:  # Verificar si `z` es divisible por 2
    print("z es divisible por 2")
elif z % 3 == 0:  # Verificar si `z` es divisible por 3
    print("z es divisible por 3")  # Nunca se ejecuta porque la primera condición es True
else:
    print("z no es divisible ni por 2 ni por 3")

# Explicación:
# - En el primer ejemplo, solo se imprime si la condición `z % 2 == 0` es verdadera.
# - El segundo ejemplo incluye varias líneas dentro del bloque `if`.
# - El tercer ejemplo utiliza un bloque `else` para manejar el caso donde la condición es falsa.
# - En el cuarto ejemplo, el uso de `elif` permite manejar múltiples condiciones.
# - En el quinto ejemplo, se muestra que Python evalúa las condiciones de arriba hacia abajo,
#   deteniéndose en la primera condición verdadera.