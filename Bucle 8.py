#	Solicita un número entero y calcula la suma de sus dígitos.
#	Ejemplo: Entrada: 123 → Salida: 6 (1 + 2 + 3


# Solicitar un número al usuario
try:
    numero = int(input("Ingresa un número entero: "))
    
    # Convertir el número a positivo en caso de que sea negativo
    numero = abs(numero)
    
    # Inicializar la suma de los dígitos
    suma_digitos = 0
    
    # Calcular la suma de los dígitos
    for digito in str(numero):
        suma_digitos += int(digito)
    
    # Mostrar el resultado
    print(f"La suma de los dígitos de {numero} es: {suma_digitos}")
except ValueError:
    print("Por favor, ingresa un número entero válido.")
