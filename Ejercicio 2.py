#Solicita al usuario un número y determina si es positivo, negativo o cero

while True:
    try:
        # Solicitar un número al usuario
        entrada = input("Ingresa un número: ")
        numero = float(entrada)  # Intentar convertir a número
        # Verificar si el número es positivo, negativo o cero
        if numero > 0:
            print("El número es positivo.")
        elif numero < 0:
            print("El número es negativo.")
        else:
            print("El número es cero.")
        break  # Salir del bucle si el número es válido
    except ValueError:
        print("Por favor, ingrese un número válido, no letras.")
