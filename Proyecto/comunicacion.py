import os
import estadisticas as est
import manejo_usuarios as usuarios

# Este menú seleciona el usuario.
def menu_usuarios():
    while True:
        menu_usuarios = int(input("Ingrese una opción:\n"
                            "1. Crear un usuario nuevo.\n"
                            "2. Usar un usuario existente.\n"
                            "3. Salir.\n"))
        os.system("cls")

        if menu_usuarios == 1:    
            usuario, interruptor = usuarios.crear_usuario()
            if interruptor == "repetir": continue
            else: break
        elif menu_usuarios == 2:
            usuario, interruptor = usuarios.escoger_usuario()
            if interruptor == "repetir": continue
            else: break
        elif menu_usuarios == 3:
            print("¡Adios!")
            usuario = ""
            interruptor = "salir"
            break
        else: continue
    return usuario, interruptor

# Este menú muestra las acciones posibles para el usuario elegido.
def menu_usuarios2(usuario):
    while True:
        menu_jugador = int(input("Ingrese una opción:\n"
                        "1. Nueva partida.\n"
                        "2. Ver estadísticas.\n"
                        "3. Salir.\n"))
        os.system("cls")

        if menu_jugador == 1: interruptor = "ok"; break
        elif menu_jugador == 2: 
            try:
                est.ver_estadisticas(usuario); continue
            except FileNotFoundError:
                print("No hay estadísticas para este usuario.\n")
                continue
        elif menu_jugador == 3: print("¡Adios!"); interruptor = "salir"; break
        else: continue
    return interruptor
