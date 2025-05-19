CREATE DATABASE LocacaoJogos;
USE LocacaoJogos;

CREATE TABLE games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    game_name VARCHAR(100) NOT NULL,
    game_price DECIMAL(10, 2) NOT NULL,
    game_quantity INT DEFAULT 0,
    game_genre VARCHAR(100),
    game_description TEXT
);

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    user_email VARCHAR(100) NOT NULL,
    user_password VARCHAR(20) NOT NULL,
    user_admin BOOLEAN DEFAULT FALSE,
    user_status BOOLEAN DEFAULT TRUE
);

CREATE TABLE game_rental (
    game_rental_id  INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    game_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (game_id) REFERENCES games(game_id),
    game_rental_date DATE,
    game_return_date DATE    
);

INSERT INTO games (game_name, game_price, game_quantity, game_genre, game_description) VALUES 
("Borderlands 3", 300, 20, "tiro", "RPG de tiro cartoonizado"),
("Batman lego 2", 50, 100, "aventura", "Lego baseado nas histórias do Batman"),
("Ratchet e Clank rift apart", 300, 50, "aventura", "Aventura espacial futurista"),
("Fifa 2022", 300, 200, "fotebol", "Fotebol de campo"),
("Call of Duty Black ops 6", 350, 60, "tiro", "Guerra, anaquilação, apocalipse e muito caos"),
("Red Dead Redemption 2", 300, 70, "tiro", "tiroteio no faroeste"),
("Minecraft", 100, 200, "aventura", "contruindo um mundo de blocos"),
("Fallout 4", 250, 38, "tiro", "sobrevivência em um mundo pós apocaliptico"),
("The Last of Us Remastered", 350, 80, "tiro", "sobrevivência no apocalipse zumbi"),
("Rayman Legends", 90, 45, "aventura", "A Clareira dos Sonhos está novamente em apuros!"),
("God of War Ragnarok", 300, 85, "acao", "Deuses se decendo na porradaria!"),
("Cuphead", 45, 130, "aventura", "Resolvendo pendências com o capiroto"),
("Dont Starve Together", 50, 55, "aventura", "Sobrevivendo ao desconhecido"),
("Resident Evil Village", 250, 25, "tiro", "sobreviva aos horrores"),
("Sniper Elite 5", 120, 60, "tiro", "vença a guerra como um sniper"),
("Farcry 6", 150, 90, "tiro", "Uma ilha no Caribe governada em regime de ditadura");