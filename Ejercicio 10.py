#Solicita un año y determina si es bisiesto 

# Solicitar el año al usuario
try:
    año = int(input("Ingresa un año: "))

    # Determinar si el año es bisiesto
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print(f"El año {año} es bisiesto.")
    else:
        print(f"El año {año} no es bisiesto.")
except ValueError:
    print("Por favor, ingresa un año válido (número entero).")
