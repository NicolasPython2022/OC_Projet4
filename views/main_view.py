from rich.console import Console
from rich.table import Table


class View:

    def display_menu(self):
        print("----------------------------------------------------\n")
        print('''Que souhaitez vous faire ?\n\t
        1 - Creation d'un tournoi \n\t
        2 - Afficher les infos d'un tournoi \n\t
        3 - Commencer un tournoi \n\t
        4 - Reprendre un tournoi en cours \n\t
        5 - Quitter \n''')

        display_menu = str(input("Entrer votre choix : "))
        print('')
        return display_menu

    def stop_and_start_tournement(self):
        input_user = input("Voulez vous continuer le tournoi ? (O/N)")
        return input_user

    def get_tournement_to_play(self, data_tournement):
        print("----------------------------------------------------")
        print("Quel tournoi voulez-vous commencer ?")
        for key in data_tournement.keys():
            print(f"\t{key}- {data_tournement[key]['name']}")
        choise_tournement = str(input("Choisir un tournoi : "))
        print("----------------------------------------------------")
        return choise_tournement

    def get_tournement_to_replay(self, data_tournement):

        print("----------------------------------------------------")
        k = True
        print("Quel tournoi voulez-vous reprendre ?")
        for key in data_tournement.keys():
            n_rounds = data_tournement[key]["nombre_rounds"]
            if data_tournement[key]["last_played_round"] < n_rounds-1:
                print(f"\t{key}- {data_tournement[key]['name']}")
                k = False
        if k:
            print("Il n' ya pas un tournoi à reprendre!!")
            choised_tournement = None
        else:
            choised_tournement = str(input("Choisir un tournoi : "))
        return choised_tournement
        print("----------------------------------------------------")

    def get_player_data(self, nb_players):

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
                           "last_visited_players": [],
                           "points": 0}
            # players_dict est le dictionnaire general qui comprend un dictionnaire representant chaque joueur.
            players_dict[str(i+1)] = dict_player

        return players_dict

    def get_data_tournoi(self):
        # Creation du tournoi
        dict_tournoi = {}
        print("----------------------Creation du Tournoi----------------------\n")
        name = str(input("Entrer un nom de Tournoi : "))
        place = str(input("Entrer le lieu du Tournoi : "))
        date_debut = str(input("Entrer la date de debut du Tournoi : "))
        date_fin = str(input("Entrer la date de fin du tournoi : "))
        director_remark = str(input("Remarques du directeur du Tournoi : "))

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
        score1 = int(input(f'score du joueur {player1.first_name}:'))
        score2 = int(input(f'score du joueur {player2.first_name}:'))

        return score1, score2

    def display_tournement_infos(self, data_tournement):
        print("----------------------------------------------------")
        print("Quel tournoi voulez vous afficher ?\n")
        for key in data_tournement.keys():
            print(f"\t{key}- {data_tournement[key]['name']}\n")
        choised_tournement = str(input("Choisir un tournoi: "))
        print("----------------------------------------------------")
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
