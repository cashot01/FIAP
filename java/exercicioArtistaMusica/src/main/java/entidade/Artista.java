package entidade;

public class Artista {
    private int id;
    private String nome;
    private String generoMusial;

    public Artista() {
    }

    public Artista(int id, String nome, String generoMusial) {
        this.id = id;
        this.nome = nome;
        this.generoMusial = generoMusial;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
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
                "id=" + id +
                ", nome='" + nome + '\'' +
                ", generoMusial='" + generoMusial + '\'' +
                '}';
    }
}
