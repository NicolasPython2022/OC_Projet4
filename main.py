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

#print(tournement.__dict__)



# Premier Round
name = "Round 1"
matchs = []
# Boucle for sur la longueur de ma liste de joueur en y ajoutant -1 afin de stopper l'iteration arriver 7 car le nombre 8 n'est pas comptabiliser
for i in range(len(players)-1):
    # Ici je choisi le joueur qui jouera le match en appellant son indice
    player1 = players[i]
    player2 = players[i+1]
    # Je donne une valeur a mon score
    score1 = 5
    score2 = 3
    # La var match1 est un tuple de deux liste contenant 2 valeurs, un joueur et un score
    match1 = ([player1,score1],[player2,score2])
    # J'instancie ma class Match en lui passant en attribut mon tuple de liste
    objet_match = match.Match(match1)
    # J'ajoute a ma liste l'instanciation de mon objet
    matchs.append(objet_match)
    print(objet_match)


classement_players = []
points_list = []
# Boucle de mes joueurs qui classifi la list des points avec la methgod sorted()
for player in players:
    nb_points = player.points
    points_list.append(nb_points)
points_list=sorted(points_list)
list_players=players
# Bouckle qui classifi la list des joueurs selon leurs nb de points
for i in range(len(points_list)):
    for player in list_players: 
        # condition sur le points si le nb de points du joueurs est egal au nb de points extraits de la liste de points classer
        if player.points==points_list[i]:
            classement_players.append(player)
            player.classement=i+1
            list_players.remove(player)
            break
# Juste pour afficher le classement
for player in classement_players:
    print(player)
            
    




date_debut = "23/04/23"
heure_debut = "14h00"
date_fin = "30/04/23"
heure_fin = "17h00"

tour = round.Round(name,matchs,date_debut,heure_debut,date_fin,heure_fin)

