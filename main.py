'''
Le fichier main.py comporte la logique de mon programme, appel des methods de mes functions.
'''
from controllers import main_controller
'''
1 - Instanciation de l'objet controller.
2 - Appel de la method qui permet de jouer aux tournois
'''
controller = main_controller.Controller()
# Jouer le tournoi
controller.play_tournement()
