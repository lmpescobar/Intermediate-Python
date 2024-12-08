# Ejercicio
# Uso de un bucle `while` para realizar cálculos repetitivos

# Descripción:
# Este código utiliza un bucle `while` para reducir un valor de error inicial,
# simulando un proceso iterativo. El bucle continúa ejecutándose hasta que
# el valor del error sea menor o igual a 1.

# Código en Python

# Paso 1: Inicializar la variable `error` con un valor inicial
error = 50.0  # El error comienza con un valor de 50

# Paso 2: Ciclo `while`
# La condición indica que el bucle continuará mientras `error` sea mayor que 1
while error > 1:
    # Reducir el valor del error dividiéndolo por 4
    error = error / 4
    
    # Imprimir el valor actual del error en cada iteración
    print(error)

# Explicación:
# 1. **Valor inicial:** El error comienza en 50.0.
# 2. **Condición del bucle:** Mientras el error sea mayor que 1, se ejecutará el bucle.
# 3. **Actualización:** En cada iteración, el error se reduce dividiéndolo por 4.
# 4. **Impresión:** El valor actual del error se muestra en cada paso.
# 5. **Finalización:** El bucle se detiene cuando el error es menor o igual a 1.

# Ejemplo de ejecución:
# - Iteración 1: error = 50 / 4 = 12.5
# - Iteración 2: error = 12.5 / 4 = 3.125
# - Iteración 3: error = 3.125 / 4 = 0.78125 (el bucle termina aquí)

# Nota:
# Si no se actualiza el valor de `error` dentro del bucle, se creará un bucle
# infinito. En ese caso, puedes detener la ejecución con `Ctrl + C` en tu consola.