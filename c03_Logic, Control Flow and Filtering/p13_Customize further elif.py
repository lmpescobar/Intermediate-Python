# Ejercicio
# Uso de estructuras `if-elif-else` en Python.

# Descripción:
# Este ejercicio amplía las estructuras de control para manejar múltiples
# condiciones utilizando `elif`, añadiendo mayor personalización a los mensajes.

# Código en Python
# Definir las variables
room = "bed"  # Indica que estamos observando el dormitorio
area = 14.0   # El área de la habitación

# Estructura `if-elif-else` para la variable `room`
if room == "kit":  # Si `room` es igual a "kit" (kitchen)
    print("Looking around in the kitchen.")  # Mensaje indicando la cocina
elif room == "bed":  # Si `room` es igual a "bed" (bedroom)
    print("Looking around in the bedroom.")  # Mensaje indicando el dormitorio
else:  # Si `room` no es ni "kit" ni "bed"
    print("Looking around elsewhere.")  # Mensaje indicando otra habitación

# Estructura `if-elif-else` para la variable `area`
if area > 15:  # Si el área es mayor que 15
    print("Big place!")  # Mensaje indicando que el lugar es grande
elif area > 10:  # Si el área es mayor que 10 pero no mayor que 15
    print("Medium size, nice!")  # Mensaje indicando un tamaño mediano
else:  # Si el área no es mayor que 10
    print("Pretty small.")  # Mensaje indicando que el lugar es pequeño

# Explicación:
# - En la estructura para `room`, se evalúan las condiciones en orden:
#   Si `room` es "kit", se imprime el mensaje correspondiente.
#   Si no, pero `room` es "bed", se imprime otro mensaje.
#   Si ninguna de las dos condiciones se cumple, se imprime el mensaje del bloque `else`.
# - En la estructura para `area`, se añaden mensajes personalizados para áreas:
#   > 15 (grande), entre 10 y 15 (mediano) y ≤ 10 (pequeño).