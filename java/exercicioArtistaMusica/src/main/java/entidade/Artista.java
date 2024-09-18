package entidade;

public class Artista extends _EntidadeBase{
    private String nome;
    private String generoMusial;

    public Artista() {
    }

    public Artista(int id, String nome, String generoMusial) {
        super(id);
        this.nome = nome;
        this.generoMusial = generoMusial;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getGeneroMusial() {
        return generoMusial;
    }

    public void setGeneroMusial(String generoMusial) {
        this.generoMusial = generoMusial;
    }

    @Override
    public String toString() {
        return "Artista{" +
                "nome='" + nome + '\'' +
                ", generoMusial='" + generoMusial + '\'' +
                "} " + super.toString();
    }
}
