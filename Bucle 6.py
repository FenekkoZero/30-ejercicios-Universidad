#Calcula el factorial de un número ingresado por el usuario (n!).
#Ejemplo: Entrada: 5 → Salida: 120


# Solicitar al usuario un número
try:
    numero = int(input("Ingresa un número para calcular su factorial: "))

    if numero < 0:
        print("El factorial no está definido para números negativos.")
    else:
        # Inicializar el resultado del factorial
        factorial = 1

        # Usar un bucle para calcular el factorial
        for i in range(1, numero + 1):
            factorial *= i

        # Mostrar el resultado
        print(f"El factorial de {numero} es: {factorial}")
except ValueError:
    print("Por favor, ingresa un número válido.")
