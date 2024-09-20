 SELECT * FROM T_ENDERECO;
 
 SELECT * FROM T_ALUNO;
 

-- GENÉRICO (NÃO PROCEDURAL) 
 INSERT INTO T_ENDERECO VALUES(01311000,'Av. Paulista',
                                'Centro','São Paulo','SP');
 INSERT INTO T_ENDERECO VALUES (01310100, 'Rua da Consolação','Centro',
                                    'São Paulo','SP');                                
                                    
-- ESPECIFICO (OU PROCEDURAL)
-- É OBRIGATÓRIO MENCIONAR AS COLUNAS NOT NULL E PK
-- PK POSSUI EXCEÇÃO QUANDO HÁ O GENERATED

INSERT INTO T_ENDERECO (cep, logradouro,bairro, cidade)
 VALUES (0131415,'Av. Ipiranga', 'Centro','São Paulo');
 
 -- ATUALIZAR LINHAS NA TABELAS
 
 -- UPDATE PROCEDURAL (OU ESPECIFICO) PARA 1ª LINHA
 UPDATE T_ALUNO SET cep=0131415 WHERE id_aluno=1;
 
 -- UPDATE NÃO PROCEDURAL (OU ESPECIFICO) PARA TODAS AS LINHAS
 -- WHERE É UMA RESTRIÇÃO DE ATUALIZAÇÃO
 -- QUANDO NÃO HÁ O WHERE, ESSA RESTRIÇÃO NÃO EXISTE
 UPDATE T_ALUNO SET nm_aluno='José';
 
 -- UPDATE PROCEDURAL (OU ESPECIFICO) PARA N LINHAS
 -- DEPENDENDO DA RESTRIÇÃO NO WHERE, PODERÁ ATUALIZAS TODAS AS LNHAS OU ALGUMAS DELAS
 UPDATE T_ALUNO SET nm_aluno='Lucas' WHERE id_aluno>=1;
 
 INSERT INTO T_ALUNO (nm_aluno, sx_aluno, cep, cpf) 
    VALUES ('Maria Eduarda','F',0131415, 222333);
INSERT INTO T_ALUNO (nm_aluno, sx_aluno, cep, cpf) 
    VALUES ('Lucia','F',0131415, 222334);
 INSERT INTO T_ALUNO (nm_aluno, sx_aluno, cep, cpf) 
    VALUES ('Maria','F',0131415, 222335);
 -- UPDATE ESPECIFICO PARA MAIS DE 1 COLUNA
 -- SEPARAR COLUNAS POR VIGULAS APOS O SET
 
 UPDATE T_ALUNO SET nm_aluno='Francisco Douglas', 
                    sx_aluno='M', 
                    dt_nascimento=to_date('19-09-2004','DD-MM-YYYY') 
        WHERE id_aluno=2; 
        
-- APAGAR OS DADOS DA TABELA
-- ESPECIFICA (PROCEDURAL)
-- WHERE É UMA RESTRIÇÃO DE REMOÇÃO
DELETE FROM T_ALUNO WHERE id_aluno=2;

-- GENÉRICA (NÃO PROCEDURAL)
-- Irá remover todas as linhas da tabela, pois não há o WHERE
DELETE FROM T_ALUNO;


-- DTL (Data Transaction Language)
-- commit: confirmar transação
-- rollback: desfazer a trasação
-- É utilizada em conjunto com a DML (INSERT, UPDATE e DELETE)

commit;

rollback;

DELETE FROM T_ENDERECO;
ROLLBACK;

UPDATE T_ENDERECO SET cidade='Campinas';
ROLLBACK;

INSERT INTO T_ENDERECO (cep, logradouro,bairro, cidade)
 VALUES (0131416,'Av. Ipiranga', 'Centro','São Paulo');
ROLLBACK;

INSERT INTO T_ENDERECO (cep, logradouro,bairro, cidade)
 VALUES (0131416,'Av. Ipiranga', 'Centro','São Paulo');
COMMIT;

ROLLBACK;

-- NÃO HÁ ROLLBACKS APÓS O COMMIT
-- O COMMIT É A DEFINIÇÃO DE UM "FIM DE TRABALHO", 
-- NO QUAL NÃO PODE SER DESFEITO

-- REMOVER AS LINHAS DA TABELA 
SELECT * FROM T_ENDERECO;

-- SO PODEMOS REMOVER LINHAS QUE NÃO ESTÃO RELACIONADAS COM OUTRAS TABELAS
-- CASO AO CONTRÁRIO, HAVERÁ O ERRO 2292 SOBRE A FK

-- TRUNCATE
-- UTILIZAR TODAS AS LINHAS DA TABELA, DE MANEIRA FISICA
-- NÃO EXISTE ROLLBACK/COMMIT PARA TRUNCATE
-- APAGARÁ TUDO DE FORMA PERMANENTE

TRUNCATE TABLE T_ALUNO;
ROLLBACK; -- NÃO IRÁ FUNCIONAR
SELECT * FROM T_ALUNO;