import json
'''
Le fichier main.py comporte la logique de mon programme, appel des methods de mes functions.
'''
from controllers import main_controller
'''
1 - Instanciation de l'objet controller.
2 - Appel de la method qui permet de jouer aux tournois
'''


def play_tournement():
    controller = main_controller.Controller()
    while True:
        display_menu = controller.view.display_menu()
        if display_menu == '1':
            controller.create_tournement()
        elif display_menu == '2':
            controller.display_tournement_infos()
        elif display_menu == '3':
            with open(controller.data_path, 'r') as f:
                data_tournement = json.load(f)
            choised_tournement = controller.view.get_tournement_to_play(
                data_tournement)
            dict_tournement = data_tournement[choised_tournement]
            dict_tournement = controller.start_tournement(dict_tournement)
            data_tournement[choised_tournement] = dict_tournement
            with open(controller.data_path, 'w') as f:
                json.dump(data_tournement, f)
        elif display_menu == '4':
            with open(controller.data_path, 'r') as f:
                data_tournement = json.load(f)
            choised_tournement = controller.view.get_tournement_to_replay(
                data_tournement)
            if choised_tournement != None:
                dict_tournement = data_tournement[choised_tournement]
                dict_tournement = controller.start_tournement(dict_tournement)
                data_tournement[choised_tournement] = dict_tournement
                with open(controller.data_path, 'w') as f:
                    json.dump(data_tournement, f)
        elif display_menu == "5":
            break
        else:
            print("Veuillez entrer un nombre entre 1 et 5 merci.")


if __name__ == '__main__':
    # Jouer le tournoi
    play_tournement()
