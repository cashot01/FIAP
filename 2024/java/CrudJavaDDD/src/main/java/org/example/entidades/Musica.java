package org.example.entidades;

public class Musica extends _EntidadeBase{
    private String titulo;
    private int duracao;
    private transient Artista artista;

    public Musica() {
    }

    public Musica(int id, String titulo, int duracao, Artista artista) {
        super(id);
        this.titulo = titulo;
        this.duracao = duracao;
        this.artista = artista;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public int getDuracao() {
        return duracao;
    }

    public void setDuracao(int duracao) {
        this.duracao = duracao;
    }

    public Artista getArtista() {
        return artista;
    }

    public void setArtista(Artista artista) {
        this.artista = artista;
    }

    @Override
    public String toString() {
        return "Musica{" +
                "titulo='" + titulo + '\'' +
                ", duracao=" + duracao +
                ", artista=" + artista +
                '}';
    }
}
