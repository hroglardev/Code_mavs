import random


def context():

    """
    Se imprime el contexto del juego.
    """
    
    print("\nArgetina y Paises Bajos se encuentran empatados 0-0 en la final de los juegos olimpicos de Paris 2024.")
    print("Quien gane se queda con la medalla de oro en los juegos olimpicos de Paris 2024.")
    print("Argentina ha ganado el sorteo y tira primero.")
    print("(ingrese 'exit' para salir del juego)")

def generate_computer_choice():

    """
    Se genera un número aleatorio entre 1 y 9 para simular la elección de la máquina
    en la tanda de penales.
    Valor de retorno:
        1 - 9
    Tipo de valor de retorno:
        integer
    """
    
    return random.randint(1, 9)

def draw_goalpost():
    
    """
    Se imprime el arco para que el jugador pueda visualizar la zona de la portería
    en la que quiere disparar.
    """

    print("\nTeniendo en cuenta el siguiente arco")
    print("|-------------------------|")
    print("|   1        2        3   |")
    print("|   4        5        6   |")
    print("|   7        8        9   |")

def generate_player_choice(instruction):    

    """
    Se solicita al jugador que elija una zona de la portería en la que quiere disparar.
    Se valida que el valor ingresado sea un número entero entre 1 y 9.
    Si el jugador ingresa "exit", se termina el juego.
    Si el jugador ingresa un valor que no es un número entero, se le solicita que ingrese un número entero.
    Si el jugador ingresa un valor que no está entre 1 y 9, se le solicita que ingrese un valor entre 1 y 9.

    Parametros:
        instruction (str): Instrucción para el jugador
    Valor de retorno:
        1 - 9
    Tipo de valor de retorno:
        integer
    """

    try:
        player_choice = input(f"{instruction} 1-9: ")
        if player_choice == "exit":
            print("Gracias por jugar, hasta la próxima!")
            exit()
        player_choice = int(player_choice)
        while player_choice < 1 or player_choice > 9:
            print("Debe seleccionar una zona de portería entre 1 y 9.")
            return generate_player_choice(instruction)
        return player_choice
    except ValueError:
        print("Debe ingresar un número entero.")
        return generate_player_choice(instruction)
    
def show_ai_choice(instruction, kicker, goalie, computer_choice, player_choice, message):

    """
    Se imprime la elección de la máquina en la tanda de penales.
    y el resultado de la elección del jugador.
    Se imprime el resultado de la tanda de penales.
    
    Parametros:
        instruction (str): Instrucción para el jugador
        kicker (str): Equipo que patea el penal
        goalie (str): Equipo que ataja el penal
        computer_choice (int): Elección de la máquina en la tanda de penales
        player_choice (int): Elección del jugador en la tanda de penales
        message (str): Mensaje que se imprime en el resultado de la tanda de penales
    """

    if instruction == "Dispare al arco":
        print(f"La portera de {goalie} se tiró a la posición {(computer_choice if kicker == "Argentina" else player_choice)} {message}")
    else:
        print(f"La tiradora de {kicker} disparó a la posición {computer_choice} y la portera de {goalie} {message}")

def penalty_attempt(instruction, kicker, goalie):

    """
    Se simula el turno de un jugador en la tanda de penales.
    Se solicita al jugador que elija una zona de la portería en la que quiere disparar.
    Se genera un número aleatorio entre 1 y 9 para simular la elección de la máquina en la tanda de penales.
    Se valida si el jugador o la máquina atajaron el gol.
    Si el jugador o la máquina atajaron el gol, se imprime el resultado y se retorna False.
    Si el jugador o la máquina convirtieron el gol, se imprime el resultado y se retorna True.
    
    Parametros:
        instruction (str): Instrucción para el jugador
        kicker (str): Equipo que patea el penal
        goalie (str): Equipo que ataja el penal
    Valor de retorno:
        True: si el jugador o la máquina convirtieron el gol
        False: si el jugador o la máquina atajaron el gol
    Tipo de valor de retorno:
        boolean
    """
    
    draw_goalpost()
    player_choice = generate_player_choice(instruction)
    computer_choice = generate_computer_choice()

    if player_choice in (2, 5, 8) and computer_choice in (2, 5, 8) or player_choice == computer_choice:
        print(f"{goalie} atajo el gol")
        show_ai_choice(instruction, kicker, goalie, computer_choice, player_choice, "y consiguió atajar el gol.")
        return False
    else:
        print(f"GOOOOOL de {kicker}!!")
        show_ai_choice(instruction, kicker, goalie, computer_choice, player_choice, "y no consiguió atajar.")
        return True
    
    
