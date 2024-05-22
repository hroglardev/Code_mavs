import random



def generate_computer_choice():
    return random.randint(1, 9)

def generate_player_choice(instruction):
    player_choice = int(input(f"\n{instruction} 1-9: "))
    while player_choice < 1 or player_choice > 9:
        player_choice = int(input(f"Debe seleccionar una zona de portería entre 1 y 9: "))
    return player_choice
    
def take_turn(instruction, kicker, goalie):
    player_choice = generate_player_choice(instruction)
    computer_choice = generate_computer_choice()
    # funcion para testear escenarios posibles eligiendo el valor de la maquina
    # computer_choice = int(input("score de la maquina ")) 
    # print(f"El jugador eligio {player_choice}, la maquina eligio {computer_choice}")
    if player_choice in (2, 5, 8) and computer_choice in (2, 5, 8) or player_choice == computer_choice:
        print(f"{goalie} atajo el gol")
        return False
    else:
        print(f"GOOOOOL DE {kicker}!!")
        return True
    
def update_score(instruction, kicker, goalie, score_kicker):
    turn_result = take_turn(instruction, kicker, goalie)
    if turn_result:
        score_kicker += 1
    return score_kicker


def play_penalties():
    user_goals = 0
    pc_goals = 0
    score_difference = 0
    rounds = 0
    remaining_rounds = 5

    while (remaining_rounds >= score_difference) or (rounds >= 5 and score_difference == 0):

        user_goals = update_score("Dispare al arco", "Argentina", "Paises Bajos", user_goals)
        score_difference = abs(user_goals - pc_goals)
        print(f"El score es Argentina: {user_goals}, Paises Bajos: {pc_goals}")
    
        if remaining_rounds < score_difference and rounds < 5:
            continue   

        pc_goals = update_score("Ataje el penal", "Paises Bajos", "Argentina", pc_goals)
        score_difference = abs(user_goals - pc_goals)
        print(f"El score es Argentina: {user_goals}, Paises Bajos: {pc_goals}")
        
        rounds += 1
        remaining_rounds -= 1

    if user_goals > pc_goals:
        print(f'Gano Argentina {user_goals} a {pc_goals}')
    else:
        print(f'Gano Paises Bajos {pc_goals} a {user_goals}')


play_penalties()






