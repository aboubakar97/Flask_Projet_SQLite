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
    return redirect('/consultation/')  # Rediriger vers la page d'accueil après l'enregistrement

# Route pour afficher tous les utilisateurs
@app.route('/utilisateurs')
def utilisateurs():
    try:
        conn = sqlite3.connect('bibliotheque.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM utilisateurs;")
        utilisateurs = cursor.fetchall()
        conn.close()
        return render_template('utilisateurs.html', utilisateurs=utilisateurs)
    except sqlite3.Error as e:
        return f"Erreur de connexion ou d'exécution de la requête: {e}"

# Route pour afficher tous les livres
@app.route('/livres')
def livres():
    try:
        conn = sqlite3.connect('bibliotheque.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM livres;")
        livres = cursor.fetchall()
        conn.close()
        return render_template('read_data2.html', livres=livres)
    except sqlite3.Error as e:
        return f"Erreur de connexion ou d'exécution de la requête: {e}"

# Route pour enregistrer un client (utilisateur)
@app.route('/enregistrer_utilisateur', methods=['GET', 'POST'])
def enregistrer_utilisateur():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        email = request.form['email']
        mot_de_passe = request.form['mot_de_passe']
        role = request.form['role']

        try:
            conn = sqlite3.connect('bibliotheque.db')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, role) VALUES (?, ?, ?, ?, ?)",
                (nom, prenom, email, mot_de_passe, role)
            )
            conn.commit()
            conn.close()
            return redirect(url_for('utilisateurs'))
        except sqlite3.Error as e:
            return f"Erreur lors de l'enregistrement du client: {e}"

    return render_template('formulaire_client.html')

# Route pour consulter les emprunts
@app.route('/emprunts')
def emprunts():
    try:
        conn = sqlite3.connect('bibliotheque.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM emprunts;")
        emprunts = cursor.fetchall()
        conn.close()
        return render_template('emprunts.html', emprunts=emprunts)
    except sqlite3.Error as e:
        return f"Erreur de connexion ou d'exécution de la requête: {e}"

# Route pour emprunter un livre (ajout dans la table des emprunts)
@app.route('/emprunter/<int:id_livre>', methods=['POST'])
def emprunter(id_livre):
    if not est_authentifie():
        return redirect(url_for('authentification'))

    try:
        conn = sqlite3.connect('bibliotheque.db')
        cursor = conn.cursor()

        # Récupérer l'id de l'utilisateur depuis la session
        id_utilisateur = session['user_id']

        # Ajouter un emprunt dans la base de données
        cursor.execute(
            "INSERT INTO emprunts (id_utilisateur, id_livre, date_emprunt, statut) VALUES (?, ?, ?, ?)",
            (id_utilisateur, id_livre, '2024-03-19', 'emprunté')
        )
        conn.commit()
        conn.close()

        return redirect(url_for('emprunts'))
    except sqlite3.Error as e:
        return f"Erreur lors de l'emprunt du livre: {e}"

# Route pour s'authentifier
@app.route('/authentification', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        # Vérifier les identifiants (exemple simple)
        username = request.form['username']
        password = request.form['password']

        # Vérifier l'utilisateur dans la base de données
        try:
            conn = sqlite3.connect('bibliotheque.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM utilisateurs WHERE email = ? AND mot_de_passe = ?", (username, password))
            utilisateur = cursor.fetchone()
            conn.close()

            if utilisateur:
                session['authentifie'] = True
                session['user_id'] = utilisateur[0]  # Id de l'utilisateur
                return redirect(url_for('index'))
            else:
                return "Identifiants incorrects", 401
        except sqlite3.Error as e:
            return f"Erreur lors de l'authentification: {e}"

    return render_template('formulaire_authentification.html')
                                                                                                                                       
if __name__ == "__main__":
  app.run(debug=True)
