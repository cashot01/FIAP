CREATE TABLE escolas_dados (
    ano NUMBER,
    sigla_uf VARCHAR2(2),
    id_municipio NUMBER,
    id_escola NUMBER,
    rede VARCHAR2(50),
    ensino VARCHAR2(50),
    anos_escolares VARCHAR2(50),
    taxa_aprovacao VARCHAR2(10),
    indicador_rendimento VARCHAR2(20),
    nota_saeb_matematica VARCHAR2(20),
    nota_saeb_lingua_portuguesa VARCHAR2(20),
    nota_saeb_media_padronizada VARCHAR2(20),
    ideb VARCHAR2(10),
    projecao VARCHAR2(10)
);

-- n procedural (consulta simples)
-- retorna todas as linhas da tablas
SELECT * FROM ESCOLAS_DADOS;

-- n procedural (consulta simples)
-- retorna todas as linhas da tablas
SELECT SIGLA_UF, ENSINO, ANOS_ESCOLARES FROM ESCOLAS_DADOS;

-- OPERADORES PARA WHERE
-- LOGICOS: OR, AND e NOT
/* COMPARAÇÃO: 
    > (MAIOR),
    < (MENOR),
    >= (MAIOR IGUAL),
    <= (MENOR IGUAL),
    <> (DIFERENTE) e
    = (IGUAL)
    
    
MATEMATICOS:
    +
    -
    *
    /
    
    
COMPARAÇÃO COM FUNÇÃO:
    BETWEEN: VERIFICAR INTERVALOS DE VALORES (TEM A MESMA LOGICA DO AND)
    IN: LISTA DE VALORES (TEM A MESMA LOGICA DO OR)
*/

-- procedural
SELECT * FROM ESCOLAS_DADOS WHERE rede='municipal';
