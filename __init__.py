from flask import Flask, render_template_string, render_template, jsonify, request, redirect, url_for, session
from flask import render_template
from flask import json
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import sqlite3
 
app = Flask(__name__)                                                                                                                  
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Clé secrète pour les sessions

# Fonction pour créer une clé "authentifie" dans la session utilisateur
def est_authentifie():
    return session.get('authentifie')

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/lecture')
def lecture():
    if not est_authentifie():
        # Rediriger vers la page d'authentification si l'utilisateur n'est pas authentifié
        return redirect(url_for('authentification'))

  # Si l'utilisateur est authentifié
    return "<h2>Bravo, vous êtes authentifié</h2>"

@app.route('/authentification', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        # Vérifier les identifiants
        if request.form['username'] == 'admin' and request.form['password'] == 'password': # password à cacher par la suite
            session['authentifie'] = True
            # Rediriger vers la route lecture après une authentification réussie
            return redirect(url_for('lecture'))
        else:
            # Afficher un message d'erreur si les identifiants sont incorrects
            return render_template('formulaire_authentification.html', error=True)

    return render_template('formulaire_authentification.html', error=False)

@app.route('/fiche_client/<int:post_id>')
def Readfiche(post_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE id = ?', (post_id,))
    data = cursor.fetchall()
    conn.close()
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

@app.route('/consultation/')
def ReadBDD():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients;')
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data.html', data=data)

@app.route('/enregistrer_client', methods=['GET'])
def formulaire_client():
    return render_template('formulaire.html')  # afficher le formulaire

@app.route('/enregistrer_client', methods=['POST'])
def enregistrer_client():
    nom = request.form['nom']
    prenom = request.form['prenom']

    # Connexion à la base de données
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Exécution de la requête SQL pour insérer un nouveau client
    cursor.execute('INSERT INTO clients (created, nom, prenom, adresse) VALUES (?, ?, ?, ?)', (1002938, nom, prenom, "ICI"))
    conn.commit()
    conn.close()
    return redirect('/consultation/') 
    
@app.route('/consultation_livres/')
def clivres():
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres;')
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data2.html', data=data)
# Route GET pour afficher le formulaire
@app.route('/ajouter_livre', methods=['GET'])
def formulaire_livre():
    return render_template('form_livre.html')

# Route POST pour enregistrer un livre
@app.route('/ajouter_livre', methods=['POST'])
def enregistrer_livre():
    titre = request.form['titre']
    auteur = request.form['auteur']
    annee_publication = request.form['annee_publication']
    genre = request.form['genre']
    stock = request.form['stock']

    # Connexion à la base de données
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()

    # Exécution de la requête SQL pour insérer un livre
    cursor.execute('INSERT INTO livres (titre, auteur, annee_publication, genre, stock) VALUES (?, ?, ?, ?, ?)', 
                   (titre, auteur, annee_publication, genre, stock))
    conn.commit()
    conn.close()
    
    return redirect('/consultation_livres/')  # Redirige vers la liste des liv

@app.route('/supprimer_livre', methods=['GET'])
def suppression():
    return render_template('supprimer_livre.html')

@app.route('/supprimer_livre', methods=['POST'])
def supprimer_livre():
    id = request.form['id']
    connection = sqlite3.connect('bibliotheque.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM livres WHERE id = ?", (id,))
    connection.commit()
    connection.close()
    
    return redirect('/consultation_livres/')


                                                                                                                                       
if __name__ == "__main__":
  app.run(debug=True)
