#    Escribe un programa que solicite una contraseña y valide si es correcta (ejemplo: contraseña fija es 12345).
#	Ejemplo: Entrada: 12345 → Salida: "Acceso concedido".

#Contraseña guardada
contraseña = '2803admin'


while True:
        # Solicitar la contraseña al usuario
        contraseña_ingresada = input("Por favor, ingresa la contraseña: ")

        

        # Verificar la operación y realizar el cálculo
        # Validar si la contraseña es correcta
        if contraseña_ingresada == contraseña:
            print("Acceso concedido.")

            # Mostrar el resultado
            print("")
            print ("Bienvenido al sistema :)")
            break  # Salir del bucle si todo es válido

        elif contraseña != contraseña_ingresada:  
            print("Contraseña incorrecta. Por favor, intente de nuevo.")
            print("")
