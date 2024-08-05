package repositorios;

import entidades.Produto;

import java.util.ArrayList;

public class ProdutoRepositorio {
    private ArrayList<Produto> produtos;

    public ProdutoRepositorio() {
        this.produtos = new ArrayList<>();
    }
    public void adicionar(Produto novoProduto){
        produtos.add(novoProduto);
    }
    public void remover(Produto produto){
        produtos.remove(produto);
    }
    public ArrayList<Produto> listar(){
        return produtos;
    }
}
