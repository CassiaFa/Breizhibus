import mysql.connector as mysqlpyth
import classes

class Connexion :
    # Comme on créé une classmethod, on instantie pas la classe avec __init__
    __USER = 'root'
    __PWD = 'root'
    __HOST = 'localhost'
    __PORT = '8081'
    __DB = 'breizhibus'
    __cursor = None

    # cls = classmethod
    @classmethod
    def ouvrir_connexion(cls) :
       if cls.__cursor == None :
            cls.__bdd = mysqlpyth.connect(user = cls.__USER, password = cls.__PWD, host = cls.__HOST, port = cls.__PORT, database = cls.__DB)
            cls.__cursor = cls.__bdd.cursor()
    
    @classmethod
    def lister_bus(cls):
        
        query = "SELECT id_bus, numero, immatriculation, id_ligne FROM bus ORDER BY bus.numero;"
        
        cls.__cursor.execute(query)
        list_bus = []

        for bus in cls.__cursor:
            list_bus.append(classes.Bus(bus[0], bus[1], bus[2], bus[3]))
        return list_bus


    @classmethod
    def Maj_bus(cls, id, ligne):
        requete = "Update bus SET id_ligne = %s WHERE id_bus = %s;"
        param = (ligne, id, )
        cls.__cursor.execute(requete, param)
        cls.__bdd.commit()

    @classmethod
    def fermer_connexion(cls):
        cls.__cursor.close()
        cls.__bdd.close()
        cls.__cursor = None