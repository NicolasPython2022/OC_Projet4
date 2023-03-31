
class ViewTournoi:
    def get_data_tournoi(self):
        # Creation du tournoi
        create_tournement= str(input('Voulez vous creer du nouveau tournoi (O/N)? '))
        dict_tournoi = {}
        if create_tournement=='O' or create_tournement=="o":
            print("---------------------------------------------------------")
            print("Creation du Tournoi")
            name = str(input("Entrer un nom de Tournoi : "))
            place = str(input("Entrer le lieu du Tournoi : "))
            date = str(input("Entrer la date du Tournoi : "))
            director_remark = str(input("Remarques du directeur du Tournoi : "))

            dict_tournoi=      {"name": name,
                                "place": place,
                                "date": date,
                                "director_remark": director_remark
                                }
        
        return dict_tournoi