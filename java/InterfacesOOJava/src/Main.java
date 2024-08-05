import entidades.Produto;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        // Instanciando uma lista de produto
        var listaDeProdutos = new ArrayList<Produto>();
        System.out.println("Lista de produtos:" + listaDeProdutos);


        // Instanciando um objeto da classe Produto
        var produto = new Produto("notebook", 2500, null);

        // adicionando o objeto a lista
        listaDeProdutos.add(produto);

        System.out.println("Lista de produtos:" + listaDeProdutos);


    }
}