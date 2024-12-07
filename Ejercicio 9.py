#   Calculadora básica:
# Solicita dos números y una operación (+, -, *, /) y realiza el cálculo correspondiente.


while True:
    try:
        # Solicitar los dos números al usuario
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        # Solicitar la operación al usuario
        operacion = input("Ingresa una operación (+, -, *, /): ")

        # Verificar la operación y realizar el cálculo
        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            if num2 == 0:  # Manejar división entre cero
                print("Error: No se puede dividir entre cero.")
                continue
            resultado = num1 / num2
        else:
            print("Operación inválida. Por favor, ingresa +, -, * o /.")
            continue

        # Mostrar el resultado
        print(f"Resultado: {resultado}")
        break  # Salir del bucle si todo es válido

    except ValueError:
        print("Por favor, ingrese números válidos.")
