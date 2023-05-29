'''
Le fichier main.py comporte la logique de mon programme, appel des methods de mes functions.
'''

from controllers import main_controller
import json
import os

'''
1 - Instanciation du controllers.
2 - Appel de la method qui recupere les infos d'un joueur : controller.view.get_player_data()
'''


def play_tourenement():
    # Instance de controller avec appel de class du fichier
    controller = main_controller.Controller()
    # jouer le tournoi
    while True:
        display_menu = controller.view.display_menu()
        if display_menu == '1':
            controller.create_tournement()
        elif display_menu == '2':
            if os.path.exists(controller.data_path):
                controller.display_tournement_infos()
            else:
                print(
                    "Pas de fichier de tournoi enregistré, veuillez créer d'abord un tournoi.")
        elif display_menu == '3':
            if os.path.exists(controller.data_path):
                with open(controller.data_path, 'r') as f:
                    data_tournement = json.load(f)
                choised_tournement = controller.view.get_tournement_to_play(
                    data_tournement)
                while choised_tournement not in data_tournement.keys() and choised_tournement != None:
                    print("La valeur entrée n'est pas valide")
                    choised_tournement = controller.view.get_tournement_to_play(
                        data_tournement)
                if choised_tournement != None:
                    dict_tournement = data_tournement[choised_tournement]
                    dict_tournement = controller.start_tournement(
                        dict_tournement)
                    data_tournement[choised_tournement] = dict_tournement
                    with open(controller.data_path, 'w') as f:
                        json.dump(data_tournement, f)
            else:
                print(
                    "Pas de fichier de tournoi enregistré, veuillez créer d'abord un tournoi.")
        elif display_menu == '4':
            if os.path.exists(controller.data_path):
                with open(controller.data_path, 'r') as f:
                    data_tournement = json.load(f)
                choised_tournement = controller.view.get_tournement_to_replay(
                    data_tournement)
                while choised_tournement not in data_tournement.keys() and choised_tournement != None:
                    print("La valeur entrée n'est pas valide")
                    choised_tournement = controller.view.get_tournement_to_replay(
                        data_tournement)

                if choised_tournement != None:
                    dict_tournement = data_tournement[choised_tournement]
                    dict_tournement = controller.start_tournement(
                        dict_tournement)
                    data_tournement[choised_tournement] = dict_tournement
                    with open(controller.data_path, 'w') as f:
                        json.dump(data_tournement, f)
            else:
                print(
                    "Pas de fichier de tournoi enregistré, veuillez créer d'abord un tournoi.")
        elif display_menu == "5":
            break
        else:
            print("Veuillez rentrer un nombre entre 1 et 5 .")


if __name__ == "__main__":
    # jouer le tournoi
    play_tourenement()
