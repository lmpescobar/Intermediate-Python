# Ejercicio
# Uso de estructuras `if-else` en Python.

# Descripción:
# Este ejercicio amplía el uso de `if` añadiendo bloques `else` para manejar
# los casos donde las condiciones no se cumplen.

# Código en Python
# Definir las variables
room = "kit"  # Indica que estamos observando la cocina
area = 14.0   # El área de la habitación

# Estructura `if-else` para la variable `room`
if room == "kit":  # Si `room` es igual a "kit" (kitchen)
    print("Looking around in the kitchen.")  # Imprime un mensaje indicando la habitación
else:  # Si `room` no es igual a "kit"
    print("Looking around elsewhere.")  # Imprime un mensaje indicando otra habitación

# Estructura `if-else` para la variable `area`
if area > 15:  # Si el área es mayor que 15
    print("Big place!")  # Imprime un mensaje indicando que el lugar es grande
else:  # Si el área no es mayor que 15
    print("Pretty small.")  # Imprime un mensaje indicando que el lugar es pequeño

# Explicación:
# - En este caso, `room` es igual a "kit", por lo que se ejecuta el bloque `if` de la primera estructura.
#   Esto imprime: "Looking around in the kitchen."
# - Para `area`, el valor es 14.0, por lo que la condición `area > 15` es falsa,
#   y se ejecuta el bloque `else`, imprimiendo: "Pretty small."