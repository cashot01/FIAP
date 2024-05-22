import java.util.List;

public class ProdutoDigital extends Produto{
    private String tipoDeArquivo;
    private int tamanhoDoArquivo;

    public ProdutoDigital(){}


    public ProdutoDigital(String nome, double preco, String descricao, String tipoDeArquivo, int tamanhoDoArquivo) {
        super(nome, preco, descricao);
        this.tipoDeArquivo = tipoDeArquivo;
        this.tamanhoDoArquivo = tamanhoDoArquivo;
    }

    public ProdutoDigital(String nome, double preco, String descricao, List<Avaliacao> avaliacoes, List<ImagemProduto> imagens, String tipoDeArquivo, int tamanhoDoArquivo) {
        super(nome, preco, descricao, avaliacoes, imagens);
        this.tipoDeArquivo = tipoDeArquivo;
        this.tamanhoDoArquivo = tamanhoDoArquivo;
    }

    public String getTipoDeArquivo() {
        return tipoDeArquivo;
    }

    public void setTipoDeArquivo(String tipoDeArquivo) {
        this.tipoDeArquivo = tipoDeArquivo;
    }

    public int getTamanhoDoArquivo() {
        return tamanhoDoArquivo;
    }

    public void setTamanhoDoArquivo(int tamanhoDoArquivo) {
        this.tamanhoDoArquivo = tamanhoDoArquivo;
    }

    @Override
    public String toString() {
        return "ProdutoDigital{" +
                "tipoDeArquivo='" + tipoDeArquivo + '\'' +
                ", tamanhoDoArquivo=" + tamanhoDoArquivo +
                "} " + super.toString();
    }

    @Override
    public void exibirDetalhes() {
        // this é uma referência ao objeto atual
        System.out.println(this);
    }
}
