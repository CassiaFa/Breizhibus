import mysql.connector as mysqlpyth
from classes import Users, Bus, Ligne, Arret

class Connexion :

    __USER = 'root'
    __PWD = 'root'
    __HOST = 'localhost'
    __PORT = '8081'
    __DB = 'breizhibus_test'
    __cursor = None

    @classmethod
    def ouvrir_connexion(cls) :
       if cls.__cursor == None :
            cls.__bdd = mysqlpyth.connect(user = cls.__USER, password = cls.__PWD, host = cls.__HOST, port = cls.__PORT, database = cls.__DB)
            cls.__cursor = cls.__bdd.cursor()
    
    @classmethod
    def lister_bus(cls):
        
        query = "SELECT id_bus, numero, immatriculation, nombre_place, id_ligne FROM bus ORDER BY bus.numero;"        
        cls.__cursor.execute(query)
        list_bus = []
        for bus in cls.__cursor:
            list_bus.append(Bus(bus[0], bus[1], bus[2], bus[3], bus[4]))
        return list_bus

    @classmethod
    def lister_ligne(cls):
        
        query = "SELECT id_ligne, nom FROM lignes;"        
        cls.__cursor.execute(query)
        list_ligne = []
        for ligne in cls.__cursor:
            list_ligne.append(Ligne(ligne[0], ligne[1]))
        return list_ligne

    @classmethod
    def lister_arret(cls):
        
        query = "SELECT id_arret, nom, adresse FROM arrets;"        
        cls.__cursor.execute(query)
        list_arret = []
        for arret in cls.__cursor:
            list_arret.append(Arret(arret[0], arret[1], arret[2]))
        return list_arret

    @classmethod
    def lister_utilisateurs(cls):
        query = "SELECT id_user, identifiant, mdp FROM users;"          
        cls.__cursor.execute(query)
        list_users = []
        for user in cls.__cursor:
            list_users.append(Users(user[0], user[1], user[2]))
        return list_users

    @classmethod
    def Maj_bus(cls, bus, ligne):
        requete = "UPDATE bus SET id_ligne = %s WHERE id_bus = %s;"
        param = (ligne, bus )
        cls.__cursor.execute(requete, param)
        cls.__bdd.commit()
    
    @classmethod
    def Add_bus(cls, numero, immatriculation, nombre_place, id_ligne):
        requete = "INSERT INTO bus (numero, immatriculation, nombre_place, id_ligne) VALUES (%s,%s, %s, %s);"
        param = (numero, immatriculation, nombre_place, id_ligne )
        cls.__cursor.execute(requete, param)
        cls.__bdd.commit()

    @classmethod
    def Sup_bus(cls, id_bus):
        requete = "DELETE FROM bus WHERE id_bus = %s ;"
        param = (id_bus,)
        cls.__cursor.execute(requete, param)
        cls.__bdd.commit()

    @classmethod
    def fermer_connexion(cls):
        cls.__cursor.close()
        cls.__bdd.close()
        cls.__cursor = None