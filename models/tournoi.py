"""Tournoi d'echec."""

class Tournoi:
    """Creation d'une class de Tournoi d'echec."""

    """Initialisation du constructor."""
    def __init__(self,
                 name,
                 place, 
                 date,
                 players,
                 rounds,
                 nombres_tours,
                 director_remark):
        
        """Initialisation des attributs d'instance."""
        self.name = name
        self.place = place
        self.date = date
        self.joueurs = players
        self.rounds = rounds
        self.nombres_tours = nombres_tours
        self.director_remark = director_remark

    """Method qui permet de returner les valeurs d'infos souhaitees."""
    def __str__(self):
        return f"""Infos Tournoi : \n\t
                        Name:                  {self.name} \n\t
                        Place:                 {self.place}\n\t
                        Date:                  {self.date}\n\t
                        Joueurs:               {self.joueurs}\n\t
                        Rounds:                {self.rounds}\n\t
                        Nombre de tours:       {self.nombres_tours}
                        Director remark:       {self.director_remark}"""
