from controllers import main_controller
#from controllers import control_tournoi

'''
1 - Faire l'instanciation ici de mon controller.
2 - Faire appel a la methode qui recupere les infos d'un joueur : controller.view.get_players_data()
'''

# Instance de controller avec appel de la class
controller = main_controller.ControlPlayer()

#tournoi = control_tournoi.ControlTournoi(players).control_data_tournoi()

players_list = controller.view_player.get_player_data()

#print(players_list)


# Appel de la method qui me retourne les valeurs souhaiter que j'assigne a ma var players
players = controller.control_player_data(players_list)

for player in players:
    print(player.last_name)
    print(player.first_name)
    print(player.date_of_birth)
    print(player.sexe)


#print(tournoi.name)