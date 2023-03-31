class ViewPlayer:
    def get_player_data(self):
        create_players=str(input("voulez vous créer des joueurs (O/N)? "))
        nb_players = 1
        players_list=[]
        if create_players=='O' or create_players=="o":
            for i in range(nb_players):
                print('----------------------------------------------------')
                print(f'Creation du joueur {i+1}')
                last_name = str(input('Entrer votre nom : '))
                first_name = str(input('Entrer maintenant votre prenom : '))
                date_of_birth = str(input('Entrer votre date de naissance :'))
                sexe = str(input('Vous etes un Homme ou une Femme ? '))

                dict_player= {"last_name": last_name,
                            "first_name": first_name,
                            "date_of_birth": date_of_birth,
                            "sexe": sexe}
            
                players_list.append(dict_player)
        
        return players_list