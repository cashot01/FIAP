import java.util.ArrayList;
import java.util.List;

public abstract class Produto {
    protected String nome;
    protected double preco;
    protected String descricao;
    protected List<Avaliacao> avaliacoes = new ArrayList<>();
    protected List<ImagemProduto> imagens = new ArrayList<>();

    public Produto() {
    }

    public Produto(String nome, double preco, String descricao) {
        this.nome = nome;
        this.preco = preco;
        this.descricao = descricao;
    }

    public Produto(String nome, double preco, String descricao, List<Avaliacao> avaliacoes, List<ImagemProduto> imagens) {
        this.nome = nome;
        this.preco = preco;
        this.descricao = descricao;
        this.avaliacoes = avaliacoes;
        this.imagens = imagens;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
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

    public List<Avaliacao> getAvaliacoes() {
        return avaliacoes;
    }

    public void setAvaliacoes(List<Avaliacao> avaliacoes) {
        this.avaliacoes = avaliacoes;
    }

    public List<ImagemProduto> getImagens() {
        return imagens;
    }

    public void setImagens(List<ImagemProduto> imagens) {
        this.imagens = imagens;
    }

    @Override
    public String toString() {
        return "Produto{" +
                "nome='" + nome + '\'' +
                ", preco=" + preco +
                ", descricao='" + descricao + '\'' +
                ", avaliacoes=" + avaliacoes +
                ", imagens=" + imagens +
                '}';
    }

    public abstract void exibirDetalhes();
}
