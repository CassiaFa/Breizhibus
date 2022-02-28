from classes import Users
from connexion_bdd import Connexion
from log import login
# from class_bus import Bus
def main():
    Connexion.ouvrir_connexion()
    les_bus = Connexion.lister_bus()
    users = Connexion.lister_utilisateurs()
    # login()
    Connexion.Maj_bus(1, 1)
    Connexion.Add_bus('BB05', 'FRR 45 YT', 30, 3)
    Connexion.fermer_connexion()
    main()