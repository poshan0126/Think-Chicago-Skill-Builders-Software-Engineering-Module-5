CREATE DATABASE MusicLibrary;
USE MusicLibrary;

-- Task 1
-- Create the Genre table

CREATE TABLE Genre (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL
);

-- Create the Artists table
CREATE TABLE Artists (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

-- Create the Albums table
CREATE TABLE Albums (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    artist_id INT NOT NULL,
    genre_id INT NOT NULL,
    release_year YEAR,
    total_tracks INT
);

-- Task 2
-- Alter the Albums table to add the duration column
ALTER TABLE Albums
ADD COLUMN duration INT;


-- Task 3
-- Add foreign key constraints to the Albums table
ALTER TABLE Albums
ADD CONSTRAINT fk_albums_artist
FOREIGN KEY (artist_id) REFERENCES Artists(id);

ALTER TABLE Albums
ADD CONSTRAINT fk_albums_genre
FOREIGN KEY (genre_id) REFERENCES Genre(id);
