from flask import Flask, render_template, request
from connexion_bdd import Connexion

app = Flask(__name__)

@app.route('/')
def index() :
    return render_template('index.html')


@app.route('/connexion')
def connexion():
    return render_template('connexion.html')

@app.route('/gestion', methods=['POST'])
def gestion():    
    login = request.values.get('user')
    mdp = request.values.get('mdp')

    Connexion.ouvrir_connexion()

    if login == None:
        droits = request.values.get('droits')
        num = request.values.get('n_bus')
        immat = request.values.get('immat')
        nb_place = request.values.get('nb_place')
        id_ligne = request.values.get('ligne')
        Connexion.Add_bus(num, immat, nb_place, id_ligne)
    else:
        droits = Connexion.check_user(login, mdp)
    
    

    bus = Connexion.lister_bus()
    arrets = Connexion.lister_arret()
    lignes = Connexion.lister_ligne()
    Connexion.fermer_connexion()
    
    return render_template('gestion.html', droits = droits, bus = bus, arrets = arrets, lignes = lignes )


if __name__== "__main__" :
    app.run(debug=True, port=5001)