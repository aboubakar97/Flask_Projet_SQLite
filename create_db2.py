import sqlite3
from datetime import date

# Connexion à la base de données
connection = sqlite3.connect('bibliotheque.db')

# Exécution du schéma pour créer les tables si elles n'existent pas
with open('schema2.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Ajout d'exemples de livres
cur.execute("INSERT INTO livres (titre, auteur, annee_publication, genre, stock) VALUES (?, ?, ?, ?, ?)",
            ('Le Petit Prince', 'Antoine de Saint-Exupéry', 1943, 'Conte philosophique', 5))

cur.execute("INSERT INTO livres (titre, auteur, annee_publication, genre, stock) VALUES (?, ?, ?, ?, ?)",
            ('1984', 'George Orwell', 1949, 'Science-fiction', 3))

cur.execute("INSERT INTO livres (titre, auteur, annee_publication, genre, stock) VALUES (?, ?, ?, ?, ?)",
            ('L’Étranger', 'Albert Camus', 1942, 'Roman', 4))

cur.execute("INSERT INTO livres (titre, auteur, annee_publication, genre, stock) VALUES (?, ?, ?, ?, ?)",
            ('Moby Dick', 'Herman Melville', 1851, 'Aventure', 2))

cur.execute("INSERT INTO livres (titre, auteur, annee_publication, genre, stock) VALUES (?, ?, ?, ?, ?)",
            ('Pride and Prejudice', 'Jane Austen', 1813, 'Romance', 6))

cur.execute("INSERT INTO livres (titre, auteur, annee_publication, genre, stock) VALUES (?, ?, ?, ?, ?)",
            ('The Great Gatsby', 'Scott Fitzgerald, F.', 1925, 'Roman', 7))

# Ajout d'exemples d'utilisateurs
cur.execute("INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, role) VALUES (?, ?, ?, ?, ?)",
            ('Dupont', 'Jean', 'jean.dupont@email.com', 'motdepasse123', 'utilisateur'))

cur.execute("INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, role) VALUES (?, ?, ?, ?, ?)",
            ('Martin', 'Sophie', 'sophie.martin@email.com', 'password456', 'admin'))

cur.execute("INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, role) VALUES (?, ?, ?, ?, ?)",
            ('Durand', 'Paul', 'paul.durand@email.com', 'securepass', 'utilisateur'))

# Ajout d'exemples d'emprunts
cur.execute("INSERT INTO emprunts (id_utilisateur, id_livre, date_emprunt, date_retour, statut) VALUES (?, ?, ?, ?, ?)",
            (1, 1, date.today().strftime('%Y-%m-%d'), '2025-04-01', 'emprunté'))  # Dupont emprunte Le Petit Prince
cur.execute("INSERT INTO emprunts (id_utilisateur, id_livre, date_emprunt, date_retour, statut) VALUES (?, ?, ?, ?, ?)",
            (2, 2, date.today().strftime('%Y-%m-%d'), '2025-04-10', 'emprunté'))  # Martin emprunte 1984

# Ajout d'exemples de recommandations
cur.execute("INSERT INTO recommandations (id_utilisateur, id_livre, raison) VALUES (?, ?, ?)",
            (1, 2, 'Recommandation basée sur le genre Science-fiction'))  # Recommandation de 1984 à Dupont
cur.execute("INSERT INTO recommandations (id_utilisateur, id_livre, raison) VALUES (?, ?, ?)",
            (2, 1, 'Recommandation basée sur les contes philosophiques'))  # Recommandation du Petit Prince à Martin

# Ajout d'exemples de notifications
cur.execute("INSERT INTO notifications (id_utilisateur, message, lu) VALUES (?, ?, ?)",
            (1, 'Votre livre "Le Petit Prince" doit être retourné avant le 1er avril.', 0))  # Notification pour Dupont
cur.execute("INSERT INTO notifications (id_utilisateur, message, lu) VALUES (?, ?, ?)",
            (2, 'Votre livre "1984" doit être retourné avant le 10 avril.', 0))  # Notification pour Martin

# Validation des modifications
connection.commit()

# Fermeture de la connexion
connection.close()
