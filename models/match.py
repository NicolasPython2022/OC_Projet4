"""Class des matchs"""


class Match:

    def __init__(self, match):
        # Initialise le constructeur et les attributs de la class.
        """
        Un match unique doit être stocké sous la forme d'un tuple
           contenant deux listes, chacune contenant deux éléments :
           une référence à une instance de joueur et un score.
           Les matchs multiples doivent être stockés sous forme de liste
           sur l'instance du tour.
        """
        self.match = match

    def __str__(self):
        player1 = self.match[0][0]
        score1 = self.match[0][1]
        player2 = self.match[1][0]
        score2 = self.match[1][1]

        return f"{player1.first_name} {score1}:{score2} {player2.first_name}"
