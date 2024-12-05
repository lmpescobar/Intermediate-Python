# Ejercicio
# Comparaciones mayores y menores en Python.

# Descripción
# En este ejercicio se practican los operadores de comparación en Python:
# "<", ">", "<=", ">=". Además, se explora cómo Python evalúa comparaciones
# con diferentes tipos de datos como enteros, cadenas y booleanos.

# Instrucciones
# 1. Escribe expresiones en Python dentro de una función print() para verificar si:
#    - `x` es mayor o igual que -10 (donde x ya ha sido definido).
#    - `"test"` es menor o igual a `y` (donde y ya ha sido definido).
#    - `True` es mayor que `False`.

# Código en Python
# Definimos la variable x como el producto de -3 y 6.
x = -3 * 6  # Resultado: -18

# Definimos la variable y como la cadena "test".
y = "test"

# 1. Verificamos si x es mayor o igual que -10.
# La comparación evalúa si el valor de x (-18) es mayor o igual que -10.
print(x >= -10)  # False porque -18 no es mayor ni igual a -10.

# 2. Verificamos si la cadena "test" es menor o igual que y.
# Aquí, Python evalúa cadenas en orden alfabético. "test" es igual a y.
print("test" <= y)  # True porque "test" es igual a y.

# 3. Verificamos si True es mayor que False.
# En Python, los booleanos se representan como enteros: False = 0, True = 1.
print(True > False)  # True porque 1 es mayor que 0.

# Explicaciones detalladas:
# - Línea 1: Se define x como el resultado de -3 multiplicado por 6.
#   Esto asigna a x el valor -18.
# - Línea 4: Se define y como la cadena "test".
# - Línea 7: Se usa el operador >= para comparar si x (-18) es mayor o igual a -10.
#   La salida es False porque -18 es menor que -10.
# - Línea 10: Se usa el operador <= para comparar si "test" es menor o igual a y ("test").
#   En las comparaciones de cadenas, "test" es igual a y, así que el resultado es True.
# - Línea 13: Se usa el operador > para comparar True y False. Como True equivale a 1
#   y False equivale a 0, el resultado es True.

# Impresiones esperadas:
# False
# True
# True