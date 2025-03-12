/* baixar arquivo SCRIPT MODELO PEDIDO no portal do aluno */

@ 'C:\Users\labsfiap\Documents\GitHub\FIAP\2025\banco\SCRIPT_MODELO_PEDIDO(1).SQL';

insert into pais select * from pf1788.pais;
commit;
 
insert into estado select * from pf1788.estado;
commit;
 
alter table cidade modify nom_cidade varchar2(30);
insert into cidade select * from pf1788.cidade;
commit;
 
insert into tipo_endereco select * from pf1788.tipo_endereco;
commit;
 
insert into cliente select * from pf1788.cliente;
commit;
 
insert into vendedor select * from pf1788.vendedor;
commit;
 
insert into cliente_vendedor select * from pf1788.cliente_vendedor;
commit;
 
insert into produto select * from pf1788.produto;
commit;
 
insert into produto_composto select * from pf1788.produto_composto;
commit;
 
insert into tipo_movimento_estoque select * from pf1788.tipo_movimento_estoque;
commit;
 
insert into movimento_estoque select * from pf1788.movimento_estoque;
commit;
 
insert into estoque select * from pf1788.estoque;
commit;
 
insert into estoque_produto select * from pf1788.estoque_produto;
commit;
 
insert into usuario select * from pf1788.usuario;
commit;
 
insert into endereco_cliente select * from pf1788.endereco_cliente;
commit;
 
ALTER TABLE PEDIDO ADD STATUS VARCHAR2(30);
insert into pedido select * from pf1788.pedido;
commit;
 
insert into historico_pedido select * from pf1788.historico_pedido;
commit;