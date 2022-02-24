
class Bus : 
    def __init__(self, id_bus, numero, immatriculation, id_ligne):
        self.id = id_bus
        self.numero = numero
        self.immatriculation = immatriculation
        self.id_ligne = id_ligne

class Ligne :
    def __init__(self, id_ligne, numero_ligne, list_bus):
        self.id = id_ligne
        self.numero_ligne = numero_ligne
        self.list_bus = list_bus