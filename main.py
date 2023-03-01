"""Fichier pricipal du programme"""

from models.player import Player
from models.tournoi import Tournoi

# Function qui creer de nouveau joueurs
def create_player(last_name, first_name, date_of_birth, sexe):
    new_player = Player(last_name, first_name, date_of_birth, sexe)
    dict_player= {"last_name": new_player.last_name,
                    "first_name": new_player.first_name,
                    "date_of_birth": new_player.date_of_birth,
                    "sexe": new_player.sexe,
                    "points": new_player.points,
                    "classement": new_player.classement}
    return dict_player

# Creer les joueurs via une boucle
create_players=str(input("voulez vous créer des joueurs (O/N)? "))
nb_players = 1
players_list=[]
if create_players=='O' or create_players=="o":
    for i in range(nb_players):
        print('----------------------------------------------------')
        print(f'Creation du joueur {i+1}')
        last_name = str(input('Entrer votre nom : '))
        first_name = str(input('Entrer maintenant votre prenom : '))
        date_of_birth = str(input('Entrer votre date de naissance :'))
        sexe = str(input('Vous etes un Homme ou une Femme ? '))

        dict_player=(last_name, first_name, date_of_birth, sexe)
        players_list.append(dict_player)

print("--------------------------------")
print("############# Players list #########")
print(players_list)


# Creation du tournoi
def create_new_tournoi(name, place, date, players, director_remark, rounds=[], nombres_tours=4):
    tournoi = Tournoi(name, place, date, players, rounds, nombres_tours, director_remark)
    dict_tournoi=       {"name": tournoi.name,
                          "place": tournoi.place,
                          "date": tournoi.date,
                          "players":tournoi.joueurs,
                          "rounds":tournoi.rounds,
                          "nombres_tours": tournoi.nombres_tours,
                          "director_remark": tournoi.director_remark}
    return dict_tournoi

create_tournement= str(input('Voulez vous creer du nouveau tournoi (O/N)? '))
if create_tournement=='O' or create_tournement=="o":
    print("---------------------------------------------------------")
    print("Creation du Tournoi")
    name = str(input("Entrer un nom de Tournoi : "))
    place = str(input("Entrer le lieu du Tournoi : "))
    date = str(input("Entrer la date du Tournoi : "))
    director_remark = str(input("Remarques du directeur du Tournoi : "))
    dict_tournoi=create_new_tournoi(name, place, date, players_list, director_remark)
    print("------------------------------")
    print("############ Tournement infos #############")
    print(dict_tournoi)