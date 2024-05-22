public class Modulo {
    public String titulo;
    public double duracao;
    public void exibirDetalhes(){

    }

    public Modulo() {
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public double getDuracao() {
        return duracao;
    }

    public void setDuracao(double duracao) {
        this.duracao = duracao;
    }

    @Override
    public String toString() {
        return "Modulo{" +
                "titulo='" + titulo + '\'' +
                ", duracao=" + duracao +
                '}';
    }
}
