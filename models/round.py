
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