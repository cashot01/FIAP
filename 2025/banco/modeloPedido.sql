/* baixar arquivo SCRIPT MODELO PEDIDO no portal do aluno */

@ 'C:\Users\labsfiap\Documents\GitHub\FIAP\2025\banco\SCRIPT_MODELO_PEDIDO(1).SQL';

INSERT into pais SELECT * from pf1788.pais;
commit;

INSERT into estado SELECT * from pf1788.estado;
commit;

INSERT into cidade SELECT * from pf1788.cidade;
commit;

INSERT into tipo_endereco SELECT * from pf1788.tipo_endereco;
commit;

INSERT into endereco_cliente SELECT * from pf1788.endereco_cliente;
commit;


ALTER TABLE cidade MODIFY nom_cidade VARCHAR2(30);

ALTER TABLE PEDIDO ADD STATUS VARCHAR2(30);