create table petshop(
id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
tipo_pet VARCHAR2(30),
nome_pet VARCHAR2(30),
idade INT
);

select * from  petshop;