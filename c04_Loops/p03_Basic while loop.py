# Ejercicio
# Uso de un ciclo `while` para implementar un sistema básico de control

# Descripción:
# Este código simula un sistema de control básico para corregir un "offset" de un péndulo invertido.
# El ciclo `while` ajustará el valor de `offset` hasta que sea igual a 0.

# Código en Python

# Inicializar la variable `offset` con un valor inicial de 8
offset = 8

# Ciclo `while` que continúa ejecutándose mientras `offset` no sea igual a 0
while offset != 0:
    # Imprimir un mensaje indicando que se está corrigiendo el offset
    print("correcting...")
    
    # Reducir el valor de `offset` en 1
    offset = offset - 1
    
    # Imprimir el valor actual de `offset` para observar los cambios
    print(f"Offset: {offset}")

# Explicación:
# 1. **Inicialización:** Se define `offset` con un valor inicial de 8.
# 2. **Condición del ciclo:** Mientras `offset` no sea igual a 0, el ciclo continuará ejecutándose.
# 3. **Cuerpo del ciclo:**
#    - Se imprime "correcting..." para indicar que se está trabajando en la corrección.
#    - Se disminuye el valor de `offset` en 1.
#    - Se imprime el valor actualizado de `offset` para monitorear el progreso.
# 4. **Finalización:** Cuando `offset` llega a 0, la condición `offset != 0` se vuelve falsa y el ciclo se detiene.

# Resultado esperado:
# La consola imprimirá:
# correcting...
# Offset: 7
# correcting...
# Offset: 6
# ...
# correcting...
# Offset: 0

# Nota:
# - Este ejercicio ilustra cómo usar un ciclo `while` para repetir acciones hasta alcanzar una condición específica.
# - Asegúrate de no olvidar actualizar la variable `offset` dentro del ciclo para evitar bucles infinitos.