'''
Le fichier main.py comporte la logique de mon programme, appel des methods de mes functions.
'''

from controllers import main_controller
from models import match
from models import round
from views import main_view
'''
1 - Instanciation du controllers.
2 - Appel de la method qui recupere les infos d'un joueur : controller.view.get_player_data()
'''
# Definition de l'objet view par l'instance de la class
view = main_view.View()
view.get_menu()


# Instance de controller avec appel de class du fichier
# controller = main_controller.Controller()


# # Method d'affichage avec rich
# # Appel de la method de class 
# controller.get_player()

# tournement = controller.get_tournoi()

# # Appel de l'attribut view du constructeur de la class Controller() avec la methode d'affichage de la class View()
# # Je lui passe en param l'objet tournement de la class Tournoi()
# controller.view.display_result(tournement)