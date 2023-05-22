"""Tournoi d'echec."""


class Tournoi:
    """Creation d'une class de Tournoi d'echec."""

    """Initialisation du constructor."""

    def __init__(self,
                 name,
                 place,
                 start_date,
                 end_date,
                 players,
                 rounds,
                 n_rounds,
                 director_remark):
        """Initialisation des attributs d'instance."""
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.players = players
        self.rounds = rounds
        self.n_rounds = n_rounds
        self.director_remark = director_remark

    """Method qui permet de returner les valeurs d'infos souhaitees."""

    def __str__(self):
        return f"""Infos Tournoi : \n\t
                        Name:                  {self.name} \n\t
                        Place:                 {self.place}\n\t
                        Date de debut:         {self.start_date}\n\t
                        Date de fin:           {self.end_date}\n\t
                        Joueurs:               {self.players}\n\t
                        Tours:                 {self.rounds}\n\t
                        Nombre de tours:       {self.n_rounds}\n\t
                        Director remark:       {self.director_remark}"""
