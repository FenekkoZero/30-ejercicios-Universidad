#  Solicita un número al usuario y muestra su tabla de multiplicar del 1 al 10.

# Solicitar un número al usuario
try:
    numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))

    # Mostrar la tabla de multiplicar del número ingresado
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
except ValueError:
    print("Por favor, ingresa un número válido.")
