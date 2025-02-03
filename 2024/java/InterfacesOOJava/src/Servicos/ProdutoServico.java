package Servicos;

import Entidades.Produto;
import Repositorios.ProdutoRepositorio;

import java.util.ArrayList;

public class ProdutoServico {
    ProdutoRepositorio produtoRepositorio;

    public ProdutoServico() {
        this.produtoRepositorio = new ProdutoRepositorio();
    }

    public void Cadastrar(Produto produto){
        var produtoValido = ValidarProduto(produto);
        if(produtoValido)
        {
            produtoRepositorio.cadastrar(produto);
            System.out.println("Produto cadastrado com sucesso");
        }
    }

    public Produto BuscarPorId(int id){
        var produto =  produtoRepositorio.buscarPorId(id);
        if(produto == null){
            System.out.println("Produto não encontrado");
        }
        return produto;
    }

    private boolean ValidarProduto(Produto produto) {
        if(produto.getPreco() < 0){
            System.out.println("Produto com preço negativo");
            return false;
        }
        return true;
    }
}
