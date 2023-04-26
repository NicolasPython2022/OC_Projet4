from models import player
from models import tournoi
from models import round
from views import main_view


class Controller:

    def __init__(self):
        self.view_player = main_view.ViewPlayer()
        self.view_tournoi = main_view.ViewTournoi()
        self.players = []

    # Tjrs mettre un verbe explicite pr les methods
    def get_player(self):
        players_list = self.view_player.get_player_data()
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
        
        #self.players = players

        return players
    

    def get_tournoi(self):

            # Ce qui est retourner par la view est stocker dans un dictionnaire "dict_tournoi"
            dict_tournoi = self.view_tournoi.get_data_tournoi()

            players = self.players

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
                # Boucle for des attribiuts de la class Round avec la method range() parametrer des nbs de tours
                for i in range(n_rounds):
                     name = "Round " + str(i+1)
                     matchs = []
                     date_debut = "23/04/23"
                     heure_debut = "14h00"
                     date_fin = "30/04/23"
                     heure_fin = "17h00"
                     # Creation de l'objet "tour"
                     tour = round.Round(name,matchs,date_debut,heure_debut,date_fin,heure_fin)
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