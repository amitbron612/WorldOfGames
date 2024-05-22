CREATE DATABASE IF NOT EXISTS games;
USE games;

CREATE TABLE IF NOT EXISTS users_scores (
    name VARCHAR(255) NOT NULL PRIMARY KEY,
    score INT NOT NULL
);

INSERT INTO users_scores (name, score) VALUES
('Amit', 10),
('Paulo', 20);
