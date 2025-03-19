import sqlite3

try:
    # Connexion à la base de données SQLite
    connection = sqlite3.connect('bibliotheque.db')

    # Chargement du schéma SQL
    with open('schema2.sql', 'r', encoding='utf-8') as f:
        connection.executescript(f.read())

    cur = connection.cursor()

    # Insertion des utilisateurs
    utilisateurs = [
        ('Dupont', 'Emilie', 'emilie.dupont@example.com', 'password123', 'utilisateur'),
        ('Leroux', 'Lucas', 'lucas.leroux@example.com', 'securepass', 'utilisateur'),
        ('Martin', 'Amandine', 'amandine.martin@example.com', 'amandinepass', 'admin')
    ]
    cur.executemany("INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, role) VALUES (?, ?, ?, ?, ?)", utilisateurs)

    # Insertion des livres
    livres = [
        ('Le Petit Prince', 'Antoine de Saint-Exupéry', 1943, 'Conte philosophique', 5),
        ('1984', 'George Orwell', 1949, 'Science-fiction', 3),
        ('L’Étranger', 'Albert Camus', 1942, 'Roman', 4)
    ]
    cur.executemany("INSERT INTO livres (titre, auteur, annee_publication, genre, stock) VALUES (?, ?, ?, ?, ?)", livres)

    # Insertion des emprunts (Emilie emprunte "1984")
    emprunts = [
        (1, 2, '2024-03-19', 'emprunté')
    ]
    cur.executemany("INSERT INTO emprunts (id_utilisateur, id_livre, date_emprunt, statut) VALUES (?, ?, ?, ?)", emprunts)

    # Validation des changements
    connection.commit()

except sqlite3.Error as e:
    print(f"Erreur SQLite : {e}")

try:
    conn = sqlite3.connect('database.db')
except sqlite3.Error as e:
    print("Erreur de connexion à la base de données:", e)
    return "Erreur de connexion à la base de données"


finally:
    # Fermeture de la connexion
    if connection:
        connection.close()
