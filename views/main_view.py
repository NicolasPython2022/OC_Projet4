from rich.console import Console
from rich.table import Table



class View:

    def get_menu(self):
        print("--------------------------------------")
        print('''
        Que souhaitez vous faire ?\n 
        1 - Creation d'un tournoi \n
        2 - Afficher les infos d'un tournoi \n
        3 - Commencer un tournoi \n
        4 - Reprendre un tournoi en cours \n
        5 - Quitter \n
        ''')

        display_menu = str(input("Entrer votre choix : "))
        return display_menu
    
    def stop_and_start(self):
        choise_user = input("Voulez-vous continuer ou arreter le tournoi en cours ?\n 'O' pour continuer et 'N' pour arreter")
        return choise_user
    
    def play_tournement(self, tournement_register):
        print("--------------------------------------")
        print("Quel tournoi souhaitez-vous commencer ? ")
        for key in tournement_register.keys():
            print(f"{key} - {tournement_register[key]}['name']")
        
        choise_tournement = input("Choisir un tournoi : ")
        return choise_tournement
    
    def resume_game(self,data_tournement):
        print("--------------------------------------")
        data = True
        print("Quel tournoi souhaitez-vous reprendre ? ")
        for key in data_tournement.keys():
            n_rounds = data_tournement[key]["numbers_rounds"]
            if data_tournement[key]["last_played_round"] < n_rounds -1:
                print(f"{key} - {data_tournement[key]['name']}")
                data = False

        if data:
            print("Il n'y a pas de tournoi a reprendre pour le moment.")
            choise_tournement = None
        else:
            choise_tournement =str(input("Choisir un tournoi a reprendre : "))
            return choise_tournement
        print("--------------------------------------")


    def get_player_data(self):
        nb_players = 4
        players_dict = {}

        for player in range(nb_players):
            print(f'---------------Creation du joueur {player+1}-----------------------')
            last_name = str(input("Nom : "))
            first_name = str(input("Prenom : "))
            date_of_birth = str(input("Date de naissance : "))
            sexe = str(input("Homme ou Femme ? "))

            dict_player = {'last_name' : last_name,
                           'first_name' : first_name,
                           'date_of_birth' : date_of_birth,
                           'sexe' : sexe,
                           'points' : 0,
                           'classement' : player+1,
                           'last_players_meet' : []
                           }     
            '''
            player_dict est le dictionnaire general qui comprend un dictionnaire representant chaque joueur.
            '''
            #players_dict.append(dict_player)
            players_dict[str(player+1)] = dict_player

        return players_dict


    def get_data_tournoi():
        '''Mehode de creation d'un tournoi.'''
        dict_tournoi = {}

        print("---------------Creation du Tournoi-----------------------")
        name = str(input('Nom du tournoi : '))
        place = str(input('Lieu du tournoi : '))
        start_date = str(input('Date de debut :'))
        end_date = str(input('Date de fin : '))
        director_remark = str(input('Remarques du Directeur : '))

        dict_tournoi = {'name' : name,
                        'place': place,
                        'start_date' : start_date,
                        'end_date' : end_date,
                        'directeur': director_remark
                        }
        
        return dict_tournoi


    def assign_score(self, player1, player2):
        score1 = int(input(f"Entree score du joueur {player1.last_name} {player1.first_name} : "))
        score2 = int(input(f"Entree score du joueur {player2.last_name} {player2.first_name} : "))
        return score1,score2


































        if display_menu == "1":
            

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
