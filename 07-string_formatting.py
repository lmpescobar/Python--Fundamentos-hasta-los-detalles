"""
06-string_formatting.py
Formateo de cadenas (f-strings) en Python

En este archivo vamos a explorar el formateo de strings usando f-strings,
la forma moderna y recomendada en Python para trabajar con strings y variables.
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

# Formateo de strings con f-strings
name = "Ricardo"
last_name = "Cuéllar"

# Formateo con f-string (forma moderna y recomendada)
full_name = f"{name} {last_name}"
print("\nFormateo con f-string:", full_name)

# Ejemplo adicional del video: usando variables numéricas
age = 29
message = f"{full_name}, tienes {age} años"
print("Mensaje formateado:", message)

"""
NOTA: Los f-strings (formatted strings) son la forma recomendada en Python moderno
para trabajar con strings que contienen variables. Son más legibles, eficientes
y fáciles de mantener que la concatenación tradicional.

Ventajas de f-strings:
1. Más legibles: puedes ver directamente dónde van las variables
2. Más eficientes: Python los evalúa más rápido que la concatenación
3. Más flexibles: puedes incluir expresiones directamente: f"El doble es {2*5}"
4. Más mantenibles: al agregar más variables, el código sigue siendo claro

Reglas importantes para f-strings:
1. Siempre comienzan con la letra 'f' o 'F' antes de las comillas
2. Las variables van entre llaves {} dentro del string
3. Puedes usar comillas simples o dobles para el string
4. Puedes incluir expresiones completas dentro de las llaves
"""

print("\n" + "="*50)
print("Resumen ejecutado correctamente!")
print("Recuerda: Los f-strings son la forma moderna de trabajar con strings y variables")
print("="*50)
