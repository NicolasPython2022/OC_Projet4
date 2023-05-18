from controllers.timestamp import get_timestamp
from models.match import Match


class Round:
    """Tour.
    Chaque tour est une liste de match.
    Chaque match consiste en une paire de joueurs avec un champ de resultats pr chaque joueurs."""

    def __init__(self, name, matchs, date_debut, heure_debut, date_fin, heure_fin):
        """Initialise le constructeur."""

        self.name = name
        self.matchs = matchs
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.heure_debut = heure_debut
        self.heure_fin = heure_fin
    
    def display_result(self):
        for match in self.matchs:
            print(match)


    # Method qui affiche la fin des matchs et qui demande le resultat de chaque match joue
    def close_match(self):
        self.end_date = get_timestamp()
        print(f"Le round {self.name} c'est termine a : {self.end_date}")
        print("Veuillez rentrer les resultats des matchs effectues.")
        for match in self.matchs:
            match.start_match()



            