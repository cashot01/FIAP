import java.util.ArrayList;
import java.util.List;
public class Curso {
    private String titulo;
    private String descricao;
    private double duracao;
    private List<Avaliacao> avaliacoes;
    public Curso() {
    }
    public Curso(String titulo, String descricao, double duracao, List<Avaliacao> avaliacoes) {
        this.titulo = titulo;
        this.descricao = descricao;
        this.duracao = duracao;
        this.avaliacoes = avaliacoes;
    }

    public String getTitulo() {
        return titulo;
    }
    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }
    public String getDescricao() {
        return descricao;
    }
    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }
    public double getDuracao() {
        return duracao;
    }
    public void setDuracao(double duracao) {
        this.duracao = duracao;
    }
    public List<Avaliacao> getAvaliacoes() {
        return avaliacoes;
    }
    public void setAvaliacoes(List<Avaliacao> avaliacoes) {
        this.avaliacoes = avaliacoes;
    }
    @Override
    public String toString() {
        return "Curso{" +
                "titulo='" + titulo + '\'' +
                ", descricao='" + descricao + '\'' +
                ", duracao=" + duracao +
                ", avaliacoes=" + avaliacoes +
                '}';
    }

    public void exibirDetalhes(){
        System.out.println(this );
    }
}
