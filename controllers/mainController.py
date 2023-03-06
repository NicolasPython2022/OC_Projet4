'''
Tous le projet a est un ensemble de module,
chaque dossier est un module de fichier.py et chaque fichier .py est un package.
On a implenter en ligne de commande, la commande "export PYTHONPATH=$PYTHONPATH:/Users/dwwm/OC_Projet4/"
'''
from models import player
from models import tournoi
from views import mainView as view


def control_user_data():
    # La function me return la liste des joueurs avec la liste de tournoi
    players_list, dict_tournoi = view.get_user_data()

    # print(players_list)
    # print(dict_tournoi)


    # Ici on instancie les objets de la class Player chaque player est representer par un dictionnaire
    players = []

    # Boucle qui instancie chaque player avec un objet
    for dict_player in players_list:
        last_name = dict_player['last_name']
        first_name = dict_player['first_name']
        date_of_birth = dict_player['date_of_birth']
        sexe = dict_player['sexe']

        # J'instancie maintenant l'objet de la class Player avec ses attributs.
        objet_player = player.Player(last_name,
                                    first_name, 
                                    date_of_birth,
                                    sexe)
        # Ici j'ajoute a ma liste l'objet de type de la class Player
        players.append(objet_player)



    # Pas besoin de cree une liste de tournoi car nous n'en avons qu'un seul
    # Ici je recuperes les valeurs du dictionnaire peut importe l'ordre d'ecriture
    name = dict_tournoi['name']
    place = dict_tournoi['place']
    date = dict_tournoi['date']
    director_remark = dict_tournoi['director_remark']
    rounds = []
    nombres_tours = 4

    # Instanciation de la class Tournoi, en respectant l'ordre des attributs
    objet_tournoi = tournoi.Tournoi(name,
                                    place, 
                                    date,
                                    players,
                                    rounds,
                                    nombres_tours,
                                    director_remark)
    
    return players, objet_tournoi