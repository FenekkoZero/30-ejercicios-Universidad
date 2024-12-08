#  Imprime todos los números pares entre 1 y 20.

print('Los números pares entre el 1 y el 20 son: ')

# Usar un bucle para imprimir números pares entre 1 y 20
for numero in range(1, 21):
    if numero % 2 == 0:  # Verificar si el número es par
        print(numero)
