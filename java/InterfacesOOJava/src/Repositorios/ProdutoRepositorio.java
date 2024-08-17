package Repositorios;

import Entidades.Produto;

import java.util.ArrayList;

public class ProdutoRepositorio extends _RepositorioBaseImpl<Produto>{

    public ArrayList<Produto> buscarPorNome(String nome){
        var produtosFiltrados = new ArrayList<Produto>();
        produtosFiltrados = lista.stream().filter(produto ->
                produto.getNome().contains(nome))
                .collect(ArrayList::new, ArrayList::add, ArrayList::addAll);

        return produtosFiltrados;
    }
}