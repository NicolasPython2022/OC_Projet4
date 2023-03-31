from views import view_tournoi
from models import tournoi


class ControlTournoi:
        
        def __init__(self,players):
              self.players = players
              #self.views = view_tournoi.ViewTournoi()


        def control_data_tournoi(self):

            dict_tournoi = view_tournoi.ViewTournoi().get_data_tournoi()

            players = self.players
    
            # Ici je recuperes les valeurs du dictionnaire peut importe l'ordre d'ecriture
            name = dict_tournoi['name']
            place = dict_tournoi['place']
            date = dict_tournoi['date']
            director_remark = dict_tournoi['director_remark']
            rounds = []
            nombres_tours = 4

            # Instanciation de la class Tournoi, en respectant l'ordre des attributs cette fois-ci
            objet_tournoi = tournoi.Tournoi(name,
                                            place, 
                                            date,
                                            players,
                                            rounds,
                                            nombres_tours,
                                            director_remark)
            
            return objet_tournoi