'''
Le fichier main.py comporte la logique de mon programme, appel des methods de mes functions.
'''

from controllers import main_controller
from models import match
from models import round
'''
1 - Instanciation du controllers.
2 - Appel de la method qui recupere les infos d'un joueur : controller.view.get_player_data()
'''

# Instance de controller avec appel de class du fichier
controller = main_controller.Controller()




# Appel method de class ControlPlayer() du modul "controllers", avec en params ma liste de players
players = controller.get_player()



# Deplacer ce code dans la view en creant une method d'affichage
for player in players:
    print(player.last_name)
    print(player.first_name)
    print(player.date_of_birth)
    print(player.sexe)


tournement = controller.get_tournoi()

if tournement != None:
    print(tournement.name)
    print(tournement.place)
    for round in tournement.rounds:
        print(round.name)

#print (tournement.__dict__)

# Premier Round
name = "Round 1"
# Liste de mes matchs
matchs = []
# un dictionnaire qui comprends des keys de joueurs et des values qui sont les joueurs avec qui le joueur a deja joueurs
last_visited_players = {}
# boucle for pour construire
for player in last_visited_players:
    last_visited_players[player] = []
    
# Boucle sur la longueur de ma liste de joueur en y ajoutant -1 afin de stopper l'iteration a 7 car le nombre 8 est "Exclut"
for i in range(len(players)-1):
    player1 = players[i]
    player2 = players[i+1]
    # Je donne une valeur a mon score
    print('Resultats du match',i+1)
    score1 = int(input(f'score du joueur {player1.first_name}:' ))
    score2 = int(input(f'score du joueur {player2.first_name}:'))
    
    # La var match1 est un tuple de deux liste contenant 2 valeurs, un joueur et un score
    match_ = ([player1,score1],[player2,score2])
    # Creation de l'objet_match en instanciant ma class Match qui est parametrer de mon tuple des deux listes
    objet_match = match.Match(match_)
    objet_match.add_points()

    # J'ajoute a ma liste de matchs[] mon objet_match et donc ses valeurs
    matchs.append(objet_match)
    print(objet_match)
    print('------------------------------')


classement_players = []
points_list = []
# Boucle de mes joueurs qui classifie la list des points avec la method sorted()
for player in players:
    nb_points = player.points
    points_list.append(nb_points)
#print(points_list)

points_list=sorted(points_list,reverse=True)
#print(points_list)

list_players=players
# Boucle qui classifie la list des joueurs selon leurs nb de points
for i in range(len(points_list)):
    for player in list_players: 
        # condition sur le points si le nb de points du joueurs est egal aux nbs de points extraits de la liste de points classer
        if player.points==points_list[i]:
            classement_players.append(player)
            player.classement=i+1
            list_players.remove(player)
            break
# Boucle  pour afficher le classement
for player in classement_players:
    print(player)

  




date_debut = "23/04/23"
heure_debut = "14h00"
date_fin = "30/04/23"
heure_fin = "17h00"

tour = round.Round(name,matchs,date_debut,heure_debut,date_fin,heure_fin)

