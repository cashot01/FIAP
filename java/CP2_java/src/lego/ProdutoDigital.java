package lego;

import java.util.List;

public class ProdutoDigital extends Produto{
    private double tamanho;

    private String tipo_arquivo;

    public ProdutoDigital() {
    }

    public ProdutoDigital(String nome, int idade, double preco, String descricao, String tema, String id_produto, String imagem, List<Avaliacao> avaliacao, double tamanho, String tipo_arquivo) {
        super(nome, idade, preco, descricao, tema, id_produto, imagem, avaliacao);
        this.tamanho = tamanho;
        this.tipo_arquivo = tipo_arquivo;
    }

    public double getTamanho() {
        return tamanho;
    }

    public void setTamanho(double tamanho) {
        this.tamanho = tamanho;
    }

    public String getTipo_arquivo() {
        return tipo_arquivo;
    }

    public void setTipo_arquivo(String tipo_arquivo) {
        this.tipo_arquivo = tipo_arquivo;
    }

    @Override
    public String toString() {
        return "ProdutoDigital{" +
                "tamanho=" + tamanho +
                ", tipo_arquivo='" + tipo_arquivo + '\'' +
                "} " + super.toString();
    }
}
