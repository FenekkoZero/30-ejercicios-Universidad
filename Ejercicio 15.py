# Solicita un nombre de usuario y contraseña, y valida si ambos son correctos. Permite tres intentos antes de bloquear el acceso.
# Ejemplo: Entrada: Usuario: admin, Contraseña: 1234 → Salida: "Bienvenido, admin.".


# Credenciales fijas
usuario_correcto = "admin"
contraseña_correcta = "1234"

# Número máximo de intentos
max_intentos = 3

# Contador de intentos
intentos = 0

while intentos < max_intentos:
    # Solicitar el nombre de usuario y la contraseña
    usuario = input("Ingresa tu nombre de usuario: ")
    contraseña = input("Ingresa tu contraseña: ")

    # Validar las credenciales
    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print(f"Bienvenido, {usuario}.")
        break
    else:
        intentos += 1
        print(f"Credenciales incorrectas. Te quedan {max_intentos - intentos} intentos.")

# Bloquear el acceso si se exceden los intentos
if intentos == max_intentos:
    print("Has excedido el número máximo de intentos. Acceso bloqueado.")
