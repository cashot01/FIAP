public class Avaliacao {
    private int pontuacao;
    private String comentario;
    private String nomeUsuario;

    public Avaliacao() {
    }

    public Avaliacao(int pontuacao, String comentario, String nomeUsuario) {
        this.pontuacao = pontuacao;
        this.comentario = comentario;
        this.nomeUsuario = nomeUsuario;
    }

    public int getPontuacao() {
        return pontuacao;
    }

    public void setPontuacao(int pontuacao) {
        this.pontuacao = pontuacao;
    }

    public String getComentario() {
        return comentario;
    }

    public void setComentario(String comentario) {
        this.comentario = comentario;
    }

    public String getNomeUsuario() {
        return nomeUsuario;
    }

    public void setNomeUsuario(String nomeUsuario) {
        this.nomeUsuario = nomeUsuario;
    }

    @Override
    public String toString() {
        return "Avaliacao{" +
                "pontuacao=" + pontuacao +
                ", comentario='" + comentario + '\'' +
                ", nomeUsuario='" + nomeUsuario + '\'' +
                '}';
    }
}
