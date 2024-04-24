package lego;

import java.util.ArrayList;
import java.util.List;

public class Produto {
    private String nome;
    private int idade;
    private  double preco;
    private String descricao;
    private String tema;
    private String id_produto;
    private String imagem;
    private ArrayList<Avaliacao> avaliacoes;


    public void exibirDetalhes(){




    }

    public Produto() {
    }

    public Produto(String nome, int idade, double preco, String descricao, String tema, String id_produto, String imagem, ArrayList<Avaliacao> avaliacao) {
        this.nome = nome;
        this.idade = idade;
        this.preco = preco;
        this.descricao = descricao;
        this.tema = tema;
        this.id_produto = id_produto;
        this.imagem = imagem;
        this.avaliacoes = avaliacao;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public String getTema() {
        return tema;
    }

    public void setTema(String tema) {
        this.tema = tema;
    }

    public String getId_produto() {
        return id_produto;
    }

    public void setId_produto(String id_produto) {
        this.id_produto = id_produto;
    }

    public String getImagem() {
        return imagem;
    }

    public void setImagem(String imagem) {
        this.imagem = imagem;
    }

    public ArrayList<Avaliacao> getAvaliacao() {
        return avaliacoes;
    }

    public void setAvaliacao(ArrayList<Avaliacao> avaliacoes) {
        this.avaliacoes = avaliacoes;
    }

    @Override
    public String toString() {
        return "Produto{" +
                "nome='" + nome + '\'' +
                ", idade=" + idade +
                ", preco=" + preco +
                ", descricao='" + descricao + '\'' +
                ", tema='" + tema + '\'' +
                ", id_produto='" + id_produto + '\'' +
                ", imagem='" + imagem + '\'' +
                ", avaliacao=" + avaliacoes +
                '}';
    }
}
