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
("Borderlands 3", 65, 20, "tiro", "RPG de tiro cartoonizado"),
("Batman lego 2", 20, 100, "aventura", "Lego baseado nas histórias do Batman"),
("Ratchet e Clank rift apart", 65, 50, "aventura", "Aventura espacial futurista"),
("Fifa 2022", 55, 200, "fotebol", "Fotebol de campo"),
("Call of Duty Black ops 6", 60, 60, "tiro", "Guerra, anaquilação, apocalipse e muito caos"),
("Red Dead Redemption 2", 70, 70, "tiro", "tiroteio no faroeste"),
("Minecraft", 20, 200, "aventura", "contruindo um mundo de blocos"),
("Fallout 4", 55, 38, "tiro", "sobrevivência em um mundo pós apocaliptico"),
("The Last of Us Remastered", 70, 80, "tiro", "sobrevivência no apocalipse zumbi"),
("Rayman Legends", 30, 45, "aventura", "A Clareira dos Sonhos está novamente em apuros!"),
("God of War Ragnarok", 50, 85, "acao", "Deuses se decendo na porradaria!"),
("Cuphead", 45, 130, "aventura", "Resolvendo pendências com o capiroto"),
("Dont Starve Together", 30, 55, "aventura", "Sobrevivendo ao desconhecido"),
("Resident Evil Village", 60, 25, "tiro", "sobreviva aos horrores"),
("Sniper Elite 5", 55, 60, "tiro", "vença a guerra como um sniper"),
("Farcry 6", 60, 90, "tiro", "Uma ilha no Caribe governada em regime de ditadura");

INSERT INTO users (user_name, user_email, user_password, user_admin, user_status) VALUES
  ('João Silva',       'joao.silva@example.com',       'a1B2c3D4', FALSE, TRUE),
  ('Maria Oliveira',    'maria.oliveira@example.com',    'xYz12345', FALSE, TRUE),
  ('Pedro Souza',       'pedro.souza@example.com',       'P4s5w6Rd', FALSE, FALSE),
  ('Ana Santos',        'ana.santos@example.com',        'QwErTy12', FALSE, TRUE),
  ('Lucas Lima',        'lucas.lima@example.com',        'LmN0pQrS', FALSE, TRUE),
  ('Beatriz Costa',     'beatriz.costa@example.com',     'zXcVbN12', FALSE, TRUE),
  ('Rafael Alves',      'rafael.alves@example.com',      'RfAlVs34', FALSE, FALSE),
  ('Camila Ferreira',   'camila.ferreira@example.com',   'CaMiLa56', FALSE, TRUE),
  ('Gustavo Pereira',   'gustavo.pereira@example.com',   'GuStAv78', FALSE, TRUE),
  ('Fernanda Gomes',    'fernanda.gomes@example.com',    'FeRnAn90', FALSE, TRUE),
  ('Tiago Ribeiro',     'tiago.ribeiro@example.com',     'TiAgO12X', FALSE, FALSE),
  ('Juliana Carvalho',  'juliana.carvalho@example.com',  'JuLiAn34', FALSE, TRUE),
  ('Felipe Dias',       'felipe.dias@example.com',       'FeLiPe56', FALSE, TRUE),
  ('Carolina Martins',  'carolina.martins@example.com',  'CaRoLi78', FALSE, FALSE),
  ('Bruno Rocha',       'bruno.rocha@example.com',       'BrUnO90R', FALSE, TRUE),
  ('Larissa Castro',    'larissa.castro@example.com',    'LaRiSs12', FALSE, TRUE),
  ('Vinícius Araújo',   'vinicius.araujo@example.com',   'ViNiCi34', FALSE, TRUE),
  ('Aline Menezes',     'aline.menezes@example.com',     'AlInE56', FALSE, FALSE),
  ('Marcelo Mendes',    'marcelo.mendes@example.com',    'MaRcEl78', FALSE, TRUE),
  ('Daniela Pires',     'daniela.pires@example.com',     'DaNiEl90', FALSE, FALSE);

INSERT INTO game_rental 
    (user_id, game_id, game_rental_date, game_return_date) VALUES
  ( 1,  5, '2025-01-03', '2025-01-10'),
  ( 2,  3, '2025-01-15', '2025-01-22'),
  ( 3,  1, '2025-01-20', '2025-01-27'),
  ( 4,  7, '2025-02-02', '2025-02-09'),
  ( 5, 12, '2025-02-10', '2025-02-17'),
  ( 6,  4, '2025-02-14', '2025-02-21'),
  ( 7,  8, '2025-03-01', '2025-03-08'),
  ( 8, 11, '2025-03-05', '2025-03-12'),
  ( 9,  2, '2025-03-10', '2025-03-17'),
  (10, 16, '2025-03-15', '2025-03-22'),
  (11,  6, '2025-04-01', '2025-04-08'),
  (12, 13, '2025-04-07', '2025-04-14'),
  (13, 14, '2025-04-12', '2025-04-19'),
  (14, 10, '2025-04-18', '2025-04-25'),
  (15,  9, '2025-05-02', '2025-05-09'),
  (16, 15, '2025-05-05', '2025-05-12'),
  (17,  7, '2025-05-08', '2025-05-15'),
  (18,  3, '2025-05-10', '2025-05-17'),
  (19, 12, '2025-05-12', '2025-05-19'),
  (20,  1, '2025-05-14', '2025-05-21');
