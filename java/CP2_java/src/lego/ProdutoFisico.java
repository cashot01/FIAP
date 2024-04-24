package lego;

public class ProdutoFisico extends Produto{
    private double peso;

    private  int lego_insides_points;

    private int qtd_pecas;

    private int minifigures;

    private double dimenssao_H;

    private double dimenssao_W;

    private double dimenssao_D;

    public ProdutoFisico() {
    }

    public ProdutoFisico(double peso, int lego_insides_points, int qtd_pecas, int minifigures, double dimenssao_H, double dimenssao_W, double dimenssao_D) {
        this.peso = peso;
        this.lego_insides_points = lego_insides_points;
        this.qtd_pecas = qtd_pecas;
        this.minifigures = minifigures;
        this.dimenssao_H = dimenssao_H;
        this.dimenssao_W = dimenssao_W;
        this.dimenssao_D = dimenssao_D;
    }
}
