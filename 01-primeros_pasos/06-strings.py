"""
06-strings.py
Cadenas de texto (strings) en Python

En este archivo vamos a explorar los diferentes tipos de strings en Python
y cómo trabajar con ellos.
"""

# Strings con comillas simples
text1 = 'Hola'
print("String con comillas simples:", text1)

# Strings con comillas dobles  
text2 = "Holaaa"
print("String con comillas dobles:", text2)

# String multilínea con triple comillas
text3 = """Hola.
Mi nombre es Ricardo.
Soy de México.
Y bla bla bla."""
print("String multilínea con triple comillas:")
print(text3)

# Concatenación de strings
name = "Ricardo"
last_name = "Cuéllar"

# Concatenación básica (sin espacio)
full_name = name + last_name
print("\nConcatenación básica (sin espacio):", full_name)

# Concatenación con espacio (agregando un string vacío)
full_name_with_space = name + " " + last_name
print("Concatenación con espacio:", full_name_with_space)

# Otra forma de concatenación con espacio
full_name_alternative = name + " " + last_name
print("Otra forma de concatenación:", full_name_alternative)

"""
NOTA: Aunque la concatenación funciona, en Python moderno
se recomienda usar f-strings (formatted strings) para mayor
legibilidad y eficiencia. Los veremos en el siguiente video.

Reglas importantes para strings:
1. Si usas comillas simples al inicio, debes cerrar con comillas simples
2. Si usas comillas dobles al inicio, debes cerrar con comillas dobles
3. Los strings con triple comillas permiten múltiples líneas
4. La concatenación une strings directamente, sin agregar espacios automáticamente
"""

print("\n" + "="*50)
print("Resumen ejecutado correctamente!")
print("Recuerda: Los strings son secuencias inmutables de caracteres")
print("="*50)
