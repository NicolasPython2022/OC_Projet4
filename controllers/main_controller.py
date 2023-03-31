from models import player
from views import main_view

class ControlPlayer:

    def __init__(self):
        self.view_player = main_view.ViewPlayer()
        #self.view = main_view.View()
        #self.players = []
    # Mettre un verbe pour la method qui soit explicite
    def control_player_data(self, players_list):
        '''
        Ma var players_list se voit assigner le fichier suivi de ma classViewPlayer,
        qui fait appel a la method de cette class .get_player_data()
        '''
        
        
        # Instanciation des objets de la class Player, chaque player est representer par un dictionnaire.
        players = []

        # Boucle qui instancie chaque player avec un objet
        for dict_player in players_list:
            last_name = dict_player['last_name']
            first_name = dict_player['first_name']
            date_of_birth = dict_player['date_of_birth']
            sexe = dict_player['sexe']

            # J'instancie maintenant l'objet de la class Player avec ses attributs.
            objet_player = player.Player(last_name,
                                        first_name, 
                                        date_of_birth,
                                        sexe)
            # Ici j'ajoute a ma liste l'objet de type de la class Player
            players.append(objet_player)
        
        #self.players = players

        return players