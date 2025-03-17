USE LocacaoJogos;

CREATE TABLE jogos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    genero VARCHAR(100) DEFAULT 'genero não fornecido',
    descricao TEXT DEFAULT 'Descrição não fornecida',
    imagem BLOB

);

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    icone  BLOB,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(20) NOT NULL,
    estado ENUM("ativo", "inativo") DEFAULT 'ativo'

);

CREATE TABLE locacao (
    id  INT AUTO_INCREMENT PRIMARY KEY,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (id_jogo) REFERENCES jogos(id),
    data_locacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    data_devolucao DATE

);

