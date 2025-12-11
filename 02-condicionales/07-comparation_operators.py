# Igualdad ==
print(5 == 5)  # True
print(5 == 3)  # False
print("hello" == "hello")  # True

# Operador de desigualdad !=
print(5 != 5)  # False
print(5 != 3)  # True
print("hello" != "world")  # True

# Mayor que >
print("\n# Mayor que >")
print(10 > 5)   # True
print(5 > 10)   # False
print(5 > 5)    # False
print("abc" > "abd")  # False (comparación lexicográfica)
print("abd" > "abc")  # True

# Menor que <
print("\n# Menor que <")
print(3 < 7)    # True
print(7 < 3)    # False
print(5 < 5)    # False
print("apple" < "banana")  # True
print("banana" < "apple")  # False

# Mayor o igual que >=
print("\n# Mayor o igual que >=")
print(10 >= 5)  # True
print(5 >= 10)  # False
print(5 >= 5)   # True (¡importante! igual también es verdadero)
print(7 >= 7)   # True

# Menor o igual que <=
print("\n# Menor o igual que <=")
print(3 <= 7)   # True
print(7 <= 3)   # False
print(5 <= 5)   # True
print(10 <= 10) # True

# Ejemplos con diferentes tipos de datos
print("\n# Ejemplos con diferentes tipos")
print(3.14 > 3)      # True (flotante vs entero)
print(10 <= 10.0)    # True (entero vs flotante)
print("a" < "b")     # True (comparación de caracteres)
print("A" < "a")     # True (las mayúsculas van antes en ASCII/Unicode)

# Ejemplos prácticos
print("\n# Ejemplos prácticos")
edad = 18
print(f"¿Es mayor de edad? {edad >= 18}")  # True

temperatura = 25
print(f"¿Temperatura agradable? {20 <= temperatura <= 30}")  # True

nota = 85
aprobado = nota >= 60
print(f"¿Aprobado con nota {nota}? {aprobado}")  # True

# Comparaciones encadenadas
print("\n# Comparaciones encadenadas")
print(1 < 2 < 3)     # True (equivale a: 1 < 2 and 2 < 3)
print(1 < 3 < 2)     # False
print(5 <= 5 <= 5)   # True
print(10 > 5 > 0)    # True

# Resumen de todos los operadores
print("\n# Resumen de operadores de comparación")
print("Operador | Significado | Ejemplo (True) | Ejemplo (False)")
print("---------|-------------|----------------|----------------")
print("==       | Igualdad    | 5 == 5         | 5 == 3")
print("!=       | Desigualdad | 5 != 3         | 5 != 5")
print(">        | Mayor que   | 10 > 5         | 5 > 10")
print("<        | Menor que   | 3 < 7          | 7 < 3")
print(">=       | Mayor o igual | 5 >= 5       | 5 >= 10")
print("<=       | Menor o igual | 5 <= 5       | 10 <= 5")
