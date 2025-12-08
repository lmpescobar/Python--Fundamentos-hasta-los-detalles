"""
08-string_indexes.py
Ejemplos de índices y slicing en strings en Python
Basado en el video tutorial sobre string indexes
"""

# 1. String básico y acceso por índice
print("=== 1. String básico y acceso por índice ===")
name = "Ricardo"
print(f"name = {name}")
print(f"name[0] = {name[0]}")   # Primera letra: 'R'
print(f"name[1] = {name[1]}")   # Segunda letra: 'i'
print(f"name[6] = {name[6]}")   # Última letra: 'o' (índice 6 para 7 letras)

# 2. Índices negativos (acceso desde el final)
print("\n=== 2. Índices negativos (acceso desde el final) ===")
print(f"name[-1] = {name[-1]}")  # Última letra: 'o'
print(f"name[-2] = {name[-2]}")  # Penúltima letra: 'd'
print(f"name[-7] = {name[-7]}")  # Primera letra: 'R'

# Demostración con otro nombre
print("\n--- Demostración con 'Juanita' ---")
name2 = "Juanita"
print(f"name2 = {name2}")
print(f"name2[-1] = {name2[-1]}")  # Última letra: 'a'

# 3. Slicing (start:stop) - obtener substrings
print("\n=== 3. Slicing (start:stop) - obtener substrings ===")
print(f"name[0:3] = '{name[0:3]}'")    # Letras en posiciones 0,1,2: 'Ric'
print(f"name[0:2] = '{name[0:2]}'")    # Letras en posiciones 0,1: 'Ri'
print(f"name[2:5] = '{name[2:5]}'")    # Letras en posiciones 2,3,4: 'car'

# Regla importante: start se incluye, stop NO se incluye
print("\n--- Regla: start se incluye, stop NO se incluye ---")
print(f"name[0:7] = '{name[0:7]}'")    # Todo el string: 'Ricardo'
print(f"name[:4] = '{name[:4]}'")      # Desde inicio hasta índice 3: 'Rica'
print(f"name[3:] = '{name[3:]}'")      # Desde índice 3 hasta el final: 'ardo'

# 4. Slicing con step (start:stop:step) - saltar caracteres
print("\n=== 4. Slicing con step (start:stop:step) - saltar caracteres ===")
print(f"name[0:3:1] = '{name[0:3:1]}'")   # Paso 1 (default): 'Ric'
print(f"name[0:3:2] = '{name[0:3:2]}'")   # Paso 2: 'Rc' (salta de 2 en 2)
print(f"name[::2] = '{name[::2]}'")       # Todo el string, paso 2: 'Rcro' (índices 0,2,4,6)
print(f"name[1::2] = '{name[1::2]}'")     # Desde índice 1, paso 2: 'iad' (índices 1,3,5)

# 5. Ejemplos adicionales y combinaciones
print("\n=== 5. Ejemplos adicionales y combinaciones ===")

# Invertir un string
print(f"name[::-1] = '{name[::-1]}'")     # String invertido: 'odraciR'

# Obtener cada tercer carácter
print(f"name[::3] = '{name[::3]}'")       # Cada tercer carácter: 'Rao'

# Slicing con índices negativos
print(f"name[-5:-2] = '{name[-5:-2]}'")   # 'car' (índices -5,-4,-3)
print(f"name[-3:] = '{name[-3:]}'")       # Últimas 3 letras: 'rdo'

# 6. Resumen de conceptos clave
print("\n=== 6. Resumen de conceptos clave ===")
print("""
Conceptos cubiertos:
1. Índices positivos: comienzan en 0 desde el inicio
2. Índices negativos: comienzan en -1 desde el final
3. Slicing (start:stop): obtiene substrings
   - start se incluye, stop NO se incluye
4. Slicing con step (start:stop:step): salta caracteres
5. Valores por defecto:
   - start: 0 (inicio)
   - stop: longitud del string (final)
   - step: 1 (sin saltos)
""")

# 7. Ejercicio práctico
print("\n=== 7. Ejercicio práctico ===")
texto = "Python es genial"
print(f"texto = '{texto}'")
print("a) Primera letra:", texto[0])
print("b) Última letra:", texto[-1])
print("c) Primera palabra:", texto[0:6])
print("d) Palabra 'es':", texto[7:9])
print("e) Cada segunda letra:", texto[::2])
print("f) Texto invertido:", texto[::-1])

print("\n¡String indexes dominados! 🎯")
