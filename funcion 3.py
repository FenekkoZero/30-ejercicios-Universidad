# Crea una función que reciba un número y retorne True si es par y False si es impar

# Definir la función que verifica si el número es par o impar
def es_par(numero):
    return numero % 2 == 0

# Solicitar un número al usuario
numero_usuario = int(input("Ingresa un número: "))

# Llamar a la función y mostrar el resultado
resultado = es_par(numero_usuario)
print(f"El número {numero_usuario} es par: {resultado}")
