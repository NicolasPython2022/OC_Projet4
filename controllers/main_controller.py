from models import player
from models import tournoi
from models import round
from models import match
from views import main_view
import random
import json
import os
# Import du type de base pour la date et l'heure
from datetime import datetime


# Mehode d'obtention de l'horodatage
def get_timestamp():
    # now()methode qui donne la date et le temps actuel
    date_complet = datetime.now()
    date = date_complet.strftime("%d/%m/%Y")
    heure = date_complet.strftime("%H:%M")
    return date, heure


class Controller:

    def __init__(self):
        self.view = main_view.View()
        self.data_path = "data.json"

    def get_players_infos(self, players_dict):
        players = []
        # Boucle qui instancie chaque player avec un objet
        for dict_player in players_dict.values():
            last_name = dict_player['last_name']
            first_name = dict_player['first_name']
            date_of_birth = dict_player['date_of_birth']
            sexe = dict_player['sexe']
            last_visited_players = dict_player['last_visited_players']
            # J'instancie maintenant l'objet de class Player avec ses attributs.
            objet_player = player.Player(last_name,
                                         first_name,
                                         date_of_birth,
                                         sexe,
                                         last_visited_players=last_visited_players)
            # Ajout de l'objet a ma liste "players"
            players.append(objet_player)
        return players

    def play_round(self, players, matchs=[]):
        # Boucle sur la longueur de ma liste de joueur en y ajoutant -1 afin de stopper l'iteration a 7 car le nombre 8 est "Exclut"
        for i in range(len(players)-1):
            player1 = players[i]

            for j in range(i+1, len(players)):
                player2 = players[j]
                if player2.last_name + " " + player2.first_name not in player1.last_visited_players:
                    # Je donne une valeur a mon score
                    print('Resultats du match', i+1)
                    # J'appel les valeurs retourner de ma methode de la view en n'oubliant pas d'indiquer ses params.
                    score1, score2 = self.view.create_score(
                        player1, player2)
                    # match_ est un tuple de deux liste contenant 2 valeurs, un joueur et un score
                    match_ = ([player1, score1], [player2, score2])
                    # Condition d'attribution du point gagnant, du perdant et du match nul
                    if score1 > score2:
                        player1.points += 1
                    elif score1 < score2:
                        player2.points += 1
                    else:
                        player1.points += 0.5
                        player2.points += 0.5

                    # Creation de l'objet_match en instanciant ma class Match qui est parametrer de mon tuple a deux listes
                    objet_match = match.Match(match_)

                    # J'ajoute a ma liste de matchs[] mon objet_match et donc ses valeurs
                    matchs.append(objet_match)
                    player1.last_visited_players.append(
                        player2.last_name+" "+player2.first_name)
                    player2.last_visited_players.append(
                        player1.last_name+" "+player1.first_name)
                    print('------------------------------')
                    break
        return matchs, players

    def update_players_classement(self, players):
        classement_players = []
        points_list = []
        # Boucle de mes joueurs qui classifie la list des points avec la method sorted()
        for p in players:
            nb_points = p.points
            points_list.append(nb_points)
        # print(points_list)
        # sorted() pour mettre en ordre croissant, reverse pour inverser
        points_list = sorted(points_list, reverse=True)

        # print(points_list)

        list_players = players
        # Boucle qui classifie la list des joueurs selon leurs nb de points
        for i in range(len(points_list)):
            for p in list_players:
                # condition sur le points si le nb de points du joueurs est egal aux nbs de points extraits de la liste de points classer
                if p.points == points_list[i]:
                    classement_players.append(p)
                    p.classement = i+1
                    list_players.remove(p)
                    break
        return classement_players

    # Enregistrer les résultats des joueurs
    def save_players_result(classement_players):
        dict_players = {}
        for i in range(len(classement_players)):
            player_dict = {}
            player_dict["last_name"] = classement_players[i].last_name
            player_dict["first_name"] = classement_players[i].first_name
            player_dict["date_of_birth"] = classement_players[i].date_of_birth
            player_dict["sexe"] = classement_players[i].sexe
            player_dict["classement"] = classement_players[i].classement
            player_dict["last_visited_players"] = classement_players[i].last_visited_players
            player_dict["points"] = classement_players[i].points
            dict_players[str(i+1)] = player_dict
        return dict_players

    # Demarrer un tournoi
    def start_tournement(self, dict_tournement):
        # Ici je recupere les valeurs du dictionnaire peut importe l'ordre d'ecriture
        last_played_round = dict_tournement['last_played_round']
        n_rounds = dict_tournement['nombre_rounds']

        # Boucle for des attributs de la class Round avec la method range() parametrer des nbs de tours
        for i in range(last_played_round+1, n_rounds):
            players_dict = dict_tournement['players']
            # Recuperer les infos de joueurs et les transformer en type de l'objet players_dict
            players = self.get_players_infos(players_dict)
            if i == 0:
                # methode de classement aleatoire des joueurs
                random.shuffle(players)
            name = "Round " + str(i+1)
            date_debut, heure_debut = get_timestamp()
            matchs = []

            print(f'Nom du Round : {name}')

            matchs, players = self.play_round(players, matchs=[])
            # Classer les joueurs selon leur classement
            classement_players = self.update_players_classement(players)
            # Enregister les resultats des joueurs
            dict_players = self.update_players_dict(classement_players)
            dict_tournement["players"] = dict_players
            dict_tournement["last_played_round"] = i

            date_fin, heure_fin = get_timestamp()
            # Creation de l'objet "tour"
            tour = round.Round(name, matchs, date_debut,
                               heure_debut, date_fin, heure_fin)
            tour.display_result()
            # demander à l'utilisateur s'il veut continuer ou arreter le tournoi dans ce tour
            # mettre moi un nouveau variable qui va prendre la valeur de l'input
            if i != n_rounds-1:
                input_user = self.view.stop_and_start_tournement()
                if input_user.capitalize() == 'N':
                    break
        return dict_tournement

    def create_tournement(self):
       # créer un touroi dans le fichier json
        new_data_tournement = {}
        data_tournement = self.view.get_data_tournoi()
        nb_players = data_tournement["nombre_players"]
        dict_players = self.view.get_player_data(nb_players)
        data_tournement['players'] = dict_players
        new_data_tournement['1'] = data_tournement
        if os.path.exists(self.data_path):
            with open(self.data_path, 'r') as f:
                history_tournement = json.load(f)
            last_tournement_key = int(list(history_tournement.keys())[-1])
            history_tournement[str(
                last_tournement_key+1)] = data_tournement
            new_data_tournement = history_tournement

        with open(self.data_path, 'w') as f:
            json.dump(new_data_tournement, f)

    def display_tournement_infos(self):
        with open(self.data_path, 'r') as f:
            data_tournement = json.load(f)
        # display tournement infos
        self.view.display_tournement_infos(data_tournement)
