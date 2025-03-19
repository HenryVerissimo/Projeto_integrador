USE LocacaoJogos;

CREATE TABLE jogos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    genero VARCHAR(100),
    descricao TEXT
);

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(20) NOT NULL,
    usuario_status BOOLEAN DEFAULT TRUE
);

CREATE TABLE locacao (
    id  INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_jogo INT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (id_jogo) REFERENCES jogos(id),
    data_locacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    data_devolucao DATE
);
