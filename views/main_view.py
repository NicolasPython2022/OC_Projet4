

class ViewPlayer:
    def get_player_data(self):
        create_players=str(input("voulez vous créer des joueurs (O/N)? "))
        nb_players = 8
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


class ViewTournoi:
    def get_data_tournoi(self):
        # Creation du tournoi
        create_tournement= str(input('Voulez vous creer un nouveau tournoi (O/N)? '))
        dict_tournoi = {}
        if create_tournement=='O' or create_tournement=="o":
            print("---------------------------------------------------------")
            print("Creation du Tournoi")
            name = str(input("Entrer un nom de Tournoi : "))
            place = str(input("Entrer le lieu du Tournoi : "))
            date_debut = str(input("Entrer la date de debut du Tournoi : "))
            date_fin = str(input("Entrer la date de fin du tournoi : "))
            director_remark = str(input("Remarques du directeur du Tournoi : "))

            dict_tournoi=      {"name": name,
                                "place": place,
                                "date_debut": date_debut,
                                "date_fin": date_fin,
                                "director_remark": director_remark
                                }
        
        return dict_tournoi