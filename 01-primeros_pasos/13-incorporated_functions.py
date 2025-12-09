"""
13-incorporated_functions.py
Funciones incorporadas y métodos en Python

En esta clase vamos a ver las funciones incorporadas (built-in functions)
y los métodos (methods) en Python.
"""

# ============================================
# FUNCIONES INCORPORADAS (BUILT-IN FUNCTIONS)
# ============================================

print("=== FUNCIONES INCORPORADAS ===")

# 1. print() - Función para imprimir mensajes
print("Hola mundo")  # Imprime: Hola mundo

# 2. type() - Función para obtener el tipo de dato
numero = 100
print(f"type(100) = {type(numero)}")  # Imprime: <class 'int'>

# 3. Transformación de tipos de datos
# Convertir entero a string
numero_str = str(numero)
print(f"str(100) = '{numero_str}'")  # Imprime: '100'
print(f"type(str(100)) = {type(numero_str)}")  # Imprime: <class 'str'>

# 4. round() - Redondear números
pi = 3.14159
print(f"round(3.14159) = {round(pi)}")  # Imprime: 3
print(f"round(3.14159, 2) = {round(pi, 2)}")  # Imprime: 3.14

# 5. abs() - Valor absoluto
print(f"abs(-10) = {abs(-10)}")  # Imprime: 10
print(f"abs(10) = {abs(10)}")    # Imprime: 10

# ============================================
# MÉTODOS (METHODS)
# ============================================

print("\n=== MÉTODOS ===")

# Los métodos son funciones específicas de una clase
# Por ejemplo, los strings tienen sus propios métodos

# Ejemplo con string
message = "Hola"
print(f"message = '{message}'")

# Método upper() - Convertir a mayúsculas
print(f"message.upper() = '{message.upper()}'")  # Imprime: 'HOLA'

# Método replace() - Reemplazar parte del string
mensaje_original = "Es un buen programador"
print(f"\nmensaje_original = '{mensaje_original}'")

# Reemplazar "Es" por "Soy"
new_message = mensaje_original.replace("Es", "Soy")
print(f"new_message = mensaje_original.replace('Es', 'Soy')")
print(f"new_message = '{new_message}'")  # Imprime: 'Soy un buen programador'

# Otros métodos útiles de strings
texto = "  Python es genial  "
print(f"\ntexto = '{texto}'")
print(f"texto.strip() = '{texto.strip()}'")  # Elimina espacios al inicio y final
print(f"texto.lower() = '{texto.lower()}'")  # Convierte a minúsculas
print(f"texto.upper() = '{texto.upper()}'")  # Convierte a mayúsculas
print(f"texto.startswith('Python') = {texto.strip().startswith('Python')}")  # True

# ============================================
# DIFERENCIA ENTRE FUNCIONES Y MÉTODOS
# ============================================

print("\n=== DIFERENCIA ENTRE FUNCIONES Y MÉTODOS ===")

print("""
Resumen:
1. Funciones incorporadas: Son funciones nativas de Python que podemos usar en cualquier momento.
   Ejemplos: print(), type(), str(), round(), abs()

2. Métodos: Son funciones específicas de una clase (tipo de dato).
   Ejemplos: string.upper(), string.replace(), string.strip()
   
   Los métodos se llaman usando la sintaxis: objeto.metodo()
   Mientras que las funciones se llaman: funcion(objeto)
""")

# Ejemplo comparativo
numero = 100

# Usando función incorporada
print(f"\nFUNCIÓN: type(numero) = {type(numero)}")

# Usando método (los enteros también tienen métodos)
print(f"MÉTODO: numero.bit_length() = {numero.bit_length()}")  # Método de enteros

# ============================================
# CONCLUSIÓN
# ============================================

print("\n=== CONCLUSIÓN ===")
print("""
Las funciones incorporadas son herramientas generales que Python nos proporciona,
mientras que los métodos son funciones específicas que pertenecen a un tipo de dato
particular (clase).

Ambos son fundamentales en la programación con Python y nos ayudan a realizar
tareas comunes de manera eficiente.
""")

print("\n¡Ejecuta este archivo para ver los resultados!")
print("Comando: python3 13-incorporated_functions.py")
