# Ejercicio
# Iterar sobre un diccionario utilizando el método `.items()`

# Descripción:
# Este ejercicio utiliza un bucle `for` con el método `.items()` para recorrer un diccionario
# llamado `europe`, que contiene países como claves y sus capitales como valores.
# El objetivo es imprimir un mensaje que indique la capital de cada país.

# Código en Python

# Diccionario `europe` que contiene países y sus capitales
europe = {
    'spain': 'madrid',
    'france': 'paris',
    'germany': 'berlin',
    'norway': 'oslo',
    'italy': 'rome',
    'poland': 'warsaw',
    'austria': 'vienna'
}

# Bucle `for` para iterar sobre los pares clave-valor del diccionario
print("Capitales de Europa:")
for country, capital in europe.items():
    # Imprimir un mensaje con el nombre del país y su capital
    print(f"The capital of {country} is {capital}")

# Explicación:
# 1. **Diccionario inicial:** `europe` contiene claves (países) y valores (capitales).
# 2. **Uso de `.items()`:**
#    - El método `.items()` genera pares clave-valor del diccionario.
#    - En cada iteración, `country` almacena la clave (país) y `capital` almacena el valor (capital).
# 3. **Impresión:** Se utiliza un mensaje formateado con f-strings para mostrar la clave y el valor.

# Resultado esperado:
# Al ejecutar este código, se imprimirá:
# The capital of spain is madrid
# The capital of france is paris
# The capital of germany is berlin
# The capital of norway is oslo
# The capital of italy is rome
# The capital of poland is warsaw
# The capital of austria is vienna

# Nota:
# - Los diccionarios en Python son estructuras desordenadas, por lo que el orden
#   de los elementos puede variar (excepto en Python >= 3.7, donde se mantiene el orden de inserción).
# - Este enfoque permite trabajar fácilmente con claves y valores de un diccionario.