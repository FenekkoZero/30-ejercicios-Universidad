#Explicación del ejercicio
print ("Escribe un programa que solicite un número y determine si es mayor o menor que 10.")
print("--")
print(" ")

#Crear variable para dejar continuar al código
es_numero = int
es_numero = 0

#Repetir el bucle hasta que la variable sea 1

while es_numero == 0:
    #Mostrar la instrucción en pantalla y tomar el dato ingresado
    numero = input("Ingrese un numero: ")
    
    if numero.isnumeric():
            es_numero = 1  
        
    else:
            print("Por favor ingrese un numero, no letras o símbolos.")
            print(" ")




#Chequear que el valor sea un numero
#En caso de haber ingresado un nuero, se procede a calcular la relación
#En caso de haber ingresado un string se le indica al usuario que ingrese un numero

if es_numero == 1:   
        #Determinar relación de < o >
        #Se usa int(variable) para convertir el dato ingresado en un valor entero
        
        if int(numero) > 5:
            print(f'{numero} es mayor a 5.')
        elif int(numero) < 5: 
            print(f'{numero} es menor a 5.')
        elif int(numero) == 5:
            print(f'El numero ingresado es 5.')    
        
    



