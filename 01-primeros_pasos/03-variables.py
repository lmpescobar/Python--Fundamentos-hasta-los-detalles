# 03-variables.py
# Variables en Python

# Ejemplo básico: crear una variable y usarla en print
saludo = "hola mundo"
print(saludo)  # Imprime: hola mundo

# Cambiamos el valor de la variable
saludo = "Hola Mundo 2"
print(saludo)  # Imprime: Hola Mundo 2

# Otras variables de texto
name = "Ricardo"
lastname = "Cuéllar"
print(name)
print(lastname)

# Variables numéricas
age = 30
money = 20.5
print(age)
print(money)

# Ejemplo de camelCase (no recomendado en Python pero funciona)
nombreCompleto = "Ricardo Cuéllar"
print(nombreCompleto)

# Recomendaciones
# PEP8 sugiere usar snake_case para variables
nombre_completo = "Ricardo Cuéllar"  # Esta es la forma convencional
print(nombre_completo)

# Variable privada (convención: un guion bajo al inicio)
_nombre_privado = "Variable Privada"
print(_nombre_privado)

# Constante (convención: mayúsculas y guiones bajos)
PI = 3.1416
print(PI)

# Podemos hacer operaciones con variables
radio = 5
area = PI * radio ** 2
print("Área del círculo con radio", radio, "es", area)

# ---------------------------------------------------------------------
# Recomendaciones de PEP8 para variables:
# 1. Usar snake_case para nombres de variables (ej: nombre_completo)
# 2. Las variables privadas comienzan con un guion bajo (ej: _privada)
# 3. Las constantes se escriben en MAYÚSCULAS con guiones bajos (ej: PI)
# 4. Evitar camelCase en Python (aunque funcione)
# 5. Usar nombres descriptivos y en inglés (buena práctica)
# 6. Python es dinámico, puedes reasignar variables a cualquier tipo.
# ---------------------------------------------------------------------

# Fin del archivo