from models import player
from models import tournoi
from models import round
from models import match
from views import main_view
import random
import json
# Import du type de base pour la date et l'heure
from datetime import datetime


# Mehode d'obtention de l'horodatage
def get_timestamp():
    # now()methode qui donne la date et le temps actuels
    date_complet = datetime.now()
    date = date_complet.strftime("%d/%m/%Y")
    heure = date_complet.strftime("%H:%M")
    return date, heure


class Controller:

    def __init__(self):
        self.view = main_view.View()

        self.players = []

    # Tjrs mettre un verbe explicite pr les methods
    def get_player(self):
        players_list = self.view.get_player_data()
        players = []

        # Boucle qui instancie chaque player avec un objet
        for dict_player in players_list:
            last_name = dict_player['last_name']
            first_name = dict_player['first_name']
            date_of_birth = dict_player['date_of_birth']
            sexe = dict_player['sexe']

            # J'instancie maintenant l'objet de class Player avec ses attributs.
            objet_player = player.Player(last_name,
                                         first_name,
                                         date_of_birth,
                                         sexe)
            # Ajout de l'objet de type de class Player a ma liste "players"
            players.append(objet_player)

        self.players = players

    def get_tournoi(self):

        # Ce qui est retourner par la view est stocker dans un dictionnaire "dict_tournoi"
        # dict_tournoi = self.view.get_data_tournoi()
        dict_tournoi = json.load('data.json')

        players_dict = dict_tournoi['players']
        players = []

        # Boucle qui instancie chaque player avec un objet
        for dict_player in players_dict.values():
            last_name = dict_player['last_name']
            first_name = dict_player['first_name']
            date_of_birth = dict_player['date_of_birth']
            sexe = dict_player['sexe']

            # J'instancie maintenant l'objet de class Player avec ses attributs.
            objet_player = player.Player(last_name,
                                         first_name,
                                         date_of_birth,
                                         sexe)
            # Ajout de l'objet de type de class Player a ma liste "players"
            players.append(objet_player)

        # Si le programme n'applique pas la condition, alors je retourne une valeur "None" afin de ne pas faire crasher le programme
        objet_tournoi = None

        if dict_tournoi != {}:
            # Ici je recupere les valeurs du dictionnaire peut importe l'ordre d'ecriture
            name_tournoi = dict_tournoi['name']
            place = dict_tournoi['place']
            start_date = dict_tournoi['date_debut']
            end_date = dict_tournoi['date_fin']
            director_remark = dict_tournoi['director_remark']
            n_rounds = 4
            rounds = []

            # un dictionnaire qui comprends des keys de joueurs et des values qui sont les joueurs avec qui le joueur a deja joueurs
            last_visited_players = {}
            # boucle for pour construire
            for player in players:
                last_visited_players[player] = []
            random.shuffle(players)
            # Boucle for des attribiuts de la class Round avec la method range() parametrer des nbs de tours
            for k in range(n_rounds):
                name = "Round " + str(k+1)
                date_debut, heure_debut = get_timestamp()
                # print(f'Date de debut : {date_debut}')
                # print(f"Heure de debut : {heure_debut}")
                matchs = []

                print(f'Nom du Round : {name}')
                # Boucle sur la longueur de ma liste de joueur en y ajoutant -1 afin de stopper l'iteration a 7 car le nombre 8 est "Exclut"
                for i in range(len(players)-1):
                    player1 = players[i]
                    for j in range(i+1, len(players)):
                        player2 = players[j]
                        if player2 not in last_visited_players[player1]:
                            # Je donne une valeur a mon score
                            print('Resultats du match', i+1)
                            # J'appel les valeurs retourner de ma methode de la view en n'oubliant pas d'indiquer ses params.
                            score1, score2 = self.view.create_score(
                                player1, player2)
                            # score1 = int(input(f'score du joueur {player1.first_name}:' ))
                            # score2 = int(input(f'score du joueur {player2.first_name}:'))

                            # La var match1 est un tuple de deux liste contenant 2 valeurs, un joueur et un score
                            match_ = ([player1, score1], [player2, score2])
                            # Creation de l'objet_match en instanciant ma class Match qui est parametrer de mon tuple des deux listes
                            objet_match = match.Match(match_)
                            objet_match.add_points()

                            # J'ajoute a ma liste de matchs[] mon objet_match et donc ses valeurs
                            matchs.append(objet_match)
                            last_visited_players[player1].append(player2)
                            last_visited_players[player2].append(player1)
                            print('------------------------------')
                            break

                classement_players = []
                points_list = []
                # Boucle de mes joueurs qui classifie la list des points avec la method sorted()
                for player in players:
                    nb_points = player.points
                    points_list.append(nb_points)
                # print(points_list)

                points_list = sorted(points_list, reverse=True)

                # print(points_list)

                list_players = players
                # Boucle qui classifie la list des joueurs selon leurs nb de points
                for i in range(len(points_list)):
                    for player in list_players:
                        # condition sur le points si le nb de points du joueurs est egal aux nbs de points extraits de la liste de points classer
                        if player.points == points_list[i]:
                            classement_players.append(player)
                            player.classement = i+1
                            list_players.remove(player)
                            break
                # Boucle  pour afficher le classement
                # for player in classement_players:
                #     print(player)

                players = classement_players

                date_fin, heure_fin = get_timestamp()
                # print(f"Date de fin : {date_fin}")
                # print(f"Heure de fin : {heure_fin}")
                # Creation de l'objet "tour"
                tour = round.Round(name, matchs, date_debut,
                                   heure_debut, date_fin, heure_fin)
                tour.display_result()
                # Ajout a ma liste rounds[] des valeurs de mon objet creer
                rounds.append(tour)

            # Instanciation de la class Tournoi, en respectant l'ordre des attributs cette fois-ci
            objet_tournoi = tournoi.Tournoi(name_tournoi,
                                            place,
                                            start_date,
                                            end_date,
                                            players,
                                            rounds,
                                            n_rounds,
                                            director_remark)

        # Retourne les valeurs de mon objet
        return objet_tournoi

    def create_tournement(self):
        display_menu = self.view.get_display_menu()

        if display_menu == "1":
            data_tournement = self.view.get_data_tournoi()
            dict_players = self.view.get_player_data()
            data_tournement['players'] = dict_players
            with open('data.json', 'w') as f:
                json.dump(data_tournement, f)

        elif display_menu == "2":
            print("Pas de tournoi enregister pour le moment")
            pass

        elif display_menu == "3":
            print("Pas de tournoi enregister pour le moment")
            pass

        elif display_menu == "4":
            print("Exit")
            pass

        else:
            print("Veuillez taper un chiffre entre 1 et 4, merci.")

    def play_tournement(self):
        dict_tournoi = json.load('data.json')
        players_dict = dict_tournoi['players']
        players = []

        # Boucle qui instancie chaque player avec un objet
        for dict_player in players_dict.values():
            last_name = dict_player['last_name']
            first_name = dict_player['first_name']
            date_of_birth = dict_player['date_of_birth']
            sexe = dict_player['sexe']

            # J'instancie maintenant l'objet de class Player avec ses attributs.
            objet_player = player.Player(last_name,
                                         first_name,
                                         date_of_birth,
                                         sexe)
            # Ajout de l'objet de type de class Player a ma liste "players"
            players.append(objet_player)

        # Si le programme n'applique pas la condition, alors je retourne une valeur "None" afin de ne pas faire crasher le programme
        objet_tournoi = None

        if dict_tournoi != {}:
            # Ici je recupere les valeurs du dictionnaire peut importe l'ordre d'ecriture
            name_tournoi = dict_tournoi['name']
            place = dict_tournoi['place']
            start_date = dict_tournoi['date_debut']
            end_date = dict_tournoi['date_fin']
            director_remark = dict_tournoi['director_remark']
            n_rounds = 4
            rounds = []

            # un dictionnaire qui comprends des keys de joueurs et des values qui sont les joueurs avec qui le joueur a deja joueurs
            last_visited_players = {}
            # boucle for pour construire
            for player in players:
                last_visited_players[player] = []
            random.shuffle(players)
            # Boucle for des attribiuts de la class Round avec la method range() parametrer des nbs de tours
            for k in range(n_rounds):
                name = "Round " + str(k+1)
                date_debut, heure_debut = get_timestamp()
                # print(f'Date de debut : {date_debut}')
                # print(f"Heure de debut : {heure_debut}")
                matchs = []

                print(f'Nom du Round : {name}')
                # Boucle sur la longueur de ma liste de joueur en y ajoutant -1 afin de stopper l'iteration a 7 car le nombre 8 est "Exclut"
                for i in range(len(players)-1):
                    player1 = players[i]
                    for j in range(i+1, len(players)):
                        player2 = players[j]
                        if player2 not in last_visited_players[player1]:
                            # Je donne une valeur a mon score
                            print('Resultats du match', i+1)
                            # J'appel les valeurs retourner de ma methode de la view en n'oubliant pas d'indiquer ses params.
                            score1, score2 = self.view.create_score(
                                player1, player2)
                            # score1 = int(input(f'score du joueur {player1.first_name}:' ))
                            # score2 = int(input(f'score du joueur {player2.first_name}:'))

                            # La var match1 est un tuple de deux liste contenant 2 valeurs, un joueur et un score
                            match_ = ([player1, score1], [player2, score2])
                            # Creation de l'objet_match en instanciant ma class Match qui est parametrer de mon tuple des deux listes
                            objet_match = match.Match(match_)
                            objet_match.add_points()

                            # J'ajoute a ma liste de matchs[] mon objet_match et donc ses valeurs
                            matchs.append(objet_match)
                            last_visited_players[player1].append(player2)
                            last_visited_players[player2].append(player1)
                            print('------------------------------')
                            break

                classement_players = []
                points_list = []
                # Boucle de mes joueurs qui classifie la list des points avec la method sorted()
                for player in players:
                    nb_points = player.points
                    points_list.append(nb_points)
                # print(points_list)

                points_list = sorted(points_list, reverse=True)

                # print(points_list)

                list_players = players
                # Boucle qui classifie la list des joueurs selon leurs nb de points
                for i in range(len(points_list)):
                    for player in list_players:
                        # condition sur le points si le nb de points du joueurs est egal aux nbs de points extraits de la liste de points classer
                        if player.points == points_list[i]:
                            classement_players.append(player)
                            player.classement = i+1
                            list_players.remove(player)
                            break
                # Boucle  pour afficher le classement
                # for player in classement_players:
                #     print(player)

                players = classement_players

                date_fin, heure_fin = get_timestamp()
                # print(f"Date de fin : {date_fin}")
                # print(f"Heure de fin : {heure_fin}")
                # Creation de l'objet "tour"
                tour = round.Round(name, matchs, date_debut,
                                   heure_debut, date_fin, heure_fin)
                tour.display_result()
                # Ajout a ma liste rounds[] des valeurs de mon objet creer
                rounds.append(tour)

            # Instanciation de la class Tournoi, en respectant l'ordre des attributs cette fois-ci
            objet_tournoi = tournoi.Tournoi(name_tournoi,
                                            place,
                                            start_date,
                                            end_date,
                                            players,
                                            rounds,
                                            n_rounds,
                                            director_remark)

        # Retourne les valeurs de mon objet
        return objet_tournoi
