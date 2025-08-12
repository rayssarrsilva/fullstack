DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS filmes;
DROP TABLE IF EXISTS alugueis;

CREATE TABLE clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(80) NOT NULL,
    email VARCHAR(40)
);

CREATE TABLE filmes (
    id_filme INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    preco_aluguel DECIMAL(10, 2)
);

CREATE TABLE alugueis (
    id_aluguel INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INT,
    id_filme INT,
    devolvido INTEGER DEFAULT 0,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente) ON DELETE CASCADE,
    FOREIGN KEY (id_filme) REFERENCES filmes(id_filme) ON DELETE CASCADE
);