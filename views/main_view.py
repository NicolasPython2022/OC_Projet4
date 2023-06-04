from rich.console import Console
from rich.table import Table
from datetime import datetime


class View:
    def display_menu(self):
        print("-----------------------------------")
        print('''Que souhaitez vous faire ?\n\t
        1 - Creation d'un tournoi \n\t
        2 - Afficher les infos d'un tournoi \n\t
        3 - Commencer un tournoi \n\t
        4 - Reprendre un tournoi en cours \n\t
        5 - Quitter \n''')
        display_menu = str(input("Entrer votre choix : "))
        print("-----------------------------------------")
        return display_menu

    def stop_and_start_tournement(self):
        input_user = input("Voulez vous continuer le tournoi ? (O/N)")
        return input_user

    def get_tournement_to_play(self, data_tournement):
        print("-------------------------------------")
        k = True
        print("Quel tournoi voulez-vous commencer ?")
        for key in data_tournement.keys():
            if data_tournement[key]["last_played_round"] == -1:
                print(f"\t{key}- {data_tournement[key]['name']}")
                k = False
        if k:
            print("Il n' ya pas un tournoi à commencer!!")
            choised_tournement = None
        else:
            choised_tournement = str(input("Choisir un tournoi : "))
        print("-------------------------------------")
        return choised_tournement

    def get_tournement_to_replay(self, data_tournement):
        print("-----------------------------------------")
        k = True
        print("Quel tournoi voulez-vous reprendre ?")
        for key in data_tournement.keys():
            n_rounds = data_tournement[key]["nombre_rounds"]
            if data_tournement[key]["last_played_round"] < n_rounds-1\
                    and data_tournement[key]["last_played_round"] >= 0:
                print(f"\t{key}- {data_tournement[key]['name']}")
                k = False
        if k:
            print("Il n' ya pas un tournoi à reprendre!!")
            choised_tournement = None
        else:
            choised_tournement = str(input("Choisir un tournoi : "))
        print("-----------------------------------------")
        return choised_tournement

    def get_player_data(self, nb_players):
        players_dict = {}
        for i in range(nb_players):
            print('----------------------------------------------------')
            print(f'Creation du joueur {i+1}')
            last_name = input('Entrer votre nom : ')
            first_name = input('Entrer maintenant votre prenom : ')
            date_of_birth = input(
                'Entrer votre date de naissance (dd-mm-yyyy) :')
            k = False
            try:
                date_of_birth = datetime.strptime(date_of_birth, "%d-%m-%Y")
            except:
                k = True
            while k:
                print(
                    '''Veuillez rentrer la date dans le bon format suivant :
                       dd-mm-yyyy .
                    ''')
                date_of_birth = input(
                    'Entrer votre date de naissance (dd-mm-yyyy) :')
                try:
                    date_of_birth = datetime.strptime(
                        date_of_birth, "%d-%m-%Y")
                    k = False
                except:
                    k = True
            date_of_birth = date_of_birth.strftime("%d-%m-%Y")
            sexe = input(
                'Vous etes un Homme ou une Femme (H/F) ? ').capitalize()
            while sexe != "H" and sexe != "F":
                print("Veuillez rentrer soit F pour femme ou H pour Homme")
                sexe = input(
                    'Vous etes un Homme ou une Femme (H/F) ? ').capitalize()

            dict_player = {"last_name": last_name,
                           "first_name": first_name,
                           "date_of_birth": date_of_birth,
                           "sexe": sexe,
                           "classement": i+1,
                           "last_visited_players": [],
                           "points": 0}

            '''players_dict est le dictionnaire general,
            qui comprend un dictionnaire representant chaque joueur.'''
            players_dict[str(i+1)] = dict_player

        return players_dict

    def get_data_tournoi(self):
        # Creation du tournoi
        dict_tournoi = {}
        print("---------------------------------------------------------")
        print("Creation du Tournoi")
        name = input("Entrer un nom de Tournoi : ")
        place = input("Entrer le lieu du Tournoi : ")
        date_debut = input(
            "Entrer la date de debut du Tournoi (dd-mm-yyyy) : ")
        k = False
        try:
            date_debut = datetime.strptime(date_debut, "%d-%m-%Y")
        except:
            k = True
        while k:
            print('''Veuillez rentrer la date dans le bon format suivant :
            dd-mm-yyyy .
            ''')
            date_debut = input(
                "Entrer la date de debut du Tournoi (dd-mm-yyyy) : ")
            try:
                date_debut = datetime.strptime(date_debut, "%d-%m-%Y")
                k = False
            except:
                k = True
        date_debut = date_debut.strftime("%d-%m-%Y")

        date_fin = input("Entrer la date de fin du tournoi (dd-mm-yyyy) : ")
        k = False
        try:
            date_fin = datetime.strptime(date_fin, "%d-%m-%Y")
        except:
            k = True
        while k:
            print('''Veuillez rentrer la date dans le bon format suivant :
            dd-mm-yyyy .
            ''')
            date_fin = input(
                "Entrer la date de fin du Tournoi (dd-mm-yyyy) : ")
            try:
                date_fin = datetime.strptime(date_fin, "%d-%m-%Y")
                k = False
            except:
                k = True
        date_fin = date_fin.strftime("%d-%m-%Y")

        director_remark = input("Remarques du directeur du Tournoi : ")

        dict_tournoi = {"name": name,
                        "place": place,
                        "date_debut": date_debut,
                        "date_fin": date_fin,
                        "nombre_rounds": 4,
                        "nombre_players": 8,
                        "last_played_round": -1,
                        "director_remark": director_remark
                        }

        return dict_tournoi

    def create_score(self, player1, player2):
        score1 = input(f'score du joueur {player1.first_name}:')
        score2 = input(f'score du joueur {player2.first_name}:')
        is_error = False
        try:
            score1, score2 = int(score1), int(score2)
        except:
            is_error = True
        while is_error:
            print(
                '''les scores ne sont pas bons,
                veuillez rentrer des nombres entiers positifs.
                ''')
            score1 = input(f'score du joueur {player1.first_name}:')
            score2 = input(f'score du joueur {player2.first_name}:')
            try:
                score1, score2 = int(score1), int(score2)
                is_error = False
            except:
                is_error = True

        return score1, score2

    def display_tournement_infos(self, data_tournement):
        print("--------------------------------")
        print("Quel tournoi voulez vous afficher ?\n")
        for key in data_tournement.keys():
            print(f"\t{key}- {data_tournement[key]['name']}")
        choised_tournement = str(input("Choisir un tournoi: "))
        while choised_tournement not in data_tournement.keys():
            print(
                '''La valeur entrée n'est pas valide,
                veuillez choisir un nombre parmi les nombres proposés.
                ''')
            choised_tournement = str(input("Choisir un tournoi: "))
        print("-------------------------------")
        data_tournement = data_tournement[choised_tournement]

        table_tournement = Table(title="Infos du tournoi")
        table_tournement.add_column('Nom')
        table_tournement.add_column('Lieux')
        table_tournement.add_column('Date de debut')
        table_tournement.add_column('Date de fin')
        table_tournement.add_column('Remarque du directeur')

        table_tournement.add_row(data_tournement['name'],
                                 data_tournement['place'],
                                 data_tournement['date_debut'],
                                 data_tournement['date_fin'],
                                 data_tournement['director_remark'])

        console = Console()
        console.print(table_tournement)

        table_player = Table(title="Infos des Joueurs")
        table_player.add_column("Classement")
        table_player.add_column("Nom de famille")
        table_player.add_column("Prenom")
        table_player.add_column("Date de naissance")
        table_player.add_column("Sexe")
        table_player.add_column("Points")

        players = data_tournement['players']

        for key in players.keys():
            # var player qui contient les infos du numero d'un joueur
            player = players[key]
            table_player.add_row(str(player['classement']),
                                 player['last_name'],
                                 player['first_name'],
                                 player['date_of_birth'],
                                 player['sexe'],
                                 str(player['points']))

        console = Console()
        console.print(table_player)
