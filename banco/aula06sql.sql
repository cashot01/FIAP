SELECT * FROM t_endereco;

SELECT * FROM T_ALUNO;

-- insert generico
INSERT INTO t_endereco VALUES (0122345, 'Av. Paulista', 'Centro', 'São Paulo', 'SP');



INSERT INTO t_endereco (cep, logradouro, bairro, cidade)
VALUES (0123454, 'Av. Ipiranga', 'Centro', 'Sao Paulo')

-- ATUALIZAR LINHAS TBELAS
-- UPDATE PROCEDUAL (ESPECIFICO) PARA N LINHAS
UPDATE T_ALUNO SET fk_cep=0131415 WHERE RA=1; 

-- UPDATE NÃO PROCEDUAL (GENERICO) PARA N LINHAS
-- Where é uma restrição de atualização 
-- quando não há o where, essa restrição n existe
UPDATE t_aluno set nome='jose'

