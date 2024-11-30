#Explicación del ejercicio
print ("""Una tienda ofrece un 20% de descuento si el cliente gasta más de $100. 
       Escribe un programa que calcule el monto final.""")
print("--")
print(" ")

#Crear una variable para dejar continuar al código una vez se ingrese un número
es_numero = int
es_numero = 0


#El bucle se va a repetir hasta que la variable "es_numero" sea 1
while es_numero == 0:
    
    #Mostrar la instrucción en pantalla y tomar el dato ingresado
    monto = input("Por favor ingrese el monto de su compra: ")
    
    #Revisar si el valor ingresado es un número o una cadena de texto
    if monto.isnumeric():
            es_numero = 1
            montoneto = int(monto)      
            #Pasar el valor de monto a un entero diferente porque... el cálculo se bugea bien raro sino, no me pregunten (?)
    else:
            print("Por favor ingrese un numero, no letras o símbolos.")
            print(" ")



total = 0
 
# El dato ingresado es numérico, por lo que se convierte en entero
# con int(variable) y se hace la comparación 
if es_numero == 1:   
        
        #Si el monto neto no aplica para un descuento, mostrar un mensaje
        if montoneto < 100:
            print(f"El monto de su compra es de ${montoneto}. Lo sentimos, no es elegible para un descuento.")
        
        #Si el cliente si aplica, calcular el 20% del monto neto, y luego el precio final con el descuento 
        elif montoneto >= 100: 
            descuento = montoneto * 0.2
            total = montoneto - int(descuento)
            
            print(f"El monto de su compra es de ${montoneto}. Usted es elegible para un descuento")
            print(f"del 20%, para un monto total de ${total}")
        
#Fin del programa