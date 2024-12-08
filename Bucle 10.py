#   Solicita calificaciones al usuario (hasta que ingrese -1) y calcula el promedio.
#	Ejemplo: Entradas: 5, 7, 8, -1 → Salida: Promedio: 6.67


# Inicializar variables
calificaciones = []
print("Ingresa las calificaciones una por una. Escribe -1 para finalizar.")

while True:
    try:
        calificacion = float(input("Ingresa una calificación: "))
        
        if calificacion == -1:  # Verificar si el usuario quiere salir
            break
        elif calificacion < 0 or calificacion > 10:  # Validar rango de calificación
            print("Por favor, ingresa una calificación válida entre 0 y 10.")
        else:
            calificaciones.append(calificacion)  # Añadir la calificación a la lista
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Calcular y mostrar el promedio si hay calificaciones
if calificaciones:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"Promedio: {promedio:.2f}")
else:
    print("No ingresaste ninguna calificación válida.")
