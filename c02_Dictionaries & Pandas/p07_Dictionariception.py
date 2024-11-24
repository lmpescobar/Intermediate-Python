# Dictionariception

# Recordemos las listas: podían contener cualquier cosa, incluso otras listas.
# Para los diccionarios ocurre lo mismo. Los diccionarios pueden contener pares clave:valor
# donde los valores también pueden ser otros diccionarios.

# Como ejemplo, observa el siguiente script donde se muestra otra versión de `europe`:
# el diccionario con el que has estado trabajando todo este tiempo. 
# Las claves siguen siendo los nombres de los países, pero los valores son diccionarios 
# que contienen más información que solo la capital.

# Es totalmente posible encadenar corchetes para seleccionar elementos.
# Para obtener la población de España desde el diccionario `europe`, por ejemplo, necesitas:

# europe['spain']['population']

# Instrucciones:
# 1. Usa corchetes encadenados para seleccionar e imprimir la capital de Francia.
# 2. Crea un diccionario llamado `data` con las claves 'capital' y 'population'.
#    Asígnales los valores 'rome' y 59.83, respectivamente.
# 3. Agrega un nuevo par clave:valor al diccionario `europe`. 
#    La clave será 'italy' y el valor será el diccionario `data` que acabas de construir.

# Paso 1: Crear el diccionario inicial
# Este diccionario `europe` contiene información sobre varios países europeos.
# Cada clave (nombre del país) está asociada a un sub-diccionario con dos claves:
# 'capital' (nombre de la capital) y 'population' (población en millones).
europe = { 
    'spain': { 'capital': 'madrid', 'population': 46.77 },
    'france': { 'capital': 'paris', 'population': 66.03 },
    'germany': { 'capital': 'berlin', 'population': 80.62 },
    'norway': { 'capital': 'oslo', 'population': 5.084 }
}

# Paso 2: Acceder a la capital de Francia
# Usamos corchetes encadenados para acceder a la clave 'capital' dentro del sub-diccionario asociado a 'france'.
print("La capital de Francia es:", europe['france']['capital'])  # Imprime: paris

# Paso 3: Crear el sub-diccionario `data`
# Este diccionario almacena la información sobre Italia.
# Contiene las claves 'capital' y 'population' con los valores 'rome' y 59.83, respectivamente.
data = {
    "capital": "rome",  # Capital de Italia
    "population": 59.83  # Población de Italia en millones
}

# Paso 4: Agregar el sub-diccionario `data` al diccionario `europe`
# Agregamos un nuevo par clave:valor al diccionario `europe`. 
# La clave será 'italy' y el valor será el diccionario `data`.
europe['italy'] = data

# Paso 5: Imprimir el diccionario actualizado
# Imprimimos el diccionario `europe` para verificar que la clave 'italy' se haya agregado correctamente.
print("Diccionario actualizado de Europa:")
print(europe)