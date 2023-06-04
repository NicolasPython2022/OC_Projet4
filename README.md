# Projet4

## Organisation d'un tournoi d'echec sous python qui fonctionne hors ligne.
Ce projet consiste en un programme permettant de jouer a un tournoi d'echec avec 8 joueur parametrer, afin qu'ils puissent de facon aleatoire se rencontrer pour des matchs de 4 rounds, et qui se verront attribuer des scores a chaque etape d'un round effectuer.
Un tableau des scores de chacun est alors etabli et sauvergarder dans un fichier json, auquel vous pourrez acceder via le menu qui s'affichera une fois le programme lancer, si :
    - Un tournoi a deja ete creer
    - Un tournoi a ete jouer en partie (ex: 2 round sur les 4 d'un tournoi complet)
    - Un tournoi a ete terminer
Si aucun tournoi n'a ete creer avant votre choix d'en afficher les infos, alors un message vous indiquera d'en creer un avant tout.

Vous pourrez donc commencer ou mettre en pause un tournoi creer.
Apres chaque round effectuer il vous sera alors propser de continuer ou bien de mettre en pause le tournoi jouer.
Le menu principal vous sera alors proposer comme nouveau choix a effectuer.
Chaque tournoi, chaque round de matchs est automatiquement sauvegarder et consultable via le menu.

## Chartre du projet
Le projet respecte ici le modele MVC qui organise chaque modules et scripts du projet selon ces regles de models, view, controller.
A - Le module models contient les classes de stucture logique sous-jacente des donnees du logiciel mais aucune information sur l'interface de l'utilisateur.
B - Le module de la view est un ensemble de methodes ici d'une classe appellee View(), qui represente les elements de l'interface utilisateur, c'est a dire tout ce que l'utilisateur peut voir a l'ecran.
C - Le module controllers lui represente les classes qui interargissent avec le module models ou bien celui de la view et sert ainsi a la communication entre eux.

## Norme du projet
Le projet respecte la norme d'ecriture flake8 qui est installer en packet dans le fichier requirements.txt, ainsi que la convention pep8.

## Installation du projet
1 - Installation sur votre ordinateur de la derniere version de python (3.11.3) ici : https://www.python.org/downloads/

2 - Ouvrir votre editeur de texte et lancer votre terminal afin de cloner le projet ci-dessus : git clone https://github.com/NicolasPython2022/OC_Projet4.git

3 - Entrer le lien du projet cloner dans votre ligne de commande afin que celui-ci s'installe.

4 - Installer un environnement virtuel via la ligne de commande : python3 -m .env

5 - Telecharchement les packets pip du fichier requirements.txt via la ligne de commande : pip install -r requirements.txt

# Lancement du programme du programme
1 - Activer votre environnement virtuel : source .env/bin/activate

2 - Le programme etant ecrit en 100% python, taper dans la ligne de commande : python3 main.py

3 - Le programme etant maintenant lancer, veuillez selectionner un choix parmis ceux qui vous sont presenter.
