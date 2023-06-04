from models import player
from views import main_view
import random
import json
import os


class Controller:
    def __init__(self):
        self.view = main_view.View()
        self.data_path = "data.json"

    def get_players_infos(self, players_dict):
        players = []
        # Boucle qui instancie chaque player avec un objet
        for dict_player in players_dict.values():
            last_name = dict_player["last_name"]
            first_name = dict_player["first_name"]
            date_of_birth = dict_player["date_of_birth"]
            sexe = dict_player["sexe"]
            last_visited_players = dict_player["last_visited_players"]
            # J'instancie maintenant l'objet de class Player avec ses attributs
            objet_player = player.Player(
                last_name,
                first_name,
                date_of_birth,
                sexe,
                last_visited_players=last_visited_players,
            )
            # Ajout de l'objet de type de class Player a ma liste "players"
            players.append(objet_player)
        return players

    def update_players_classement(self, players):
        classement_players = []
        points_list = []
        # Boucle de mes joueurs qui classifie la list
        # des points avec la method sorted()
        for p in players:
            nb_points = p.points
            points_list.append(nb_points)
        points_list = sorted(points_list, reverse=True)
        list_players = players
        # Boucle qui classifie la list des joueurs selon leurs nb de points
        for i in range(len(points_list)):
            for p in list_players:
                # condition sur le points si le nb de points du joueurs est
                # egal aux nbs de points extraits de la liste de points classer
                if p.points == points_list[i]:
                    classement_players.append(p)
                    p.classement = i + 1
                    list_players.remove(p)
                    break
        return classement_players

    def play_match(self, player1, player2):
        score1, score2 = self.view.create_score(player1, player2)
        # Condition d'attribution du point gagnant, du perdant et du match nul
        if score1 > score2:
            player1.points += 1
        elif score1 < score2:
            player2.points += 1
        else:
            player1.points += 0.5
            player2.points += 0.5

        return player1, player2

    def play_round(self, players):
        '''Boucle sur la longueur de ma liste de joueur en y ajoutant -1
           afin de stopper l'iteration a 7 car le nombre 8 est Exclut '''
        for i in range(len(players) - 1):
            player1 = players[i]
            for j in range(i + 1, len(players)):
                player2 = players[j]
                if (
                    player2.last_name + " " + player2.first_name
                    not in player1.last_visited_players
                ):
                    print("Resultats du match", i + 1)
                    # Jouer un match
                    player1, player2 = self.play_match(player1, player2)
                    '''J'ajoute a ma liste de matchs[] mon objet_match et
                       donc ses valeurs '''
                    player1.last_visited_players.append(
                        player2.last_name + " " + player2.first_name
                    )
                    player2.last_visited_players.append(
                        player1.last_name + " " + player1.first_name
                    )
                    print("------------------------------")
                    break
        return players

    def save_players_results(self, classement_players):
        # Enregistrer les résultats des joueurs dans un dictionnaire
        dict_players = {}
        for i in range(len(classement_players)):
            player_dict = {}
            player_dict["last_name"] = classement_players[i].last_name
            player_dict["first_name"] = classement_players[i].first_name
            player_dict["date_of_birth"] = classement_players[i].date_of_birth
            player_dict["sexe"] = classement_players[i].sexe
            player_dict["classement"] = classement_players[i].classement
            player_dict["last_visited_players"] = classement_players[
                i
            ].last_visited_players
            player_dict["points"] = classement_players[i].points
            dict_players[str(i + 1)] = player_dict
        return dict_players

    def start_tournement(self, dict_tournement):
        # Je recupere les valeurs du dict peut importe l'ordre d'écriture
        last_played_round = dict_tournement["last_played_round"]
        n_rounds = dict_tournement["nombre_rounds"]

        '''Boucle for sur attribut de class Round,
           avec range() parametrer des n_rounds '''
        for k in range(last_played_round + 1, n_rounds):
            players_dict = dict_tournement["players"]

            # Infos de joueurs
            players = self.get_players_infos(players_dict)

            # Jouer un tour
            if k == 0:
                random.shuffle(players)
            name = "Round " + str(k + 1)
            print(f"Nom du Round : {name}")
            #
            players = self.play_round(players)

            # Classer les joueurs selon leurs classements
            classement_players = self.update_players_classement(players)

            # enregistrer les résultats des joueurs
            dict_players = self.save_players_results(classement_players)
            dict_tournement["players"] = dict_players
            dict_tournement["last_played_round"] = k

            if k != n_rounds - 1:
                input_user = self.view.stop_and_start_tournement()
                if input_user.capitalize() == "N":
                    break
        return dict_tournement

    def create_tournement(self):
        # Créer un touroi dans le fichier json
        new_data_tournement = {}
        data_tournement = self.view.get_data_tournoi()
        nb_players = data_tournement["nombre_players"]
        dict_players = self.view.get_player_data(nb_players)
        data_tournement["players"] = dict_players
        new_data_tournement["1"] = data_tournement
        if os.path.exists(self.data_path):
            with open(self.data_path, "r") as f:
                history_tournement = json.load(f)
            last_tournement_key = int(list(history_tournement.keys())[-1])
            history_tournement[str(last_tournement_key + 1)] = data_tournement
            new_data_tournement = history_tournement

        with open(self.data_path, "w") as f:
            json.dump(new_data_tournement, f)

    def display_tournement_infos(self):
        with open(self.data_path, "r") as f:
            data_tournement = json.load(f)
        # display tournement infos
        self.view.display_tournement_infos(data_tournement)
