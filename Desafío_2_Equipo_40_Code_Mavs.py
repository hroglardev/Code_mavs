'''
[
  {
    'Australia': [
    {'numero': '10', 'nombre': ' Katrina Powell', 'cantidad_pases': 454, 'pases_bien': 243, 'pases_mal': 211, 'porcentaje': 53.52}, 
    {'numero': '9', 'nombre': 'Madonna Blyth’', 'cantidad_pases': 444, 'pases_bien': 236, 'pases_mal': 208, 'porcentaje': 53.15}, …]
  }, 
  {
    'Argentina': [
    {'numero': '7', 'nombre': 'Agustina Gorzelany', 'cantidad_pases': 449, 'pases_bien': 250, 'pases_mal': 199, 'porcentaje': 55.68}, 
    {'numero': '15', 'nombre': 'Luciana Aymar', 'cantidad_pases': 466, 'pases_bien': 251, 'pases_mal': 215, 'porcentaje': 53.86}, …]
  }
]
'''


     

team_to_dict = {}

def find_player(name, team, number):
  player_exists = any(name in dictionary.values() for dictionary in team)
  if not player_exists: 
      team_to_dict[team].append({
        "numero": number,
        "nombre": name,
        "cantidad_pases": 0,
        "pases_bien": 0,
        "pases_mal": 0,
        "porcentaje": 0,
     })
  return [item for item in team if item.get("nombre") == name][0]


def savePlayer(team, number, name, pass_status, time):
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


def contar_pases_y_efectividad():
  with open("pases.txt", 'r') as file:
      for i in file:
          team, number, name, pass_status, time = i.split(';')
          savePlayer(team, number, name, pass_status, time)

  return [{key: value} for key, value in team_to_dict.items()]

contar_pases_y_efectividad()


