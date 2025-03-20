USE RentalGames;

CREATE TABLE games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    game_name VARCHAR(100) NOT NULL,
    game_price DECIMAL(10, 2) NOT NULL,
    game_genre VARCHAR(100),
    game_description TEXT
);

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    user_email VARCHAR(100) NOT NULL,
    user_password VARCHAR(20) NOT NULL,
    user_status BOOLEAN DEFAULT TRUE
);

CREATE TABLE rental (
    rental_id  INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    game_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (game_id) REFERENCES games(game_id),
    rental_data DATETIME DEFAULT CURRENT_TIMESTAMP,
    return_data DATE    
);
