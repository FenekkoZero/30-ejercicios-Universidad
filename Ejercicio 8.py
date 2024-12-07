#Explicación del ejercicio
print ("Solicita una edad y clasifica al usuario como niño (0-12), adolescente (13-17) o adulto (18+).")
print("--")
print(" ")

#Crear variable para dejar continuar al código
es_numero = int
es_numero = 0

#Repetir el bucle hasta que la variable sea 1

while es_numero == 0:
    #Mostrar la instrucción en pantalla y tomar el dato ingresado
    numero = input("Ingrese su edad: ")
    
    if numero.isnumeric():
            es_numero = 1  
            edad = int(numero)
    else:
            print("Por favor ingrese un numero, no letras o símbolos.")
            print(" ")




#Chequear que el valor sea un numero
#En caso de haber ingresado un nuero, se procede a calcular la relación
#En caso de haber ingresado un string se le indica al usuario que ingrese un numero

if es_numero == 1:   
        #Determinar relación de < o >
        #Se usa int(variable) para convertir el dato ingresado en un valor entero
        
        if edad >= 18:
            print(f"Tienes {edad} años. Eres un adulto.")
        elif edad < 18 and edad >= 12: 
                print(f"Tienes {edad} años. Eres un adolescente.")
        elif edad < 12:
            print(f"Tienes {edad} años. Eres un niño.")
    