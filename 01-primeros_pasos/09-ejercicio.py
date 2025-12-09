"""
09-ejercicio.py
Ejercicio de String Indexes: Invertir un nombre

En este ejercicio vamos a practicar el uso de índices y slicing en strings
para invertir un nombre sin usar librerías externas ni concatenación manual.

Basado en el video tutorial sobre string indexes y el ejercicio propuesto.
"""

# 1. Definir el nombre a invertir
print("=== 1. Definir el nombre a invertir ===")
name = "Ricardo"
print(f"Nombre original: {name}")
print(f"Longitud del nombre: {len(name)} caracteres")

# 2. Recordar conceptos básicos de string indexes
print("\n=== 2. Recordar conceptos básicos de string indexes ===")
print("Índices positivos (de izquierda a derecha):")
for i in range(len(name)):
    print(f"  name[{i}] = '{name[i]}'")

print("\nÍndices negativos (de derecha a izquierda):")
for i in range(1, len(name) + 1):
    print(f"  name[{-i}] = '{name[-i]}'")

# 3. Intentar soluciones manuales (para entender el problema)
print("\n=== 3. Intentar soluciones manuales ===")
print("Opción 1: Concatenación manual (no óptima):")
name_reverse_manual = name[6] + name[5] + name[4] + name[3] + name[2] + name[1] + name[0]
print(f"  name_reverse_manual = {name_reverse_manual}")

print("\nProblema con la solución manual:")
print("  - Solo funciona para nombres de 7 letras")
print("  - Si cambia la longitud del nombre, hay que modificar el código")
print("  - No es escalable ni mantenible")

# 4. Solución óptima usando string indexes con step negativo
print("\n=== 4. Solución óptima usando string indexes ===")
print("Sintaxis: name[start:stop:step]")
print("  - start: posición inicial (vacío = inicio)")
print("  - stop: posición final (vacío = final)")
print("  - step: paso/salto entre caracteres")

print("\nEjemplos de step positivo:")
print(f"  name[::1] = '{name[::1]}'   # Paso 1: todo el string normal")
print(f"  name[::2] = '{name[::2]}'   # Paso 2: cada segundo carácter")

print("\nEjemplo de step negativo (¡la solución!):")
print(f"  name[::-1] = '{name[::-1]}'   # Paso -1: string invertido")

# 5. Explicación detallada de name[::-1]
print("\n=== 5. Explicación detallada de name[::-1] ===")
print("¿Cómo funciona name[::-1]?")
print("  1. start vacío: comienza desde el final (porque step es negativo)")
print("  2. stop vacío: termina al principio")
print("  3. step = -1: avanza de derecha a izquierda, un carácter a la vez")
print("\n  Equivalente a: name[-1:-len(name)-1:-1]")
print(f"  name[-1:-8:-1] = '{name[-1:-8:-1]}'")

# 6. Verificación de la solución
print("\n=== 6. Verificación de la solución ===")
name_reverse = name[::-1]
print(f"Nombre original: {name}")
print(f"Nombre invertido: {name_reverse}")

# Verificar que realmente está invertido
print("\nVerificación carácter por carácter:")
for i in range(len(name)):
    original_char = name[i]
    reversed_char = name_reverse[-(i+1)]
    print(f"  name[{i}]='{original_char}' ↔ name_reverse[{-(i+1)}]='{reversed_char}'")

# 7. Prueba con otros nombres
print("\n=== 7. Prueba con otros nombres ===")
test_names = ["Ana", "Juan", "María", "Alejandro", "Python"]
for test_name in test_names:
    reversed_name = test_name[::-1]
    print(f"  '{test_name}' → '{reversed_name}'")

# 8. Resumen y conclusiones
print("\n=== 8. Resumen y conclusiones ===")
print("""
Lo aprendido en este ejercicio:
1. Los string indexes permiten acceder a caracteres individuales
2. El slicing [start:stop:step] permite obtener substrings con saltos
3. Usar step negativo (-1) invierte el orden del string
4. Esta solución funciona para cualquier string, sin importar su longitud
5. Es más eficiente y mantenible que soluciones manuales

Ventajas de usar name[::-1]:
✓ Funciona para cualquier longitud de string
✓ No requiere modificar el código si cambia el nombre
✓ Es una sola línea de código
✓ Es eficiente en memoria y procesamiento
✓ Es fácil de leer y entender
""")

# 9. Ejercicio adicional para el estudiante
print("\n=== 9. Ejercicio adicional para practicar ===")
print("Intenta estos ejercicios por tu cuenta:")
print("  1. Invertir la frase 'Hola mundo'")
print("  2. Obtener cada tercer carácter de 'Programación'")
print("  3. Extraer las vocales de 'Electroencefalografista'")
print("  4. Crear un palíndromo a partir de 'oso'")

print("\n" + "="*60)
print("¡Ejercicio completado! Has aprendido a invertir strings con índices.")
print("Recuerda: name[::-1] es tu mejor amigo para invertir cualquier string.")
print("="*60)
