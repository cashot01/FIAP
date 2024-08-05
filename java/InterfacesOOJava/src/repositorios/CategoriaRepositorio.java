package repositorios;

import entidades.Categoria;
import entidades.Produto;

import java.util.ArrayList;

public class CategoriaRepositorio {
    private ArrayList<Produto> categorias;

    public CategoriaRepositorio() {
        this.categorias = new ArrayList<>();
    }
    public void adicionar(Produto novoProduto){
        categorias.add(novoProduto);
    }
    public void remover(Produto produto){
        categorias.remove(produto);
    }
    public ArrayList<Produto> listar(){
        return categorias;
    }
}
