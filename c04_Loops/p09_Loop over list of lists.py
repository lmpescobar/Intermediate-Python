# Ejercicio
# Iterar sobre una lista de listas usando un bucle `for`

# Descripción:
# Este ejercicio utiliza un bucle `for` para recorrer una lista de listas (`house`),
# donde cada sublista contiene el nombre y el área de una habitación.
# El objetivo es imprimir un mensaje para cada habitación con su nombre y área.

# Código en Python

# Lista `house` que contiene sublistas con el nombre y el área de las habitaciones
house = [
    ["hallway", 11.25],
    ["kitchen", 18.0],
    ["Living room", 20.0],
    ["bedroom", 10.75],
    ["bathroom", 9.50]
]

# Bucle `for` para iterar sobre cada sublista de `house`
print("Información de las habitaciones:")
for room in house:
    # `room[0]` contiene el nombre de la habitación
    # `room[1]` contiene el área de la habitación
    print(f"The {room[0]} is {room[1]} sqm")

# Explicación:
# 1. **Lista inicial:** `house` contiene sublistas con el formato [nombre, área].
# 2. **Bucle `for`:**
#    - En cada iteración, `room` toma el valor de una sublista de `house`.
#    - `room[0]` accede al nombre de la habitación.
#    - `room[1]` accede al área de la habitación.
# 3. **Impresión:** En cada iteración, se imprime un mensaje formateado con el nombre y el área.

# Resultado esperado:
# Al ejecutar este código, se imprimirá:
# The hallway is 11.25 sqm
# The kitchen is 18.0 sqm
# The Living room is 20.0 sqm
# The bedroom is 10.75 sqm
# The bathroom is 9.5 sqm

# Nota:
# - Este enfoque usa un bucle `for` para manejar estructuras de datos más complejas,
#   como listas de listas.
# - Las f-strings (`f"The {room[0]} is {room[1]} sqm"`) simplifican la creación de mensajes formateados.