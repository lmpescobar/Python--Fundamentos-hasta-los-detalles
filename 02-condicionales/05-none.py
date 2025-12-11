"""
¿Qué es None?
==============
None es un valor especial en Python que significa "nada" o "vacío".
Piensa en None como una caja vacía: existe la caja, pero no tiene nada dentro.

Cuando usar None:
- Cuando una variable aún no tiene valor
- Cuando una función no devuelve nada
- Para indicar que algo no existe o no está disponible
"""

print("=== PARTE 1: None básico ===")

# Ejemplo 1: Variable sin valor
mi_variable = None
print(f"1. Variable con None: {mi_variable}")
print(f"   Tipo de la variable: {type(mi_variable)}")

# Ejemplo 2: Comparar con None
print("\n2. Comparando con None:")
print("   Usa 'is' para comparar (no uses '=='):")

if mi_variable is None:
    print("   ✓ La variable es None")
else:
    print("   ✗ La variable NO es None")

# Ejemplo 3: None en condicionales
print("\n3. None en condicionales (es False):")

if not mi_variable:
    print("   ✓ None se considera False en un if")
else:
    print("   ✗ None se considera True en un if")

print("\n=== PARTE 2: None en funciones ===")

# Ejemplo 4: Función que no retorna nada
def decir_hola(nombre):
    print(f"   Hola {nombre}, ¡bienvenido!")
    # Esta función no tiene 'return', así que retorna None automáticamente

resultado = decir_hola("Ana")
print(f"4. Resultado de función sin return: {resultado}")

# Ejemplo 5: Función que retorna None explícitamente
def buscar_en_lista(valor, lista):
    """Busca un valor en una lista. Retorna None si no lo encuentra."""
    if valor in lista:
        return f"Encontrado: {valor}"
    else:
        return None  # Explícitamente retornamos None

numeros = [1, 2, 3, 4, 5]
busqueda1 = buscar_en_lista(3, numeros)
busqueda2 = buscar_en_lista(10, numeros)

print(f"\n5. Buscando en lista [1, 2, 3, 4, 5]:")
print(f"   Buscar 3: {busqueda1}")
print(f"   Buscar 10: {busqueda2}")

print("\n=== PARTE 3: None en la práctica ===")

# Ejemplo 6: Valor por defecto en funciones
def crear_perfil(nombre, edad, ciudad=None):
    """Crea un perfil de usuario. Ciudad es opcional."""
    perfil = {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad  # Puede ser None si no se especifica
    }
    return perfil

perfil1 = crear_perfil("Carlos", 25, "Madrid")
perfil2 = crear_perfil("Laura", 30)  # No especificamos ciudad

print("6. Perfiles de usuarios:")
print(f"   Perfil 1: {perfil1}")
print(f"   Perfil 2: {perfil2}")

# Ejemplo 7: Inicializar variables para usar después
print("\n7. Inicializar variable con None:")

calificacion = None  # Aún no sabemos la calificación

# Más tarde en el programa...
calificacion = 95  # Ahora sí tenemos el valor

if calificacion is not None:
    print(f"   Calificación obtenida: {calificacion}")
else:
    print("   Calificación no disponible aún")

print("\n=== PARTE 4: None vs otros valores ===")

# Ejemplo 8: None no es igual a 0, False, o ""
print("8. Diferencias importantes:")

valores_a_comparar = [None, 0, False, "", [], 1, True, "Hola"]

print("   Valor      | ¿Es None? | ¿Es False en if?")
print("   -----------|-----------|------------------")

for valor in valores_a_comparar:
    es_none = valor is None
    es_false = not bool(valor)  # Convertir a booleano
    print(f"   {repr(valor):10} | {str(es_none):9} | {str(es_false):16}")

print("\n=== RESUMEN PARA PRINCIPIANTES ===")
print("""
PUNTOS CLAVE SOBRE NONE:
1. None significa "nada" o "sin valor"
2. Usa 'variable is None' para verificar (no uses ==)
3. Las funciones sin 'return' retornan None automáticamente
4. None es útil para valores opcionales o no disponibles
5. None se considera False en condicionales
6. None NO es lo mismo que 0, False, o cadena vacía

EJERCICIO PRÁCTICO:
Intenta modificar este código:
1. Crea una función que retorne None si un número es negativo
2. Usa None para representar un teléfono no disponible en un perfil
3. Verifica si una variable tiene valor usando 'is not None'
""")

# Ejemplo final interactivo
print("\n=== EJEMPLO FINAL INTERACTIVO ===")

def verificar_edad(edad):
    """Verifica si una persona es mayor de edad."""
    if edad < 0:
        return None  # Edad inválida
    elif edad >= 18:
        return "Mayor de edad"
    else:
        return "Menor de edad"

# Probamos la función
edades = [15, 25, -5, 0, 18]

print("Verificando edades:")
for edad in edades:
    resultado = verificar_edad(edad)
    if resultado is None:
        print(f"  Edad {edad}: ¡Inválida! (retorna None)")
    else:
        print(f"  Edad {edad}: {resultado}")

print("\n¡Recuerda! None es tu amigo para representar 'nada' en Python.")
