#Solicita tres números y determina cuál es el mayor.

while True:
    try:
        # Solicitar un número al usuario
        entrada = input("Ingrese un número: ")
        entrada2 = input("Ingrese un segundo número: ") 
        entrada3 = input("Ingrse un tercer número: ")
        
        numero = float(entrada)  # Intentar convertir a número
        numero2 = float(entrada2)
        numero3 = float(entrada3)

        # Comparar los 3 números
        
        if numero >= numero2 and numero >= numero3:
            mayor = numero
            print(f'El número mayor es {mayor}.')
            
        elif numero2 >= numero and numero2 >= numero3:
            mayor = numero2
            print(f'El número mayor es {mayor}.')
            
        else:
            mayor = numero3
            print(f'El número mayor es {mayor}.')
            
        break  # Salir del bucle si el número es válido
    
    
    except ValueError:
        print("Por favor, ingrese un número válido, no letras.")
