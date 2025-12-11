"""
OPERADORES DE MEMBRESÍA: 'in' y 'not in'
=========================================

¿Qué son los operadores de membresía?
--------------------------------------
Los operadores de membresía nos permiten verificar si un elemento
está presente (o no está presente) en una secuencia como:
- Listas
- Strings (cadenas de texto)
- Tuplas
- Diccionarios (solo en las claves)
- Conjuntos

' in ' → Verifica si un elemento ESTÁ en la secuencia
'not in' → Verifica si un elemento NO ESTÁ en la secuencia
"""

print("=== PARTE 1: OPERADOR 'in' (está en) ===\n")

# Ejemplo 1: 'in' con listas
print("1. 'in' con listas:")
frutas = ["manzana", "banana", "naranja", "uva"]

print(f"   Frutas: {frutas}")
print(f"   ¿'banana' está en la lista? {'banana' in frutas}")  # True
print(f"   ¿'pera' está en la lista? {'pera' in frutas}")      # False

# Ejemplo 2: 'in' con strings
print("\n2. 'in' con strings (cadenas de texto):")
texto = "Hola mundo, aprendiendo Python"

print(f"   Texto: '{texto}'")
print(f"   ¿'mundo' está en el texto? {'mundo' in texto}")    # True
print(f"   ¿'Python' está en el texto? {'Python' in texto}")  # True
print(f"   ¿'java' está en el texto? {'java' in texto}")      # False

# Ejemplo 3: 'in' con tuplas
print("\n3. 'in' con tuplas:")
coordenadas = (10, 20, 30)

print(f"   Coordenadas: {coordenadas}")
print(f"   ¿20 está en las coordenadas? {20 in coordenadas}")  # True
print(f"   ¿40 está en las coordenadas? {40 in coordenadas}")  # False

print("\n=== PARTE 2: OPERADOR 'not in' (no está en) ===\n")

# Ejemplo 4: 'not in' con listas
print("4. 'not in' con listas:")
colores = ["rojo", "verde", "azul"]

print(f"   Colores: {colores}")
print(f"   ¿'amarillo' NO está en la lista? {'amarillo' not in colores}")  # True
print(f"   ¿'rojo' NO está en la lista? {'rojo' not in colores}")          # False

# Ejemplo 5: 'not in' con strings
print("\n5. 'not in' con strings:")
palabra_secreta = "contraseña"

print(f"   Palabra secreta: '{palabra_secreta}'")
print(f"   ¿'123' NO está en la palabra? {'123' not in palabra_secreta}")  # True
print(f"   ¿'contra' NO está en la palabra? {'contra' not in palabra_secreta}")  # False

print("\n=== PARTE 3: CON DICCIONARIOS ===\n")

# Ejemplo 6: 'in' y 'not in' con diccionarios
print("6. Con diccionarios (solo verifica las CLAVES):")
estudiante = {
    "nombre": "Ana",
    "edad": 20,
    "carrera": "Ingeniería",
    "promedio": 8.5
}

print(f"   Diccionario estudiante: {estudiante}")
print(f"   ¿Existe la clave 'edad'? {'edad' in estudiante}")          # True
print(f"   ¿Existe la clave 'dirección'? {'dirección' in estudiante}") # False
print(f"   ¿NO existe la clave 'teléfono'? {'teléfono' not in estudiante}")  # True

print("\n=== PARTE 4: EJEMPLOS PRÁCTICOS ===\n")

# Ejemplo 7: Verificar usuario en sistema
print("7. Verificar acceso de usuario:")
usuarios_permitidos = ["admin", "usuario1", "invitado"]
usuario_actual = "admin"

if usuario_actual in usuarios_permitidos:
    print(f"   ✓ Acceso concedido para '{usuario_actual}'")
else:
    print(f"   ✗ Acceso denegado para '{usuario_actual}'")

# Ejemplo 8: Buscar palabra prohibida
print("\n8. Moderación de contenido:")
palabras_prohibidas = ["spam", "publicidad", "oferta"]
mensaje = "Hola, tengo una oferta especial para ti"

tiene_palabra_prohibida = any(palabra in mensaje.lower() for palabra in palabras_prohibidas)
print(f"   Mensaje: '{mensaje}'")
print(f"   ¿Tiene palabras prohibidas? {tiene_palabra_prohibida}")

# Ejemplo 9: Validar opciones de menú
print("\n9. Menú de opciones válidas:")
opciones_validas = ["A", "B", "C", "S"]
opcion_usuario = "B"

if opcion_usuario in opciones_validas:
    print(f"   ✓ Opción '{opcion_usuario}' es válida")
else:
    print(f"   ✗ Opción '{opcion_usuario}' no es válida")

# Ejemplo 10: Verificar ingredientes
print("\n10. Receta de cocina:")
ingredientes_disponibles = ["harina", "huevos", "azúcar", "leche"]
ingrediente_necesario = "huevos"

if ingrediente_necesario in ingredientes_disponibles:
    print(f"   ✓ Tenemos '{ingrediente_necesario}' para la receta")
else:
    print(f"   ✗ Nos falta '{ingrediente_necesario}' para la receta")

print("\n=== PARTE 5: EJERCICIOS PARA PRACTICAR ===\n")

print("""EJERCICIOS SUGERIDOS:
1. Crea una lista de números del 1 al 10 y verifica si el 5 está en la lista
2. Crea un string con tu nombre y verifica si contiene la letra 'a'
3. Crea un diccionario de productos con precios y verifica si un producto existe
4. Escribe una función que reciba una lista y un elemento, y retorne True si el elemento está en la lista
5. Crea un sistema de login que verifique si un usuario está en la lista de usuarios registrados

PISTAS:
- Usa 'in' para verificar presencia
- Usa 'not in' para verificar ausencia
- Recuerda que con diccionarios solo se verifican las claves, no los valores
""")

print("\n=== RESUMEN FINAL ===\n")

print("""RESUMEN DE OPERADORES DE MEMBRESÍA:

'elemento in secuencia' → Retorna True si el elemento está en la secuencia
'elemento not in secuencia' → Retorna True si el elemento NO está en la secuencia

USOS COMUNES:
- Verificar si un usuario tiene acceso
- Buscar palabras en textos
- Validar opciones de menú
- Comprobar ingredientes disponibles
- Filtrar contenido

RECUERDA:
1. 'in' y 'not in' son sensibles a mayúsculas/minúsculas
2. Con diccionarios solo verifican las CLAVES
3. Son muy eficientes y fáciles de leer
4. Se pueden usar en condicionales (if, while)
""")

# Demostración final
print("\n=== DEMOSTRACIÓN FINAL ===\n")

lista_ejemplo = [1, 2, 3, 4, 5]
string_ejemplo = "Python es genial"
diccionario_ejemplo = {"a": 1, "b": 2, "c": 3}

print(f"Lista: {lista_ejemplo}")
print(f"¿3 in lista? {3 in lista_ejemplo}")
print(f"¿6 not in lista? {6 not in lista_ejemplo}")

print(f"\nString: '{string_ejemplo}'")
print(f"¿'es' in string? {'es' in string_ejemplo}")
print(f"¿'Java' not in string? {'Java' not in string_ejemplo}")

print(f"\nDiccionario: {diccionario_ejemplo}")
print(f"¿'b' in diccionario? {'b' in diccionario_ejemplo}")
print(f"¿'d' not in diccionario? {'d' not in diccionario_ejemplo}")

print("\n¡Los operadores 'in' y 'not in' son tus aliados para buscar en Python!")
