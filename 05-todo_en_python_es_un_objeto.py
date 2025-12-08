# Todo en Python es un objeto
# Demostración del concepto "Todo en Python es un objeto"

# Variables tomadas del archivo anterior
nombre = "Ricardo"
edad = 29
decimal = 20.42
booleano = True
lista = [1, 2, 3]

print("=== Demostración: Todo en Python es un objeto ===")
print()

# 1. Mostrar el tipo de cada variable con type()
print("1. Usando type() para ver la clase de cada variable:")
print(f"   nombre = {nombre}  -> type(nombre) = {type(nombre)}")
print(f"   edad = {edad}  -> type(edad) = {type(edad)}")
print(f"   decimal = {decimal}  -> type(decimal) = {type(decimal)}")
print(f"   booleano = {booleano}  -> type(booleano) = {type(booleano)}")
print(f"   lista = {lista}  -> type(lista) = {type(lista)}")
print()

# 2. Demostrar que incluso las funciones son objetos
print("2. Las funciones también son objetos:")
print(f"   type(print) = {type(print)}")
print(f"   type(type) = {type(type)}")
print()

# 3. Los objetos tienen métodos (superpoderes)
print("3. Métodos de los objetos (ejemplo con string):")
print(f"   nombre.upper() = {nombre.upper()}")
print(f"   nombre.lower() = {nombre.lower()}")
print(f"   nombre.replace('a', 'o') = {nombre.replace('a', 'o')}")
print()

# 4. Los números también son objetos y tienen métodos
print("4. Métodos de los números (int):")
print(f"   edad.bit_length() = {edad.bit_length()}")  # bits necesarios para representar el número
print(f"   edad.__add__(5) = {edad.__add__(5)}")      # equivalente a edad + 5
print()

# 5. Las listas son objetos con métodos
print("5. Métodos de las listas:")
lista.append(4)
print(f"   Después de lista.append(4) -> lista = {lista}")
print(f"   lista.pop() = {lista.pop()} -> lista ahora = {lista}")
print()

print("=== Conclusión ===")
print("Todo en Python es un objeto: variables, funciones, tipos, etc.")
print("Por eso podemos usar métodos como .upper(), .append(), etc.")
print("Recuerda: ¡Todo en Python es un objeto! x3")