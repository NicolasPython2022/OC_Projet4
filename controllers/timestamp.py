# Import du type de base pour la date et l'heure
from datetime import datetime


# Mehode d'obtention de l'horodatage
def get_timestamp():
    # now()methode qui donne la date et le temps actuels
    return datetime.now().strftime("%d/%m/%Y-%H:%M:%S")


'''
time.strftime(format[, t])
Convertit un n-uplet ou struct_time représentant une heure renvoyée par gmtime() ou localtime() en une chaîne spécifiée par l’argument format.

Si t n’est pas fourni, l’heure actuelle renvoyée par localtime() est utilisée .format doit être une chaîne.

Si l’un des champs de t se situe en dehors de la plage autorisée, une ValueError est levée .

Signification

Notes

Représentation appropriée de la date et de l’heure selon les paramètres régionaux.

%d

Jour du mois sous forme décimale [01,31].

%H

Jour de l’année sous forme de nombre décimal [001,366].

%m

Mois sous forme décimale [01,12].

%M

Minutes sous forme décimale [00,59].

%p

L’équivalent local de AM ou PM.

(1)

%S

Secondes sous forme de nombre décimal [00,61].

(2)

Année sans siècle comme un nombre décimal [00, 99].

%Y

Un caractère '%' littéral.



'''