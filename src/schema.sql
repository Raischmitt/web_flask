DROP TABLE IF EXISTS lista;

CREATE TABLE lista (
  codigo_lista INTEGER PRIMARY KEY AUTOINCREMENT,
  tarefa TEXT NOT NULL
);

INSERT INTO lista (tarefa) values ("dar comida para o cachorro");
INSERT INTO lista (tarefa) values ("brincar com a lili");
INSERT INTO lista (tarefa) values ("passear com o peixe");