def update_score(instruction, kicker, goalie, score_kicker):
    
    """
    Actualiza el score del equipo que patea el penal.
    Parametros:
        instruction (str): Instrucción para el jugador
        kicker (str): Equipo que patea el penal
        goalie (str): Equipo que ataja el penal
        score_kicker (int): Score del equipo que patea el penal
    Valor de retorno:
        int: Score actualizado del equipo que patea el penal
    Tipo de valor de retorno:
        integer
    """

    turn_result = penalty_attempt(instruction, kicker, goalie)
    if turn_result:
        score_kicker += 1
    return score_kicker

def show_score(score_kicker, score_goalie):
    
    """
    Imprime el score de la tanda de penales.
    Parametros:
        score_kicker (int): Score del equipo que patea el penal
        score_goalie (int): Score del equipo que ataja el penal
    """
    
    print(f"El score es Argentina: {score_kicker}, Paises Bajos: {score_goalie}")

def play_penalties():
   
    """
    Esta es la función principal que simula la tanda de penales.
    Se inicializan las variables de la tanda de penales.
    Se simula una ronda de penales y se analiza despues de cada tiro si la tanda debe finaliza o continuar.
    Se actualiza el score de la tanda de penales.
    Se imprime el score de la tanda de penales.
    Cuando la tanda de penales termina, se imprime el resultado de la tanda de penales, agregando algo de contexto histórico.
    
    Variables:
        user_goals (int): Score de Argentina
        pc_goals (int): Score de Paises Bajos
        score_difference (int): Diferencia de goles entre Argentina y Paises Bajos
        rounds (int): Ronda actual de la tanda de penales
        remaining_rounds (int): Rondas restantes de la tanda de penales
    """

    user_goals = 0
    pc_goals = 0
    score_difference = 0
    rounds = 0
    remaining_rounds = 5

    while (remaining_rounds >= score_difference) or (rounds >= 5 and score_difference == 0):

        user_goals = update_score("Dispare al arco", "Argentina", "Paises Bajos", user_goals)
        score_difference = abs(user_goals - pc_goals)
        show_score(user_goals, pc_goals)
    
        """
        Lógica para saber si ya con el gol del usuario y con la diferecia de goles tiene la victoria asegurada.
        """

        if remaining_rounds < score_difference and rounds < 5:
            continue   

        pc_goals = update_score("Ataje el penal", "Paises Bajos", "Argentina", pc_goals)
        score_difference = abs(user_goals - pc_goals)
        show_score(user_goals, pc_goals)
        
        rounds += 1
        remaining_rounds -= 1

    if user_goals > pc_goals:
        print(f'\nArgentina ganó {user_goals} a {pc_goals}')
        print("ARGENTINA GANA SU PRIMERA MEDALLA DE ORO OLIMPICA EN EL HOCKEY FEMENINO!!!\n")
    else:
        print(f"\nPaises Bajos ganó {pc_goals} a {user_goals}")
        print("Victoria de Países Bajos... gana su 5ta medalla de oro... Argentina se queda con su 4ta medalla de plata...\n")


'''
Llamado de funciones para proporcionar contexto al usuario e inicializar el programa principal.
'''

context()
play_penalties()
