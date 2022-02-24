from connexion_bdd import Connexion
# from class_bus import Bus
def main():
    Connexion.ouvrir_connexion()
    les_bus = Connexion.lister_bus()
    Connexion.fermer_connexion()
    for bus in les_bus :
        print(bus.numero)   

main()
