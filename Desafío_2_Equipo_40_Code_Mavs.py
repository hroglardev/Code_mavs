team_to_dict = {}

def find_player(name, team, number):
  '''
  Función que recibe nombre del jugador, nombre del equipo y número de camiseta.
  La función chequea si alguno de los valores de las posiciones de las listas del diccionario pasado por parametro contiene un nombre que coincida con el nombre pasado por parametro.

  En caso de no encontrar coincidencia, procedera a crear un nuevo diccionario en la lista del equipo representando al nuevo jugador con sus variables iniciales.

  Luego devuelve el diccionario representativo del jugador creado o en caso de haberlo encontrado inicialmente, el jugador encontrado con sus variables actuales.

  Valor de retorno:
    {numero: number, nombre: name, cantidad_pases: 0 o valor actual, pases_bien: 0 o valor actual, pases_mal: 0 o valor actual, porcentaje: 0 o valor actual}
  Tipo de dato de retorno:
    Diccionario
  '''
  player_exists = any(name in dictionary.values() for dictionary in team)
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



def savePlayer(team, number, name, pass_status):

  '''
  La función recibe nombre del equipo, número de camiseta, nombre del jugador, status del pase.

  Itera sobre el diccionario base para comprobar que el equipo exista y en caso contrario añadir una propiedad con el nombre del equipo con un valor de una lista vacía.

  Utilizando la función find_player encuentra el jugador cuyos datos se deben actualizar.

  La función itera la lista de jugadores del equipo que corresponde hasta encontrar un match entre el nombre en la variable target_player y el nombre de la posición sobre la cual se encuentra el bucle.
  Una vez encontrado el jugador, actualiza los pases totales y sus pases exitosos/fallidos dependiendo del status del mismo pasado por parametro.

  Al final actualiza el porcentaje de efectividad de pases.

  La función no posee valor de retorno ya que es utilizada para actualizar información.
  '''
  if team not in team_to_dict:
    team_to_dict[team] = []
  
  target_player = find_player(name, team_to_dict[team], number)
  for player in team_to_dict[team]:
     if target_player["nombre"] == player["nombre"]:
        player["cantidad_pases"] += 1
        if pass_status == "1":
           player["pases_bien"] += 1
        else:
           player["pases_mal"] += 1
        player["porcentaje"] = round((player["pases_bien"] * 100) / player["cantidad_pases"], 2)


def sort_players_by_pass_efficiency():
   '''
   La función itera el diccionario de equipos y en cada lista de jugadores, los ordena segun su porcentaje de efectividad de pases en orden descendente.
   '''
   for team in team_to_dict:
      team_to_dict[team] = sorted(team_to_dict[team], key=lambda player: player["porcentaje"], reverse=True)

def contar_pases_y_efectividad():
  '''
  La función abre el archivo de registros de pases e itera cada linea de este.
  Por cada linea utiliza el caracter ";" para dividir los datos en una lista en la cual cada posición representa cada dato.

  Actualiza los datos del jugador correspondiente utilizando la función de savePlayer.
  Una vez que finaliza de cargar los datos de todos los jugadores y sus pases, ordena los datos utilizando la función de sort_players_by_pass_efficiency.

  Por ultimo la función toma el diccionario de equipos y por cada par clave: valor, crea un diccionario individual los cuales seran devueltos dentro de una lista.

    
  Tipo de dato de retorno:
    Lista de diccionarios de equipos cuyo valor es una lista de diccionarios de jugadores.
  '''

  with open("pases.txt", 'r') as file:
      for i in file:
          team, number, name, pass_status, _ = i.split(';')
          savePlayer(team, number, name, pass_status)
  
  sort_players_by_pass_efficiency()
  return [{key: value} for key, value in team_to_dict.items()]




contar_pases_y_efectividad()








