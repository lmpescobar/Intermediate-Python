# Ejercicio: Manipulación de diccionarios (Dictionary Manipulation 2)

# Descripción:
# En este ejercicio, trabajaremos con un diccionario que contiene algunos errores y datos irrelevantes. 
# El objetivo es corregir la capital de Alemania (Germany), eliminar datos incorrectos (Australia no está en Europa)
# y verificar el contenido actualizado del diccionario.

# Objetivo:
# - Actualizar el valor asociado a una clave existente.
# - Eliminar un par clave:valor del diccionario.
# - Imprimir el diccionario actualizado.

# Código en Python:

# Definición inicial del diccionario: países europeos y sus capitales.
europe = {
    'spain': 'madrid',
    'france': 'paris',
    'germany': 'bonn',       # Error: la capital de Alemania no es 'bonn'.
    'norway': 'oslo',
    'italy': 'rome',
    'poland': 'warsaw',
    'australia': 'vienna'    # Error: Australia no pertenece a Europa.
}

# 1. Actualizar la capital de Alemania (Germany).
# La capital correcta es 'berlin'.
europe['germany'] = 'berlin'

# 2. Eliminar la clave 'australia' y su valor asociado, ya que Australia no está en Europa.
del europe['australia']

# 3. Imprimir el diccionario actualizado para verificar los cambios.
print("Diccionario actualizado:", europe)

# Explicación detallada del código:

# 1. Actualización de un valor en el diccionario:
# - `europe['germany'] = 'berlin'`: Este comando actualiza el valor asociado a la clave 'germany'.
# - Como las claves en un diccionario son únicas, Python sobrescribe el valor anterior ('bonn') con el nuevo valor ('berlin').

# 2. Eliminación de un par clave:valor del diccionario:
# - `del europe['australia']`: Elimina la entrada completa para la clave 'australia' del diccionario.
# - Esto es útil para limpiar datos irrelevantes o incorrectos.

# 3. Impresión del diccionario actualizado:
# - `print("Diccionario actualizado:", europe)`: Muestra el contenido del diccionario después de realizar las modificaciones.
# - Esto asegura que las actualizaciones y eliminaciones se realizaron correctamente.

# Reflexión:
# - Actualizar y eliminar elementos en un diccionario es directo y eficiente.
# - Los diccionarios son estructuras ideales para almacenar datos relacionados de forma estructurada y rápida.
# - Este ejercicio demuestra cómo corregir errores y mantener datos relevantes en un diccionario.