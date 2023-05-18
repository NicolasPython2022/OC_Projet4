"""Joueurs du tournoi."""

class Player:
    """"Joueur."""

    def __init__(self, last_name, first_name, date_of_birth, sexe, points=0, classement=None):
        """Initialise le constructeur et les attributs de la class."""

        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.sexe = sexe
        self.points = points
        self.classement = classement

    
    def update_classement(self,classement):
        self.classement = classement
    
    
    def __str__(self):
        return f"""Infos du joueur : \n\t
            Name:{self.last_name} 
            First Name: {self.first_name}\n\t
            Total points: {self.points} \n\t
            Classement: {self.classement}"""
