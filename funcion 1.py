# Crea una función que reciba un nombre como parámetro y retorne un saludo

# Definir la función que saluda al usuario
def saludar(nombre):
    return f"Hola, {nombre}!"

# Solicitar el nombre al usuario y llamar a la función
nombre_usuario = input("Ingresa tu nombre: ")
saludo = saludar(nombre_usuario)
print(saludo)
