class Ligne :
    def __init__(self, id_ligne, numero_ligne, list_bus, list_arret):
        self.id = id_ligne
        self.numero_ligne = numero_ligne
        self.list_bus = list_bus
        self.list_arret = list_arret

class Bus : 
    def __init__(self, id_bus, numero, immatriculation, id_ligne):
        self.id = id_bus
        self.numero = numero
        self.immatriculation = immatriculation
        self.id_ligne = id_ligne


class Arret :
    def __init__(self, id_arret, nom, adresse):
        self.id_arret = id_arret
        self.nom = nom
        self.adresse = adresse

class Users :
    def __init__(self, id_user, identifiant, mdp):
        self.id_user = id_user
        self.identifiant = identifiant
        self.mdp = mdp