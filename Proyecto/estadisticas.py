from datetime import datetime

# Esta función crea un archivo de estadísticas para cada usuario.
def crear_estadisticas(usuario, condicion):
    fecha_hora = datetime.now()  # Variable que contiene la fecha y hora
    fecha_hora = fecha_hora.strftime("%d/%m/%Y %H:%M:%S")  # Se da formato a la fecha y hora.
    file = open(f"est_{usuario}.txt", "a")
    file.write(f"{fecha_hora}: {condicion}\n")
    file.close()

# Esta función carga las estadísticas para un usuario dado y las muestra en pantalla.
# Muestra las 5 partidas más recientes.
def ver_estadisticas(usuario):
    file = open(f'est_{usuario}.txt', 'r')
    estadisticas = []
    for line in file:
        estadisticas.append(line.rstrip('\n'))  # Elimina el salto de línea.
    file.close()
    if len(estadisticas) == 0: 
        print("No hay estadísticas para este usuario.\n")
    elif len(estadisticas) >= 5:
        for i in range(-1, -6, -1):
            print(estadisticas[i])
        print("\n")
    else: 
        for i in range(1, len(estadisticas) + 1):
            print(estadisticas[-i])
        print("\n")
