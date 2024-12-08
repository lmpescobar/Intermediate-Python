# Ejercicio
# Uso de operadores booleanos (and, or, not) en Python

# Descripción del ejercicio:
# Este ejercicio evalúa el conocimiento sobre la prioridad y evaluación
# de los operadores booleanos `and`, `or` y `not`. El código dado utiliza
# estas operaciones lógicas para calcular una expresión booleana compuesta.

# Instrucciones:
# 1. Analizar la expresión booleana paso a paso para entender su resultado.
# 2. Recordar que `not` tiene mayor prioridad que `and` y `or`.
# 3. Determinar el resultado del código proporcionado.

# Código en Python
# Variables iniciales
x = 8  # Se asigna el valor 8 a la variable x
y = 9  # Se asigna el valor 9 a la variable y

# Evaluación de la expresión booleana
resultado = not(not(x < 3) and not(y > 14 or y > 10))

# Impresión del resultado final
print(resultado)  # Esto imprimirá True o False según la evaluación.

# Explicación del código:
# 1. Se evalúa `x < 3`, lo que resulta en False (porque 8 no es menor que 3).
# 2. Se aplica `not` a `False`, lo que lo convierte en True.
# 3. Se evalúa `(y > 14 or y > 10)`:
#    - `y > 14` es False (9 no es mayor que 14).
#    - `y > 10` es False (9 no es mayor que 10).
#    - El resultado de la expresión completa es False.
# 4. Se aplica `not` a la expresión anterior, convirtiéndola en True.
# 5. Ahora se evalúa la conjunción `True and True`, que da True.
# 6. Finalmente, se aplica el `not` externo, convirtiendo True en False.
# El resultado final de la expresión booleana es False.