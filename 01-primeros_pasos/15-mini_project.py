# Mini proyecto: Registro de usuario
# Este programa recibe datos del usuario y muestra una tarjeta con la información

def main():
    print("=== REGISTRO DE USUARIO ===")
    
    # Solicitar datos al usuario
    name = input("¿Cuál es tu nombre? ")
    year_of_birth = input("¿En qué año naciste? ")
    email = input("¿Cuál es tu correo electrónico? ")
    password = input("Escribe una contraseña: ")
    
    # Convertir año de nacimiento a entero para cálculos
    try:
        birth_year = int(year_of_birth)
    except ValueError:
        print("Error: El año de nacimiento debe ser un número válido.")
        return
    
    # Calcular edad en el 2050
    future_year = 2050
    future_age = future_year - birth_year
    
    # Calcular longitud de la contraseña
    password_length = len(password)
    
    # Crear tarjeta con formatted string
    card = f"""
    ====================================
    |          DATOS DEL USUARIO       |
    ====================================
    | Nombre: {name}
    | Email: {email}
    | Tendrás {future_age} años en el {future_year}
    | Tu contraseña es: {"*" * password_length}
    ====================================
    """
    
    # Mostrar la tarjeta
    print(card)

if __name__ == "__main__":
    main()
