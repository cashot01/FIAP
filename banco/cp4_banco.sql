
-- Criar tabela CLIENTE

CREATE TABLE T_QF_CLIENTE (

    id_cliente INT PRIMARY KEY,
    cpf_cnpj VARCHAR2(15) NOT NULL,
    nm_cliente VARCHAR2(100) NOT NULL,
    dt_nascimento DATE,
    sx_cliente VARCHAR2(2) CHECK (sx_cliente = 'M' OR sx_cliente = 'F'),
    st_cliente VARCHAR2(1) NOT NULL
);
 
-- Criar tabela ENDEREÇO

CREATE TABLE T_QF_ENDERECO (

    id_endereco INT PRIMARY KEY,
    id_cliente INT,
    logradouro VARCHAR2(150) NOT NULL,
    numero VARCHAR2(10) NOT NULL,
    complemento VARCHAR2(100),
    bairro VARCHAR2(100) NOT NULL,
    cidade VARCHAR2(100) NOT NULL ,
    uf VARCHAR2(2) NOT NULL,
    cep VARCHAR2(8) NOT NULL,
    ponto_referencia VARCHAR2(150),
    FOREIGN KEY (id_cliente) REFERENCES T_QF_CLIENTE(id_cliente)
);
 
-- Criar tabela AUTENTICAÇÃO

CREATE TABLE T_QF_AUTENTICA (

    id_autentica INT PRIMARY KEY,
    id_cliente INT,
    login VARCHAR2(20) UNIQUE NOT NULL,
    senha VARCHAR2(30) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES T_QF_CLIENTE(id_cliente)

);
 
-- Criar tabela PEDIDO

CREATE TABLE T_QF_PEDIDO (

    id_pedido INT PRIMARY KEY,
    id_cliente INT,
    id_cupom INT,
    vl_total NUMBER(5, 2) NOT NULL,
    dt_hr_pedido DATE NOT NULL,
    st_pedido VARCHAR2(20) NOT NULL,
    obs_gerais VARCHAR2(255),
    FOREIGN KEY (id_cliente) REFERENCES T_QF_CLIENTE(id_cliente),
    FOREIGN KEY (id_cupom) REFERENCES T_QF_CUPOM(id_cupom)

);
 
-- Criar tabela CUPOM

CREATE TABLE T_QF_CUPOM (

    id_cupom INT PRIMARY KEY,
    cd_cupom VARCHAR2(100) NOT NULL,
    vl_desconto NUMBER(5, 2) NOT NULL,
    val_cupom DATE
);
 
-- Criar tabela PAGAMENTO

CREATE TABLE T_QF_PAGAMENTO (

    id_pagamento INT PRIMARY KEY,
    id_pedido INT,
    forma_pagamento VARCHAR2(20) NOT NULL,
    vl_pagamento NUMBER(5, 2) NOT NULL,
    dt_hr_pagamento DATE not NULL,
    st_pagamento VARCHAR2(20) NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES T_QF_PEDIDO(id_pedido)

);
 
-- Criar tabela ESTOQUE

CREATE TABLE T_QF_ESTOQUE (

    id_estoque INT PRIMARY KEY,
    id_produto INT,
    id_armazem INT,
    qtd_disponivel INT ,
    FOREIGN KEY (id_produto) REFERENCES T_QF_PRODUTO(id_produto),
    FOREIGN KEY (id_armazem) REFERENCES T_QF_ARMAZEM(id_armazem)
);
 
-- Criar tabela ARMAZÉM

CREATE TABLE T_QF_ARMAZEM (

    id_armazem INT PRIMARY KEY,
    ds_armazem VARCHAR2(100) UNIQUE NOT NULL,
    local_armazem VARCHAR2(100) NOT NULL
);
 
-- Criar tabela PRODUTO

CREATE TABLE T_QF_PRODUTO (

    id_produto INT PRIMARY KEY,
    ds_produto VARCHAR2(150) UNIQUE NOT NULL,
    vl_produto NUMBER(5, 2) NOT NULL,
    peso NUMBER(5, 2) NOT NULL,
    dimensoes VARCHAR2(20) NOT NULL,
    id_categoria INT,
    id_marca INT,
    FOREIGN KEY (id_categoria) REFERENCES T_QF_CATEGORIA(id_categoria),
    FOREIGN KEY (id_marca) REFERENCES T_QF_MARCA(id_marca)

);
 
-- Criar tabela CATEGORIA

CREATE TABLE T_QF_CATEGORIA (

    id_categoria INT PRIMARY KEY,
    ds_categoria VARCHAR2(1500) UNIQUE NOT NULL
);
 
-- Criar tabela MARCA

CREATE TABLE T_QF_MARCA (

    id_marca INT PRIMARY KEY,

    ds_marca VARCHAR2(100) UNIQUE NOT NULL

);
 
-- Criar tabela ITEM_PEDIDO

CREATE TABLE T_QF_ITEM_PEDIDO (

    id_item INT PRIMARY KEY,

    id_pedido INT,

    id_produto INT,

    qt_produto INT NOT NULL,

    vl_subtotal NUMBER(5, 2) NOT NULL,
    vl_desconto NUMBER(5, 2), 

    FOREIGN KEY (id_pedido) REFERENCES T_QF_PEDIDO(id_pedido),

    FOREIGN KEY (id_produto) REFERENCES T_QF_PRODUTO(id_produto)

);
 
-- Adiciona no campo dt_hr_estoque na tabela T_QF_ESTOQUE

ALTER TABLE T_QF_ESTOQUE

ADD dt_hr_estoque DATE;
 
-- Adiciona no campo cor_produto na tabela T_QF_PRODUTO

ALTER TABLE T_QF_PRODUTO

ADD cor_produto VARCHAR2(20);
 
 
DROP TABLE T_QF_ITEM_PEDIDO;

DROP TABLE T_QF_MARCA;

DROP TABLE T_QF_CATEGORIA;

DROP TABLE T_QF_PRODUTO;

DROP TABLE T_QF_ARMAZEM;

DROP TABLE T_QF_ESTOQUE;

DROP TABLE T_QF_PAGAMENTO;

DROP TABLE T_QF_CUPOM;

DROP TABLE T_QF_PEDIDO;

DROP TABLE T_QF_AUTENTICA;

DROP TABLE T_QF_ENDERECO;

DROP TABLE T_QF_CLIENTE;
 
 
 
 