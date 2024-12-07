# Solicita una calificación numérica y devuelve la letra correspondiente

# Solicitar la calificación al usuario
try:
    calificacion = int(input("Ingresa tu calificación numérica (0-100): "))

    # Determinar la calificación en letra
    if 90 <= calificacion <= 100:
        letra = "A"
    elif 80 <= calificacion <= 89:
        letra = "B"
    elif 70 <= calificacion <= 79:
        letra = "C"
    elif 60 <= calificacion <= 69:
        letra = "D"
    elif 0 <= calificacion < 60:
        letra = "F"
    else:
        letra = "Inválida"

    # Mostrar el resultado
    if letra == "Inválida":
        print("Por favor, ingresa una calificación válida entre 0 y 100.")
    else:
        print(f"Tu calificación es: {letra}")
except ValueError:
    print("Por favor, ingresa un número válido.")
