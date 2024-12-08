# Ejercicio
# Uso de condicionales `if` en Python.

# Descripción:
# Este ejercicio trabaja con dos variables:
# - `room`: Una cadena de texto que indica la habitación de la casa que estamos observando.
# - `area`: Un número que representa el área de esa habitación.
# Se deben escribir declaraciones `if` para realizar acciones basadas en estas variables.

# Código en Python
# Definir las variables
room = "kit"  # Indica que estamos observando la cocina
area = 14.0   # El área de la habitación

# Declaración `if` para la variable `room`
if room == "kit":  # Si `room` es igual a "kit" (kitchen)
    print("Looking around in the kitchen.")  # Imprime un mensaje indicando la habitación

# Declaración `if` para la variable `area`
if area > 15:  # Si el área es mayor que 15
    print("Big place!")  # Imprime un mensaje indicando que el lugar es grande

# Explicación:
# - En este caso, `room` es igual a "kit", por lo que se ejecuta el primer bloque `if` y se imprime:
#   "Looking around in the kitchen."
# - El valor de `area` es 14.0, por lo que la condición `area > 15` es falsa,
#   y el segundo bloque `if` no se ejecuta.