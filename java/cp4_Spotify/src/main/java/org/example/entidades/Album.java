package org.example.entidades;

import org.example.servicos.ValidadorEntidades;

import java.util.ArrayList;
import java.util.List;

public class Album extends _EntidadeBase {
    private String titulo;
    private int anoDeLancamento;
    private List<Musica> musicas = new ArrayList<>();

    public Album() {
    }

    public Album(int id, String titulo, int anoDeLancamento, List<Musica> musicas) {
        super(id);
        this.titulo = titulo;
        this.anoDeLancamento = anoDeLancamento;
        this.musicas = musicas;
    }

    public int getAnoDeLancamento() {
        return anoDeLancamento;
    }

    public void setAnoDeLancamento(int anoDeLancamento) {
        if (ValidadorEntidades.NumeroValido(anoDeLancamento)){
            this.anoDeLancamento = anoDeLancamento;
        }
    }

    public List<Musica> getMusicas() {
        return musicas;
    }

    public void setMusicas(List<Musica> musicas) {
        this.musicas = musicas;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        if (ValidadorEntidades.PalavraValida(titulo)){
            this.titulo = titulo;
        }
    }

    @Override
    public String toString() {
        return "Album{" +
                "titulo='" + titulo + '\'' +
                ", anoDeLancamento=" + anoDeLancamento +
                ", musicas=" + musicas +
                "} " + super.toString();
    }
}
