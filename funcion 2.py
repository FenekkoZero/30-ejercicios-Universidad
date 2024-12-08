#  Escribe una función que reciba dos números como parámetros y retorne su suma.

# Definir la función que suma dos números
def sumar(numero1, numero2):
    return numero1 + numero2

# Solicitar los dos números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Llamar a la función y mostrar el resultado
resultado = sumar(num1, num2)
print(f"La suma de {num1} y {num2} es: {resultado}")
