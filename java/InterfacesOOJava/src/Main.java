import Entidades.Produto;
import Repositorios.CupomRepositorio;
import Repositorios.LojaRepositorio;
import Repositorios.ProdutoRepositorio;
import Repositorios.VendaRepositorio;
import Servicos.ProdutoServico;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        var produtoServico = new ProdutoServico();
        produtoServico.Cadastrar(new Produto(1,"Produto 1", -10.00));


    }
}