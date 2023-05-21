# Esta función accede al archivo de usuarios y muestra su contenido.
def cargar_usuarios():
    file = open('usuarios.txt', 'r')
    usuarios = []
    for line in file:
        usuarios.append(line.rstrip('\n'))  # Elimina el salto de línea.
    file.close()
    return usuarios

# Rutina lógica para elegir un usuario del registro existente.
def escoger_usuario():
    usuarios = cargar_usuarios()  # Se cargan los usuarios disponibles.
    if len(usuarios) == 0:
        print("No se ha registrado ningún usuario. Registre un nuevo usuario.\n")
        return 0, "salir"
    else:
        print("Seleccione el usuario:")
        for usuario in usuarios:
            print(usuario)
        usuario_seleccionado = input("")
        if usuario_seleccionado in usuarios:
            return usuario_seleccionado, "ok"
        else: 
            print("El usuario seleccionado no existe.\n")
            return 0, "salir"

# Rutina lógica para crear nuevos usuarios.
def crear_usuario():
    usuarios = cargar_usuarios()  # Se cargan los usuarios disponibles.
    usuario_nuevo = input("Ingrese su nombre de usuario: ")
    # Se verifica si el usuario ya existe.
    if usuario_nuevo in usuarios:  
        print("El usuario seleccionado ya existe.\n")
        return 0, "salir"
    else:
        file = open("usuarios.txt", "a")
        file.write(f"{usuario_nuevo}\n")
        file.close()
        return usuario_nuevo, "ok"
    
