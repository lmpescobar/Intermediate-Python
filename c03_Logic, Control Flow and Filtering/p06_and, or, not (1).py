# Ejercicio
# Uso de operadores booleanos: and, or, not.

# Descripción
# En este ejercicio se utilizan operadores booleanos para realizar 
# comparaciones con las áreas de dos cocinas representadas por 
# las variables `my_kitchen` y `your_kitchen`.

# Instrucciones
# 1. Verifica si el área de `my_kitchen` es mayor que 10 y menor que 18.
# 2. Verifica si el área de `my_kitchen` es menor que 14 o mayor que 17.
# 3. Verifica si el doble del área de `my_kitchen` es menor que el triple del área de `your_kitchen`.

# Código en Python
# Definir las variables con las áreas de las cocinas.
my_kitchen = 18.0  # Área de mi cocina en metros cuadrados.
your_kitchen = 14.0  # Área de tu cocina en metros cuadrados.

# 1. Verificar si `my_kitchen` es mayor que 10 y menor que 18.
# Ambas condiciones deben ser True para que la expresión completa sea True.
print(my_kitchen > 10 and my_kitchen < 18)
# Resultado esperado: False, porque aunque es mayor que 10, no es menor que 18.

# 2. Verificar si `my_kitchen` es menor que 14 o mayor que 17.
# Al menos una de las condiciones debe ser True para que la expresión sea True.
print(my_kitchen < 14 or my_kitchen > 17)
# Resultado esperado: True, porque `my_kitchen` (18.0) es mayor que 17.

# 3. Verificar si el doble de `my_kitchen` es menor que el triple de `your_kitchen`.
# Se realiza la comparación aritmética y lógica en una sola línea.
print(2 * my_kitchen < 3 * your_kitchen)
# Resultado esperado: False, porque 2 * 18 = 36 no es menor que 3 * 14 = 42.

# Explicaciones detalladas:
# - Línea 9: Se define `my_kitchen` con un valor flotante de 18.0.
# - Línea 10: Se define `your_kitchen` con un valor flotante de 14.0.
# - Línea 13: Se usa `and` para comprobar si `my_kitchen` está entre 10 y 18.
#   La salida es False porque una de las condiciones no se cumple.
# - Línea 16: Se usa `or` para comprobar si `my_kitchen` es menor que 14 o mayor que 17.
#   La salida es True porque una de las condiciones se cumple.
# - Línea 19: Se realiza una operación aritmética antes de comparar el doble de `my_kitchen`
#   con el triple de `your_kitchen`. La salida es False porque 36 no es menor que 42.

# Resultados esperados:
# False
# True
# False