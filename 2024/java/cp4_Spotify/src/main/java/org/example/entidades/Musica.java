package org.example.entidades;

import org.example.servicos.ValidadorEntidades;

public class Musica extends _EntidadeBase{
    private String titulo;
    private int duracao;

    public Musica() {
    }

    public Musica(int id, String titulo, int duracao) {
        super(id);
        this.titulo = titulo;
        this.duracao = duracao;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        if (ValidadorEntidades.PalavraValida(titulo)){
            this.titulo = titulo;
        }
    }

    public int getDuracao() {
        return duracao;
    }

    public void setDuracao(int duracao) {
        if (ValidadorEntidades.NumeroValido(duracao)){
            this.duracao = duracao;
        }
    }

    @Override
    public String toString() {
        return "Musica{" +
                "titulo='" + titulo + '\'' +
                ", duracao=" + duracao +
                "} " + super.toString();
    }
}
