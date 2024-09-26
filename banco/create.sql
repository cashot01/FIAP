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
-- operadores de comparação 
-- com igual
SELECT * FROM ESCOLAS_DADOS WHERE rede='municipal';

-- com diferente
SELECT * FROM ESCOLAS_DADOS WHERE rede<>'municipal';

-- com maior
SELECT * FROM ESCOLAS_DADOS WHERE ano > 2021;

-- com menor
SELECT * FROM ESCOLAS_DADOS WHERE ano < 2021;

-- com maior igual
SELECT * FROM ESCOLAS_DADOS WHERE ano >= 2021;

-- com menor igual
SELECT * FROM ESCOLAS_DADOS WHERE ano <= 2021;

-- operadores logicos
-- AND
-- intervalos de valores
SELECT * FROM ESCOLAS_DADOS WHERE ano > 2017 and ano < 2020;
SELECT * FROM ESCOLAS_DADOS WHERE ano >= 2017 and ano <= 2020;

-- regras obrigatorias
SELECT * FROM ESCOLAS_DADOS WHERE ano > 2017 and rede='municipal';

-- intervalo com between
SELECT * FROM ESCOLAS_DADOS WHERE ano BETWEEN 2019 and 2021;


-- OR
SELECT * FROM ESCOLAS_DADOS WHERE ano = 2019 or ano=2021;

SELECT * FROM ESCOLAS_DADOS WHERE rede = 'municipal' or ensino = 'fundamental';


-- IN
SELECT * FROM ESCOLAS_DADOS WHERE rede in('municipal', 'privada');




-- cenarios de erros
-- nome coluna ou tabela inexistente
SELECT * FROM ESCOLAS_DADOS WHERE anooooooo > 2017 and ano < 2020;
-- condição logica invalidada
SELECT * FROM ESCOLAS_DADOS WHERE ano > 2017 and ano < 2015;
-- junção incompleta




