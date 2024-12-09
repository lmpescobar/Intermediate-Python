# Ejercicio
# Uso del bucle `for` para iterar sobre listas y otros elementos iterables.

# Descripción:
# Este ejercicio muestra cómo usar el bucle `for` en diferentes escenarios:
# - Iterar sobre los elementos de una lista.
# - Usar `enumerate()` para obtener índices y valores.
# - Iterar sobre una cadena de texto.

# Código en Python

# Parte 1: Iterar sobre una lista
fam = [1.73, 1.68, 1.71, 1.89]  # Lista con las alturas de una familia en metros

# Imprimir cada elemento de la lista
print("Iteración sobre una lista:")
for height in fam:
    print(height)  # Imprime cada altura de la lista

# Parte 2: Usar `enumerate()` para obtener índice y valor
print("\nIteración con índices:")
for index, height in enumerate(fam):
    print(f"Índice {index}: Altura {height}")  # Muestra el índice y el valor

# Parte 3: Iterar sobre una cadena de texto
word = "family"  # Cadena de texto

print("\nIteración sobre una cadena:")
for c in word:
    print(c.capitalize())  # Imprime cada carácter en mayúscula

# Explicación:
# 1. **Iteración sobre listas:** El bucle `for` permite recorrer cada elemento de la lista `fam`.
# 2. **Uso de `enumerate`:** Este método devuelve tanto el índice como el valor, útil cuando necesitas ambas cosas.
# 3. **Iteración sobre cadenas:** Una cadena es un iterable, por lo que puedes recorrer cada carácter como si fuera una lista.

# Resultado esperado:
# - Parte 1:
#   1.73
#   1.68
#   1.71
#   1.89
#
# - Parte 2:
#   Índice 0: Altura 1.73
#   Índice 1: Altura 1.68
#   Índice 2: Altura 1.71
#   Índice 3: Altura 1.89
#
# - Parte 3:
#   F
#   A
#   M
#   I
#   L
#   Y