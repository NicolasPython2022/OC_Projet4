from rich.console import Console
from rich.table import Table
import os
import json


class View:

    def get_menu(self):
        print('''
        Que souhaitez vous faire ?\n 
        1 - Creation d'un tournoi \n
        2 - Afficher les infos d'un tournoi \n
        3 - Commencer un tournoi \n
        4 - Reprendre un tournoi en cours \n
        5 - Quitter \n
        ''')

        display_menu = str(input("Entrer votre choix : "))
        if display_menu == "1":
            new_data_tournement = {}
            data_tournement = self.get_data_tournoi()
            dict_players = self.get_player_data()
            data_tournement['players'] = dict_players
            new_data_tournement['1'] = data_tournement
            if os.path.exists('data.json'):
                with open('data.json', 'r') as f:
                    history_tournement = json.load(f)
                last_tournement_key = int(list(history_tournement.keys())[-1])
                history_tournement[str(
                    last_tournement_key+1)] = data_tournement
                new_data_tournement = history_tournement

            with open('data.json', 'w') as f:
                json.dump(new_data_tournement, f)

        elif display_menu == "2":
            with open('data.json', 'r') as f:
                data_tournement = json.load(f)

            print("Quel tournoi voulez vous afficher ?\n")
            for key in data_tournement.keys():
                print(f"{key}- {data_tournement[key]['name']}")
            choised_tournement = str(input("Choisir un tiournoi: "))
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

        elif display_menu == "3":
            if os.path.exists('data.json'):
                with open('data.json') as f:
                    history_tournement = json.load(f)
                print("Quel tournoi voulez-vous commencer ? ")
                for key in history_tournement.keys():
                    print(f"{key}- {history_tournement[key]['name']}")
                choise_tournement = str(input("Choisir un tournoi : "))
                history_tournement = history_tournement[choise_tournement]

        elif display_menu == "4":
            print("Exit")
            pass

        else:
            print("Veuillez taper un chiffre entre 1 et 4, merci.")

    def get_player_data(self):

        nb_players = 4
        players_dict = {}

        for i in range(nb_players):
            print('----------------------------------------------------')
            print(f'Creation du joueur {i+1}')
            last_name = str(input('Entrer votre nom : '))
            first_name = str(input('Entrer maintenant votre prenom : '))
            date_of_birth = str(input('Entrer votre date de naissance :'))
            sexe = str(input('Vous etes un Homme ou une Femme ? '))

            dict_player = {"last_name": last_name,
                           "first_name": first_name,
                           "date_of_birth": date_of_birth,
                           "sexe": sexe,
                           "classement": i+1,
                           "points": 0}
            # players_dict est le dictionnaire general qui comprend un dictionnaire representant chaque joueur.
            players_dict[str(i+1)] = dict_player

        return players_dict

    def get_data_tournoi(self):
        # Creation du tournoi
        dict_tournoi = {}
        print("---------------------------------------------------------")
        print("Creation du Tournoi")
        name = str(input("Entrer un nom de Tournoi : "))
        place = str(input("Entrer le lieu du Tournoi : "))
        date_debut = str(input("Entrer la date de debut du Tournoi : "))
        date_fin = str(input("Entrer la date de fin du tournoi : "))
        director_remark = str(input("Remarques du directeur du Tournoi : "))

        dict_tournoi = {"name": name,
                        "place": place,
                        "date_debut": date_debut,
                        "date_fin": date_fin,
                        "director_remark": director_remark
                        }

        return dict_tournoi

    def create_score(self, player1, player2):
        score1 = int(input(f'score du joueur {player1.first_name}:'))
        score2 = int(input(f'score du joueur {player2.first_name}:'))

        return score1, score2

    def display_result(self, tournement):
        table_tournement = Table(title="Infos du tournoi")
        table_tournement.add_column('Nom')
        table_tournement.add_column('Lieux')
        table_tournement.add_column('Date de debut')
        table_tournement.add_column('Date de fin')
        table_tournement.add_column('Remarque du directeur')
        if tournement != None:
            table_tournement.add_row(tournement.name, tournement.place,
                                     tournement.start_date, tournement.end_date, tournement.director_remark)

        console = Console()
        console.print(table_tournement)

        # Appel de l'attribut de l'objet de la class Controller
        players = tournement.players

        # Method d'affichache avec rich
        table_player = Table(title="Infos des Joueurs")
        table_player.add_column("Classement", justify="right", style="green")
        table_player.add_column(
            "Nom de famille", justify="center", style="cyan", no_wrap=True)
        table_player.add_column("Prenom", style="magenta")
        table_player.add_column("Date de naissance",
                                justify="right", style="green")
        table_player.add_column("Sexe", justify="right", style="green")
        table_player.add_column("Points", justify="right", style="green")

        for player in players:
            table_player.add_row(str(player.classement), player.last_name,
                                 player.first_name, player.date_of_birth, player.sexe, str(player.points))

        # J'instancie la class Console() quin sera afficher ds le terminal

        console.print(table_player)

    # while True:
    #         value = input(msg_display)
    #                 return int(value) if value.isnumeric()
