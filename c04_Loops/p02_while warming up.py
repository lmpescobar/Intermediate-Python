# Ejercicio
# Uso del ciclo `while` para ejecutar un bloque de código repetidamente

# Descripción:
# Este código utiliza un ciclo `while` para imprimir valores de la variable `x`.
# El ciclo se ejecuta mientras `x` sea menor que 4, incrementando `x` en cada iteración.

# Código en Python

# Inicializar la variable `x`
x = 1  # Valor inicial de x

# Ciclo `while` que se ejecuta mientras la condición sea verdadera
while x < 4:  # El ciclo continuará mientras x sea menor que 4
    print(x)  # Imprimir el valor actual de x
    x = x + 1  # Incrementar el valor de x en 1

# Explicación:
# 1. **Inicialización:** La variable `x` se inicializa con el valor 1.
# 2. **Condición del ciclo:** El ciclo `while` se ejecuta mientras `x` sea menor que 4.
# 3. **Ejecución del cuerpo del ciclo:**
#    - Se imprime el valor actual de `x`.
#    - Se incrementa `x` en 1 para acercarse al final del ciclo.
# 4. **Finalización del ciclo:** Cuando `x` alcanza el valor 4, la condición `x < 4` se vuelve falsa y el ciclo termina.

# Resultado esperado:
# El programa imprimirá:
# 1
# 2
# 3

# Nota:
# - El ciclo `while` es útil cuando no sabes exactamente cuántas veces necesitas repetir el bloque de código,
#   pero tienes una condición que define cuándo debe detenerse.