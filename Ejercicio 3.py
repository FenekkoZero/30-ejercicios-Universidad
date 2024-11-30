#Explicación del ejercicio
print ("Solicita un número al usuario y determina si es par o impar.")
print("--")
print(" ")

#Crear una variable para dejar continuar al código una vez se ingrese un número
es_numero = int
es_numero = 0


#El bucle se va a repetir hasta que la variable "es_numero" sea 1
while es_numero == 0:
    
    #Mostrar la instrucción en pantalla y tomar el dato ingresado
    numero = input("Ingrese un número: ")
    
    #Revisar si el valor ingresado es un número o una cadena de texto
    if numero.isnumeric():
            es_numero = 1      
    else:
            print("Por favor ingrese un numero, no letras o símbolos.")
            print(" ")




# El dato ingresado es numérico, por lo que se convierte en entero
# con int(variable) y se hace la comparación 
if es_numero == 1:   
        
        if int(numero) % 2 == 0:
            print(f'{numero} es un número par.')
        elif int(numero) %2 != 0: 
            print(f'{numero} es un número impar.')
        
#Fin del programa