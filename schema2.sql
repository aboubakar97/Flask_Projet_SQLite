-- Table des utilisateurs (clients et administrateurs)
DROP TABLE IF EXISTS utilisateurs;
CREATE TABLE utilisateurs (
    id INT PRIMARY KEY ,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    mot_de_passe VARCHAR(255) NOT NULL,
    role ENUM('utilisateur', 'admin') NOT NULL
);

-- Table des livres
DROP TABLE IF EXISTS livres;
CREATE TABLE livres (
    id INT PRIMARY KEY ,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    titre VARCHAR(255) NOT NULL,
    auteur VARCHAR(150) NOT NULL,
    annee_publication INT NOT NULL,
    genre VARCHAR(100) NOT NULL,
    stock INT NOT NULL DEFAULT 1
);

-- Table des emprunts (gestion des prêts et retours)
DROP TABLE IF EXISTS emprunts;
CREATE TABLE emprunts (
    id INT PRIMARY KEY ,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    id_utilisateur INT NOT NULL,
    id_livre INT NOT NULL,
    date_emprunt DATE NOT NULL,
    date_retour DATE DEFAULT NULL,
    statut ENUM('emprunté', 'retourné', 'en retard') NOT NULL DEFAULT 'emprunté',
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateurs(id) ON DELETE CASCADE,
    FOREIGN KEY (id_livre) REFERENCES livres(id) ON DELETE CASCADE
);

-- Table des recommandations (suggestions basées sur les emprunts)
DROP TABLE IF EXISTS recommandations;
CREATE TABLE recommandations (
    id INT PRIMARY KEY ,
    id_utilisateur INT NOT NULL,
    id_livre INT NOT NULL,
    raison TEXT NOT NULL,
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateurs(id) ON DELETE CASCADE,
    FOREIGN KEY (id_livre) REFERENCES livres(id) ON DELETE CASCADE
);

-- Table des notifications (retours en retard, nouvelles recommandations, etc.)
DROP TABLE IF EXISTS notifications;
CREATE TABLE notifications (
    id INT PRIMARY KEY ,
    id_utilisateur INT NOT NULL,
    message TEXT NOT NULL,
    date_notification TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    lu BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateurs(id) ON DELETE CASCADE
);
