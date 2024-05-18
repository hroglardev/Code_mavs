import random



# Equipo Argentino

pl_arg = [
    ("Clara Barberi", 26),
    ("Cristina Cosentino", 13),
    ("Juana Castellaro", 50),
    ("Agustina Gorzelany", 3),
    ("Valentina Raposo", 4),
    ("Victoria Miranda", 29),
    ("Stefania Antoniazzi", 36),
    ("Victoria Sauze", 18),
    ("Agostina Alonso", 5),
    ("Sofia Toccalino", 2),
    ("Sofia Cairo", 20),
    ("Rocio Sanchez", 17),
    ("Catalina Andrade", 45),
    ("Eugenia Trinchinetti", 22),
    ("Celina Di Santo", 24),
    ("Julieta Jankunas", 28),
    ("Victoria Manuele", 19),
    ("Maria Granatto", 10),
    ("Agustina Albertarrio", 7),
    ("Maria Campoy", 26),
    ("Lara Casas", 61),
    ("Zoe Diaz", 55),
    ("Valentina Marcucci", 31),
    ("Delfina Thome", 11)
]

# Equipo Australiano

pl_aus = [
    ("Alice Arnott", 11),
    ("Jocelyn Bartram", 19),
    ("Maddison Brooks", 8),
    ("Jane Claxton", 18),
    ("Claire Colwill", 1),
    ("Rebecca Greiner", 29),
    ("Greta Hayes", 12),
    ("Stephanie Kershaw", 14),
    ("Amy Lawton", 4),
    ("Rosie Malone", 2),
    ("Kaitlin Nobbs", 15),
    ("Brooke Peris", 3),
    ("Aleisha Power", 7),
    ("Hattie Shand", 13),
    ("Lucy Sharman", 17),
    ("Karri Somerville", 20),
    ("Penny Squibb", 6),
    ("Grace Stewart", 30),
    ("Tatum Stewart", 22),
    ("Renee Taylor", 21),
    ("Mariah Williams", 24),
    ("Grace Young", 5),
    ("Dayle Dolkens", 52),
    ("Shanea Tonkin", 9)
]


teams = [
  ("Argentina", pl_arg),
  ("Australia", pl_aus)
]


records_amount = 50000

def generate_pass_status ():
  '''
  Esta función hace uso del módulo random
  para generar un número entre el 0 y el 1 que marcara si
  el pase fue exitoso o no.

  Valor de retorno:
    0: Fallido
    1: Exitoso
  Tipo de dato de retorno:
    Número entero = int
  '''
  return random.randint(0, 1)

def generate_minute ():
  '''
  Se utiliza el módulo random para genenerar
  un número entre el 0 y el 60 simulando los minutos
  de juego de un partido de hockey standard.

  Valor de retorno:
    0 - 60
  Tipo de dato de retorno:
    Número entero = int
  '''

  return random.randint(0, 60) 

def pass_entry (team, player, pass_status, minute):
  '''
  Esta función toma 4 paramentros:
    team (string): equipo al que pertenece la jugadora que realizó el pase.
    player (tupla de dos posiciones): jugadora que realizó el pase. 
      En la primera posición se encuentra el nombre de la jugadora.
      En la segunda posición se encuentra su número de camiseta.
    pass_status (int): Valor de 0 o 1.
    minute (int): Valor de 0 a 60.
  
  Valor de retorno:
    Equipo;número de camiseta;nombre del jugador;resultado del pase; minuto del juego;
  Tipo de dato de retorno:
    String
  '''

  return f"{team};{player[1]};{player[0]};{pass_status};{minute}"

def create_registries():
  '''
  Función para crear registro de pases.

  La función intentará realizar lo siguiente:

  Utilizando la función open para abrir el archivo en el que se guardaran los registros de los pases.
  La función entra en un bucle a ejecutarse un numero de veces preestablecido.
  Por cada iteración guardara un registro de pase en el archivo abierto.
  Al finalizar el proceso, le indicara al usuario la finalización a traves de un mensaje por consola.

  Si el programa encuentra algun error al abrir el archivo, se mostrará un mensaje por consola indicando la falla.

  '''

try:
  with open('pases.txt', "w") as match:
    for i in range(records_amount):
        random_team = random.choice(teams)
        random_player = random.choice(random_team[1])
        registry = pass_entry(random_team[0], random_player, generate_pass_status(), generate_minute())
        match.write(f'{registry}' + '\n')
  print("Registro de pases creado con éxito")
except Exception as err:
  print(f"Hubo un problema: {err}")

 
'''
Llamado a la función para correr el programa y crear/guardar los registros de pases.
'''
create_registries()





  