# Solicita un número entero y muestra su versión invertida.
# Ejemplo: Entrada: 1234 → Salida: 4321.


# Solicitar un número al usuario
try:
    numero = int(input("Ingresa un número entero: "))
    
    # Convertir el número a positivo para evitar problemas con el signo
    invertido = int(str(abs(numero))[::-1])
    
    # Volver a aplicar el signo si el número original era negativo
    if numero < 0:
        invertido = -invertido

    # Mostrar el resultado
    print(f"El número invertido de {numero} es: {invertido}")
except ValueError:
    print("Por favor, ingresa un número entero válido.")
