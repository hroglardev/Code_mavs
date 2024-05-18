teams = {}

def contar_pases_y_efectividad():
  '''
  Función abre el archivo de registros de pases e itera cada linea de este.
  Por cada linea utiliza el caracter ";" para dividir los datos en una lista en la cual cada posición representa cada dato y se utiliza un .split() para separar a estos datos.

  Actualiza los datos del jugador correspondiente utilizando la función de save_player.
  Una vez que finaliza de cargar los datos de todos los jugadores y sus pases, ordena los datos utilizando la función de sort_players_by_pass_efficiency.

  Por ultimo la función toma el diccionario de equipos y por cada par clave: valor, crea un diccionario individual los cuales seran devueltos dentro de una lista.

  La función arrojara un error por consola en caso de haber un problema en la apertura del archivo de datos.

  Valor de retorno:
    [
      {team_1: [{},{},...]},
      {team_2: [{},{},...]}
    ]
  Tipo de dato de retorno:
    Lista de diccionarios de equipos cuyo valor es una lista de diccionarios de jugadores.
  '''
  try:
    with open("pases.txt", 'r') as file:
      for i in file:
        team, number, name, pass_status, _ = i.split(';')
        save_player(name, team, number, pass_status)
    
    sort_players_by_pass_efficiency()
    print("Registro de pases creado con éxito")
    return [{key: value} for key, value in teams.items()]
  except Exception as err:
    print(f"Hubo un problema: {err}")
    

def find_player(name, team, number):

  '''
  Esta función recibe 3 parámetros:
    name (string): nombre del jugador.
    team (string) equipo del jugador.
    number (string) número de camiseta del jugador.

  La función chequea si alguna de las posiciones de las listas del diccionario pasado por parametro contiene un nombre que coincida con el nombre pasado por parametro y si este no existe lo crea en el diccionario del equipo correspondiente con sus estadisticas inicializadas en 0.
  

  Valor de retorno:
    {numero: number, nombre: name, cantidad_pases: 0 o valor actual, pases_bien: 0 o valor actual, pases_mal: 0 o valor actual, porcentaje: 0 o valor actual}
  Tipo de dato de retorno:
    Diccionario
  '''

  player_exists = any(player.get("nombre") == name for player in team)
  if not player_exists: 
    team.append({
      "numero": number,
      "nombre": name,
      "cantidad_pases": 0,
      "pases_bien": 0,
      "pases_mal": 0,
      "porcentaje": 0,
    })

  return [item for item in team if item.get("nombre") == name][0]

def save_player(name, team, number, pass_status):

  '''
  Esta función recibe 4 parámetros:
    name (string): nombre del jugador.
    team (string) equipo del jugador.
    number (string) número de camiseta del jugador.
    pass_status (string) estado del pase 0 errado, 1 acertado

  Función para guardar los jugadores en sus respectivos equipos y actualizar sus datos y estadísticas de pases.
  Lo primero que hace es consultar con un if si el equipo ya se encuentra agregado o si hay que agregarlo (se inicializa el equipo con un lista vacio de jugadores. Se resolvio de esta manera para contemplar casos de mas de dos equipos), luego con la función find_player busca al jugador correspondiente y al final recorre el lista de jugadores que tiene el equipo con una busqueda lineal para poder encontrar al jugador que se requiere y actualiza los pases totales, el porcentaje de pases acertados y sus pases exitosos/fallidos dependiendo del status del mismo pasado por parametro.

  El bucle dejara de iterar una vez que el jugador sea encontrado y sus datos hayan sido actualizados.
  '''

  if team not in teams:
    teams[team] = []
  
  target_player = find_player(name, teams[team], number)
  for player in teams[team]:
    if target_player["nombre"] == player["nombre"]:
      player["cantidad_pases"] += 1
      if pass_status == "1":
        player["pases_bien"] += 1
      else:
        player["pases_mal"] += 1
      player["porcentaje"] = round((player["pases_bien"] * 100) / player["cantidad_pases"], 2)
      break

def sort_players_by_pass_efficiency():

  '''
  Función que itera el diccionario de equipos y en cada lista de jugadores, los ordena segun su porcentaje de efectividad de pases en orden descendente.
  '''

  for team in teams:
    teams[team] = sorted(teams[team], key=lambda player: player["porcentaje"], reverse=True)

contar_pases_y_efectividad()