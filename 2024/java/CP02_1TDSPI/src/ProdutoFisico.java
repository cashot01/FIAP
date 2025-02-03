import java.util.List;

public class ProdutoFisico extends Produto{
    private double peso;
    private Dimensoes dimensoes;

    public ProdutoFisico(){

    }

    public ProdutoFisico(String nome, double preco, String descricao, double peso, Dimensoes dimensoes) {
        super(nome, preco, descricao);
        this.peso = peso;
        this.dimensoes = dimensoes;
    }

    public ProdutoFisico(String nome, double preco, String descricao, List<Avaliacao> avaliacoes, List<ImagemProduto> imagens, double peso, Dimensoes dimensoes) {
        super(nome, preco, descricao, avaliacoes, imagens);
        this.peso = peso;
        this.dimensoes = dimensoes;
    }

    public double getPeso() {
        return peso;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    public Dimensoes getDimensoes() {
        return dimensoes;
    }

    public void setDimensoes(Dimensoes dimensoes) {
        this.dimensoes = dimensoes;
    }

    @Override
    public String toString() {
        return "ProdutoFisico{" +
                "peso=" + peso +
                ", dimensoes=" + dimensoes +
                "} " + super.toString();
    }

    @Override
    public void exibirDetalhes() {
        System.out.println(this);
    }
}
