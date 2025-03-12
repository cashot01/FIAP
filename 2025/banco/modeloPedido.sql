/* baixar arquivo SCRIPT MODELO PEDIDO no portal do aluno */

@ 'C:\Users\labsfiap\Documents\GitHub\FIAP\2025\banco\SCRIPT_MODELO_PEDIDO(1).SQL';

insert into pais select * from pf1788.pais;
commit;

select  * from RM555466.pais; 
 
insert into estado select * from pf1788.estado;
commit;

select  * from RM555466.estado;
 
alter table cidade modify nom_cidade varchar2(30);
insert into cidade select * from pf1788.cidade;
commit;

select  * from RM555466.cidade; 
 
insert into tipo_endereco select * from pf1788.tipo_endereco;
commit;

select  * from RM555466.tipo_endereco; 
 
insert into cliente select * from pf1788.cliente;
commit;

select  * from RM555466.cliente; 
 
insert into vendedor select * from pf1788.vendedor;
commit;

select  * from RM555466.vendedor; 
 
insert into cliente_vendedor select * from pf1788.cliente_vendedor;
commit;

select  * from RM555466.cliente_vendedor; 
 
insert into produto select * from pf1788.produto;
commit;

select  * from RM555466.produto; 
 
insert into produto_composto select * from pf1788.produto_composto;
commit;

select  * from RM555466.produto_composto; 
 
insert into tipo_movimento_estoque select * from pf1788.tipo_movimento_estoque;
commit;

select  * from RM555466.tipo_movimento_estoque; 
 
insert into movimento_estoque select * from pf1788.movimento_estoque;
commit;

select  * from RM555466.movimento_estoque;
 
insert into estoque select * from pf1788.estoque;
commit;

select  * from RM555466.estoque;
 
insert into estoque_produto select * from pf1788.estoque_produto;
commit;

select  * from RM555466.estoque_produto;
 
insert into usuario select * from pf1788.usuario;
commit;

select  * from RM555466.usuario;
 
insert into endereco_cliente select * from pf1788.endereco_cliente;
commit;

select  * from RM555466.endereco_cliente;
 
ALTER TABLE PEDIDO ADD STATUS VARCHAR2(30);
insert into pedido select * from pf1788.pedido;
commit;

select  * from RM555466.pedido;
 
insert into historico_pedido select * from pf1788.historico_pedido;
commit;

select  * from RM555466.historico_pedido;