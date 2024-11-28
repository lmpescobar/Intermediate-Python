# Igualdad en Python
# En Python, puedes verificar si dos valores o variables son iguales usando el operador de igualdad (==).
# Para verificar si son diferentes, utilizas el operador de desigualdad (!=).

# Ejemplos de comparación de igualdad y desigualdad:
# Estos ejemplos verifican la igualdad y desigualdad entre diferentes tipos de valores.

# Ejemplo 1: Verificar si 2 es igual a (1 + 1)
print(2 == (1 + 1))  # Resultado: True, porque 1 + 1 es igual a 2.

# Ejemplo 2: Verificar si la cadena "intermediate" es diferente de "python"
print("intermediate" != "python")  # Resultado: True, porque ambas cadenas son diferentes.

# Ejemplo 3: Verificar si True es diferente de False
print(True != False)  # Resultado: True, porque True y False son valores booleanos opuestos.

# Ejemplo 4: Verificar si "Python" es diferente de "python"
print("Python" != "python")  # Resultado: True, porque Python distingue entre mayúsculas y minúsculas.

# Instrucciones del ejercicio:
# A continuación, realizamos las verificaciones solicitadas.

# 1. Verificar si True es igual a False
print(True == False)  # Resultado: False, porque True y False no son iguales.

# 2. Verificar si -5 * 15 no es igual a 75
# Se realiza una operación aritmética (-5 * 15) y se verifica si el resultado es diferente a 75.
print((-5 * 15) != 75)  # Resultado: True, porque -75 no es igual a 75.

# 3. Verificar si las cadenas "pyscript" y "PyScript" son iguales
# Comparación entre cadenas que distingue mayúsculas y minúsculas.
print("pyscript" == "PyScript")  # Resultado: False, porque las cadenas no coinciden debido a la diferencia en mayúsculas.

# 4. Comparar booleanos con enteros: Verificar si True es igual a 1
# En Python, True se representa como 1 y False como 0, por lo que esta comparación devuelve True.
print(True == 1)  # Resultado: True, porque True y 1 son equivalentes en Python.

# Conclusión:
# 1. El operador == verifica si dos valores son iguales, devolviendo True si lo son.
# 2. El operador != verifica si dos valores son diferentes, devolviendo True si no son iguales.
# 3. Python distingue entre mayúsculas y minúsculas al comparar cadenas.
# 4. Booleanos y enteros pueden compararse, ya que True equivale a 1 y False equivale a 0.