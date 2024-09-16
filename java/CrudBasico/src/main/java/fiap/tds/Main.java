package fiap.tds;

import fiap.tds.entities.Produto;
import fiap.tds.repositories.ProdutoRespositorio;

import java.sql.DriverManager;
import java.sql.SQLException;

public class Main {
    public static void main(String[] args) {
        System.out.println("Fazendo insert no oracle");

        var produtoRespositorio = new ProdutoRespositorio();

        //var produto = new Produto(0, "Sprite", 5.5);
        //produtoRespositorio.Insert(produto);
        var produtos = produtoRepositorio.GetAll();
        produtos.forEach(System.out::println);
    }
}