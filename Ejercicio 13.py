# Función para determinar el signo zodiacal
def obtener_signo_zodiacal(dia, mes):
    if (mes == "marzo" and dia >= 21) or (mes == "abril" and dia <= 19):
        return "Aries"
    elif (mes == "abril" and dia >= 20) or (mes == "mayo" and dia <= 20):
        return "Tauro"
    elif (mes == "mayo" and dia >= 21) or (mes == "junio" and dia <= 20):
        return "Géminis"
    elif (mes == "junio" and dia >= 21) or (mes == "julio" and dia <= 22):
        return "Cáncer"
    elif (mes == "julio" and dia >= 23) or (mes == "agosto" and dia <= 22):
        return "Leo"
    elif (mes == "agosto" and dia >= 23) or (mes == "septiembre" and dia <= 22):
        return "Virgo"
    elif (mes == "septiembre" and dia >= 23) or (mes == "octubre" and dia <= 22):
        return "Libra"
    elif (mes == "octubre" and dia >= 23) or (mes == "noviembre" and dia <= 21):
        return "Escorpio"
    elif (mes == "noviembre" and dia >= 22) or (mes == "diciembre" and dia <= 21):
        return "Sagitario"
    elif (mes == "diciembre" and dia >= 22) or (mes == "enero" and dia <= 19):
        return "Capricornio"
    elif (mes == "enero" and dia >= 20) or (mes == "febrero" and dia <= 18):
        return "Acuario"
    elif (mes == "febrero" and dia >= 19) or (mes == "marzo" and dia <= 20):
        return "Piscis"
    else:
        return "Fecha inválida"

# Solicitar la fecha de nacimiento al usuario
try:
    dia = int(input("Ingresa el día de tu nacimiento: "))
    mes = input("Ingresa el mes de tu nacimiento (en minúsculas): ").strip().lower()

    # Determinar el signo zodiacal
    signo = obtener_signo_zodiacal(dia, mes)

    # Mostrar el resultado
    print(f"Tu signo zodiacal es: {signo}")
except ValueError:
    print("Por favor, ingresa un día válido (número entero).")
