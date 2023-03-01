from models.tournoi import Tournoi

"""Function qui permet de cree un nouveau tournoi, en appellant la class Tournoi et ses attributs en parametres."""

def create_tournoi(name, place, date, players, rounds, nombres_tours, director_remark):
    new_tournoi = Tournoi(name, place, date, players, rounds, nombres_tours, director_remark)
    
    return new_tournoi