USE Empresa;

CREATE funcionarios (
    id AUTO_INCREMENT PRIMARY KEY,
    funcionario VARCHAR(60) NOT NULL,
    cidade VARCHAR(50),
    data_contratacao DATE
)