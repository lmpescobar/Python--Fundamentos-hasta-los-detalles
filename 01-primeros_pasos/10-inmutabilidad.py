"""
Inmutabilidad en Python - Ejemplo de la clase

Este archivo demuestra que los strings son inmutables en Python.
Intenta cambiar un carácter individual de un string para ver el error.
"""

# Ejemplo 1: Reasignación de variable (esto funciona)
nombre = 'Ricardo'
print(f"1. Valor inicial: {nombre}")

nombre = 'Andrei'
print(f"2. Después de reasignar: {nombre}")

# Ejemplo 2: Intentar cambiar un carácter (esto genera error)
print("\n3. Intentando cambiar la primera letra de 'Ricardo' a 'L'...")
nombre = 'Ricardo'
nombre[0] = 'L'  # ERROR: 'str' object does not support item assignment
print(f"4. Después del cambio (nunca se ejecuta): {nombre}")

# Ejemplo 3: La forma correcta - crear un nuevo string
print("\n5. Forma correcta de 'cambiar' un string:")
nombre = 'Ricardo'
nombre = 'L' + nombre[1:]  # Creamos un nuevo string
print(f"6. Nuevo valor: {nombre}")

print("\n--- Conclusión ---")
print("Los strings son inmutables: no se pueden modificar después de creados.")
print("Solo se pueden reasignar a nuevos valores.")
