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

SELECT * FROM ESCOLAS_DADOS;
