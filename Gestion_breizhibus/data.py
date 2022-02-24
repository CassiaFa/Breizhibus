import mysql.connector as msql
from sympy import total_degree

bdd = None
cursor = None

def connexion():
    global bdd
    global cursor

    bdd = msql.connect(user='root', password='root', host='localhost', port="8081", database='clients')
    cursor = bdd.cursor()

def deconnexion():
    global bdd
    global cursor

    cursor.close()
    bdd.close()

def get_bus(id) :
    global cursor

    connexion()
    query ="SELECT * FROM bus"
    # WHERE id=" + str(id)
    cursor.execute(query)
    utilisateurs = []
    global total
    total=0

    for enregistrement in cursor :
        utilisateur = {}
        utilisateur['id'] = enregistrement[0]
        utilisateur['nom'] = enregistrement[1]
        utilisateur['prenom'] = enregistrement[2]
        utilisateur['telephone'] = enregistrement[3]
        utilisateur['email'] = enregistrement [4]
        utilisateur['age'] = enregistrement [5]
        utilisateur['sexe'] = enregistrement [6]
        utilisateur['pourquoi'] = enregistrement [7]
        utilisateur['montant'] = enregistrement [8]
        utilisateurs.append(utilisateur)
        
    deconnexion()
    return (utilisateurs)

def somme ():
    connexion()
    total = 0
    query ="SELECT * FROM users"
    cursor.execute(query)
    for enregistrement in cursor :
            total +=enregistrement[8]
    deconnexion()
    return (total)

def set_utilisateur(nom, prenom, telephone, email, age, sexe, pourquoi, montant):
    global bdd
    global cursor

    connexion()

    query='INSERT INTO users(nom, prenom, telephone, email, age, sexe, pourquoi, montant) VALUES ("'+nom+'","'+prenom+'","'+telephone+'","'+email+'","'+age+'","'+sexe+'","'+pourquoi+'","'+montant+'")'
    cursor.execute(query)
    bdd.commit()

    deconnexion()


