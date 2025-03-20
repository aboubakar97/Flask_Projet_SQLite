
import sqlite3

connection = sqlite3.connect('bibliotheque.db')

with open('schema2.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO livres (titre,auteur,annee_publication, genre,stock) VALUES (?, ?,?,?,?)",( 'Le Petit Prince',"Antoine de Saint-Exupéry", 1943, 'Conte philosophique', 5))
cur.execute("INSERT INTO livres (titre,auteur,annee_publication, genre,stock) VALUES (?, ?,?,?,?)",( '1984', "George Orwell", 1949, 'Science-fiction', 3))
cur.execute("INSERT INTO livres (titre,auteur,annee_publication, genre,stock) VALUES (?, ?,?,?,?)",( 'L’Étranger',"Albert Camus", 1942, 'Roman', 4))
cur.execute("INSERT INTO livres (titre,auteur,annee_publication, genre,stock) VALUES ( ?,?,?,?,?)",( 'Moby Dick',"Herman Melville", 1851, 'Aventure', 2))
cur.execute("INSERT INTO livres  (titre,auteur,annee_publication, genre,stock) VALUES ( ?,?,?,?,?)",( 'Pride and Prejudice',"Jane Austen", 1813, 'Romance', 6))
cur.execute("INSERT INTO livres (titre,auteur,annee_publication, genre,stock) VALUES ( ?,?,?,?,?)",( 'The Great Gatsby',"Scott Fitzgerald, F.", 1925, 'Roman', 7))

connection.commit()
connection.close()


