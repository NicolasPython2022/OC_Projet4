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

            # Ce qui est retourner par la view est stocke dans un dictionnaire "dict_tournoi"
            dict_tournoi = self.view_tournoi.get_data_tournoi()

            players = self.players

            objet_tournoi = None

            if dict_tournoi != {}:
                # Ici je recuperes les valeurs du dictionnaire peut importe l'ordre d'ecriture
                name_tournoi = dict_tournoi['name']
                place = dict_tournoi['place']
                date = dict_tournoi['date']
                director_remark = dict_tournoi['director_remark']
                nombres_tours = 4
                rounds = []
                for i in range(nombres_tours):
                     name = "Round " + str(i+1)
                     matchs = []
                     date_debut = "23/04/23"
                     heure_debut = "14h00"
                     date_fin = "30/04/23"
                     heure_fin = "17h00"

                     tour = round.Round(name,matchs,date_debut,heure_debut,date_fin,heure_fin)
                     rounds.append(tour)
                


                # Instanciation de la class Tournoi, en respectant l'ordre des attributs cette fois-ci
                objet_tournoi = tournoi.Tournoi(name_tournoi,
                                                place, 
                                                date,
                                                players,
                                                rounds,
                                                nombres_tours,
                                                director_remark)
                
                
            return objet_tournoi