import mysql.connector as mysqlpyth
from classes import Users, Bus

class Connexion :
    # Comme on créé une classmethod, on instantie pas la classe avec __init__
    __USER = 'root'
    __PWD = 'root'
    __HOST = 'localhost'
    __PORT = '8081'
    __DB = 'breizhibus_test'
    __cursor = None

    # cls = classmethod
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
    def Sup_bus(cls, numero, immatriculation, nombre_place, id_ligne):
        requete = "INSERT INTO bus (numero, immatriculation, nombre_place, id_ligne) VALUES (%s,%s, %s, %s);"
        param = (numero, immatriculation, nombre_place, id_ligne )
        cls.__cursor.execute(requete, param)
        cls.__bdd.commit()

    @classmethod
    def fermer_connexion(cls):
        cls.__cursor.close()
        cls.__bdd.close()
        cls.__cursor = None

    @classmethod
    def lister_utilisateurs(cls):
        
        query = "SELECT id_user, identifiant, mdp FROM users;"
        
        cls.__cursor.execute(query)
        list_users = []

        for user in cls.__cursor:
            list_users.append(Users(user[0], user[1], user[2]))
        return list_users
