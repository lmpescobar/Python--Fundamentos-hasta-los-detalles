"""
Conversiones en Python

Este archivo demuestra diferentes tipos de conversiones en Python
basado en el tutorial del video.
"""

print("=== CONVERSIONES EN PYTHON ===\n")

# 1. Verificación del tipo de dato con type()
print("1. Verificación del tipo de dato:")
value = 100
print(f"Valor: {value}, Tipo: {type(value)}")

# 2. Conversión de int a string
print("\n2. Conversión de int a string:")
value = 100
print(f"Valor original: {value}, Tipo: {type(value)}")

# Convertir a string
value_str = str(value)
print(f"Valor convertido: {value_str}, Tipo: {type(value_str)}")

# Demostración de concatenación con string (y error con int)
print("\n3. Demostración de concatenación:")
# Esto NO funcionará con int (comentado para evitar error)
# resultado_error = "Hola " + value  # Esto causaría TypeError
# print(f"Esto causaría error: {resultado_error}")

# Esto SÍ funcionará con string
resultado_exito = "Hola " + value_str
print(f"Concatenación exitosa con string: {resultado_exito}")

# 4. Conversión de string a int
print("\n4. Conversión de string a int:")
value_str = "100"
print(f"Valor original: {value_str}, Tipo: {type(value_str)}")

# Convertir a int
value_int = int(value_str)
print(f"Valor convertido: {value_int}, Tipo: {type(value_int)}")

# 5. Conversión de string a float
print("\n5. Conversión de string a float:")
value_str = "100"
print(f"Valor original: {value_str}, Tipo: {type(value_str)}")

# Convertir a float
value_float = float(value_str)
print(f"Valor convertido: {value_float}, Tipo: {type(value_float)}")

# 6. Conversión de int a float
print("\n6. Conversión de int a float:")
value_int = 100
print(f"Valor original: {value_int}, Tipo: {type(value_int)}")

# Convertir a float
value_float = float(value_int)
print(f"Valor convertido: {value_float}, Tipo: {type(value_float)}")

# 7. Conversión de float a int
print("\n7. Conversión de float a int:")
value_float = 100.7
print(f"Valor original: {value_float}, Tipo: {type(value_float)}")

# Convertir a int (pierde la parte decimal)
value_int = int(value_float)
print(f"Valor convertido: {value_int}, Tipo: {type(value_int)}")

# 8. Manejo de errores - conversión fallida
print("\n8. Manejo de errores - conversión fallida:")
try:
    value_str = "hola"
    print(f"Intentando convertir '{value_str}' a int...")
    value_int = int(value_str)
    print(f"Resultado: {value_int}")
except ValueError as e:
    print(f"Error: {e}")
    print("No se puede convertir un string no numérico a int")

# 9. Resumen de funciones de conversión
print("\n9. Resumen de funciones de conversión:")
print("- str(): convierte cualquier tipo a string")
print("- int(): convierte a entero (solo strings numéricos, floats, etc.)")
print("- float(): convierte a número decimal")
print("- type(): devuelve el tipo de dato de un valor")

print("\n=== FIN DEL PROGRAMA ===")
