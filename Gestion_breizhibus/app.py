from flask import Flask, render_template, request
from matplotlib.pyplot import get
from connexion_bdd import Connexion

from classes import Arret

app = Flask(__name__)

@app.route('/')
def index() :
    Connexion.ouvrir_connexion()
    lst_ligne = Connexion.lister_ligne()
    Connexion.fermer_connexion()
    return render_template('index.html', lin=lst_ligne)


@app.route('/rouge', methods=["POST"])
def rouge():
    Connexion.ouvrir_connexion()
    ligne=request.values.get("Ligne")
    print("\n==================\n", ligne)
    arrets= Connexion.lister_arret()
    Connexion.fermer_connexion()
    return render_template('rouge.html', arr=arrets)

@app.route('/connexion')
def connexion():
    return render_template('connexion.html')

@app.route('/gestion')
def gestion():
    return render_template('gestion.html')


if __name__== "__main__" :
    app.run(debug=True, port=5001)