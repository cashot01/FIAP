CREATE TABLE Dados_Escolas (
    ano INT,
    sigla_uf VARCHAR(2),
    id_municipio VARCHAR(10),
    id_escola VARCHAR(10),
    rede VARCHAR(10),
    ensino VARCHAR(15),
    anos_escolares VARCHAR(20),
    taxa_aprovacao NUMBER,
    indicador_rendimento DECIMAL(10, 8),
    nota_saeb_matematica NUMBER,
    nota_saeb_lingua_portuguesa NUMBER,
    nota_saeb_media_padronizada NUMBER,
    ideb NUMBER,
    projecao NUMBER
);

-- DROP TABLE Dados_Escolas;

-- CONSULTA SIMPLES
SELECT * FROM Dados_Escolas;

-- funções numericas
SELECT nota_saeb_media_padronizada FROM Dados_Escolas;

SELECT 
        nota_saeb_media_padronizada, 
        ROUND(nota_saeb_media_padronizada, 2) round_nota, 
        TRUNC (nota_saeb_media_padronizada, 0) trunc_nota,
        MOD (nota_saeb_media_padronizada, 2) mod_nota,
        (nota_saeb_media_padronizada * (-1)) vlr_negativo,
        ABS(nota_saeb_media_padronizada * (-1)) vlr_abs,
        SQRT (nota_saeb_media_padronizada) raiz_quadrada,
        CEIL (nota_saeb_media_padronizada) arr_up,
        FLOOR (nota_saeb_media_padronizada) arr_down

FROM Dados_Escolas;


-- FUNÇÕES DE TEXTO
SELECT 
    rede,
    UPPER(rede) maiusc,
    LOWER(rede) minusc,
    INITCAP(rede) mai_min
FROM Dados_Escolas;  



SELECT 
    rede,
    CONCAT('escola ', rede),
    SUBSTR(rede, 3, 4),
    LENGTH(rede),
    LPAD(rede, 10, '.'),
    RPAD(rede, 10, '.'),
    LTRIM(rede, 'to'),
    RTRIM(rede, 'tal'),
    REPLACE(rede, 'to', 'TO')
FROM Dados_Escolas;    

-- APELIDOS
-- PODE SER DEFENIDOS COM A CLAUSULA AS (ALIAS) OU A FRENTE DO OBJETO
