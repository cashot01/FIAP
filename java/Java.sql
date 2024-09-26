create table PRODUTOS
(
    ID    NUMBER generated as identity,
    NOME  VARCHAR2(255) not null,
    PRECO NUMBER(15, 2) not null
)

