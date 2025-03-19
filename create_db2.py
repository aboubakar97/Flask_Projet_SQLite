import sqlite3

# Connexion à la base de données SQLite
connection = sqlite3.connect('bibliotheque.db')

# Chargement du schéma SQL
with open('schema2.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Insertion des utilisateurs
cur.execute("INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, role) VALUES (?, ?, ?, ?, ?)",
            ('Dupont', 'Emilie', 'emilie.dupont@example.com', 'password123', 'utilisateur'))
cur.execute("INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, role) VALUES (?, ?, ?, ?, ?)",
            ('Leroux', 'Lucas', 'lucas.leroux@example.com', 'securepass', 'utilisateur'))
cur.execute("INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, role) VALUES (?, ?, ?, ?, ?)",
            ('Martin', 'Amandine', 'amandine.martin@example.com', 'amandinepass', 'admin'))

# Insertion des livres
cur.execute("INSERT INTO livres (titre, auteur, annee_publication, genre, stock) VALUES (?, ?, ?, ?, ?)",
            ('Le Petit Prince', 'Antoine de Saint-Exupéry', 1943, 'Conte philosophique', 5))
cur.execute("INSERT INTO livres (titre, auteur, annee_publication, genre, stock) VALUES (?, ?, ?, ?, ?)",
            ('1984', 'George Orwell', 1949, 'Science-fiction', 3))
cur.execute("INSERT INTO livres (titre, auteur, annee_publication, genre, stock) VALUES (?, ?, ?, ?, ?)",
            ('L’Étranger', 'Albert Camus', 1942, 'Roman', 4))

# Insertion des emprunts (Emilie emprunte "1984")
cur.execute("INSERT INTO emprunts (id_utilisateur, id_livre, date_emprunt, statut) VALUES (?, ?, ?, ?)",
            (1, 2, '2024-03-19', 'emprunté'))

# Validation des changements et fermeture de la connexion
connection.commit()
connection.close()
