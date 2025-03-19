
import sqlite3

connection = sqlite3.connect('bibliotheque.db')

with open('schema2.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO livres (id, created, auteur, titre,annee_publication, genre,stock) VALUES (?, ?,?, ?,?,?,?)",(1, '2025-03-19 10:00:00', 'Le Petit Prince',"Antoine de Saint-Exupéry", 1943, 'Conte philosophique', 5))
cur.execute("INSERT INTO livres (id, created, auteur, titre,annee_publication, genre,stock) VALUES (?, ?,?, ?,?,?,?)",(2, '2025-0-19 10:05:00', '1984', "George Orwell", 1949, 'Science-fiction', 3))
cur.execute("INSERT INTO livres (id, created, auteur, titre,annee_publication, genre,stock) VALUES (?, ?,?, ?,?,?,?)",(3, '2025-03-19 10:10:00', 'L’Étranger',"Albert Camus", 1942, 'Roman', 4))
cur.execute("INSERT INTO livres (id, created, auteur,titre,annee_publication, genre,stock) VALUES (?, ?, ?,?,?,?,?)",(4, '2025-03-19 10:15:00', 'Moby Dick',"Herman Melville", 1851, 'Aventure', 2))
cur.execute("INSERT INTO livres (id, created, auteur,titre,annee_publication, genre,stock) VALUES (?, ?, ?,?,?,?,?)",(5, '2025-03-19 10:20:00', 'Pride and Prejudice',"Jane Austen", 1813, 'Romance', 6))
cur.execute("INSERT INTO livres (id, created, auteur,titre,annee_publication, genre,stock) VALUES (?, ?, ?,?,?,?,?)",(6, '2025-03-19 10:25:00', 'The Great Gatsby',"Scott Fitzgerald, F.", 1925, 'Roman', 7))

connection.commit()
connection.close()


