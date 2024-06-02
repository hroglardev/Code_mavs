import random

# Definir la longitud de la pista (en metros)
LONGITUD_PISTA = 100

# Lista de jugadores y sus posiciones iniciales
jugadores = {
    "Atleta 1": {"posicion": 0, "energia": 100},
    "Atleta 2": {"posicion": 0, "energia": 100},
    "Atleta 3": {"posicion": 0, "energia": 100}
}

def start_menu():

    '''
    Función para mostrar el menú de inicio y seleccionar la longitud de la carrera.
    
    Valor de retorno:
        100, 200, 400
    Tipo de valor de retorno:
        integer
    '''

    tipos_de_carrera = [100, 200, 400]
    print("Bienvenidos a la carrera olimpica.")
    print("(Ingrese exit para salir)")
    try:
        player_selection = input("Seleccione la longitud en metros de la carrera (100, 200 o 400): ")
        if player_selection == "exit":
            print("Gracias por jugar, hasta la próxima!")
            exit()
        player_selection = int(player_selection)
        while player_selection not in tipos_de_carrera:
            print("Debe elegir las distancias de 100m, 200m o 400m")
            return start_menu()
        return player_selection
    except ValueError:
        print("Debe ingresar un número entero.")
        return start_menu()


def replay_or_exit():
    
    print("¿Desea volver a jugar?")
    choice = input("S / N")
    if choice == "N":
        exit()
    else:
        iniciar_carrera()


# def save_data(new_round):
#     try:
#       with open('registros.txt', "w") as records: 
#     except Exception as err:
#       print(f"Hubo un problema: {err}")

# def get_data():
#     data = {}
#     try:
#       with open('registros.txt', "r") as records:
#         for line in range(len(records)):
#           score_data = line.split(":")
#           data[score_data[0]] = score_data[1].strip()
#     except Exception as err:
#       print(f"Hubo un problema: {err}")


# Función para simular el lanzamiento de dados (avance en la carrera)
def lanzamiento_dados():
    
    '''
    Función para simular el lanzamiento de dados (avance en la carrera).
    
    Valor de retorno:
        1 - 6
    Tipo de valor de retorno:
        integer
    '''
    
    return random.randint(1, 6)

# Función para mostrar la posición actual de los jugadores
def mostrar_posiciones():
    
    '''
    Función para mostrar la posición actual de los jugadores.
    Imprime en consola el nombre del jugador, su posición en la pista y su energía.
    '''

    for jugador, info in jugadores.items():
        print(f"{jugador}: {'-' * info['posicion']}[{info['posicion']}] Energía: {info['energia']}")

def get_user_info():
    
    '''
    Función para obtener el nombre del usuario.
    
    Valor de retorno:
        nombre ingresado por el usuario
    Tipo de valor de retorno:
        string
    '''
    
    name = input("Introduzca su nombre: ")
    return name

# Función para determinar al ganador
def determinar_ganador():
    
    '''
    Función para determinar al ganador de la carrera.
    Verifica si algún jugador ha cruzado la meta (LONGITUD_PISTA).

    si consigue un ganador, devuelve el nombre del jugador ganador.
        Valor de retorno:
            nombre del jugador ganador
        Tipo de valor de retorno:
            string

    si no hay ganador, devuelve None.
    '''
    
    for jugador, info in jugadores.items():
        if info["posicion"] >= LONGITUD_PISTA:
            return jugador
    return None

# Función para simular eventos especiales durante la carrera
def evento_especial(jugador):
    
    '''
    Función para simular eventos especiales durante la carrera.
    Los eventos especiales pueden ser ventajas o desventajas para el jugador.

    Parametros:
        jugador (str): Nombre del jugador al que se le aplica el evento especial
    
    si el evento es "Ráfaga de viento a favor":
        el jugador avanza 3 posiciones en la pista
    
    si el evento es "Pérdida de energía":
        el jugador pierde 20 puntos de energía
        si la energía del jugador es menor a 0, se establece en 0 
    '''

    evento = random.choice(["Ráfaga de viento a favor", "Pérdida de energía"])
    print(f"\n¡{evento} para {jugador}!")
    if evento == "Ráfaga de viento a favor":
        jugadores[jugador]["posicion"] += 3
    elif evento == "Pérdida de energía":
        jugadores[jugador]["energia"] -= 20
        if jugadores[jugador]["energia"] < 0:
            jugadores[jugador]["energia"] = 0

# Función principal para iniciar la carrera
def iniciar_carrera():
    
    '''
    Función principal para iniciar la carrera.
    Inicializa la posición y energía de los jugadores.
    Muestra el mensaje de inicio de la carrera.
    Mientras la carrera no haya finalizado, solicita a los jugadores lanzar los dados.
    Verifica si ocurre un evento especial durante la carrera.
    Muestra las posiciones de los jugadores.
    Determina al ganador de la carrera.
    '''

    jugadores[get_user_info()] = {"posicion": 0, "energia": 100}

    is_finished = False
    print("¡Comienza la carrera olímpica!")
    while not is_finished:
        input("Presiona Enter para lanzar los dados...")
        for jugador in jugadores:
            avance = lanzamiento_dados()
            jugadores[jugador]["posicion"] += avance
            if jugadores[jugador]["posicion"] >= LONGITUD_PISTA:
                jugadores[jugador]["posicion"] = LONGITUD_PISTA
                print(f"\n{jugador} ha cruzado la meta!")
                is_finished = True
                continue
            if random.random() < 0.2:  # Probabilidad del 20% de un evento especial
                evento_especial(jugador)
        mostrar_posiciones()
        ganador = determinar_ganador()
        if ganador:
            print(f"\n¡{ganador} ha ganado la carrera!")
            is_finished = True

# Iniciar la carrera
iniciar_carrera()