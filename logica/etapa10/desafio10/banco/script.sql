DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS filmes;
DROP TABLE IF EXISTS alugueis;

CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    nome VARCHAR(80) NOT NULL,
    email VARCHAR(40)
);

CREATE TABLE filmes (
    id_filme INT PRIMARY KEY,
    titulo VARCHAR(100),
    categoria VARCHAR(50) NOT NULL,
    preco_aluguel DECIMAL(10, 2)
);

CREATE TABLE alugueis (
    id_aluguel INT PRIMARY KEY,
    id_cliente INT,
    id_filme INT,
    devolvido BOOLEAN NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_filme) REFERENCES filmes(id_filme)
);