package org.example.entidades;

import java.util.ArrayList;
import java.util.List;

public class Artista extends _EntidadeBase{
    private String nome;
    private List<Musica> musicas = new ArrayList<>();

    public Artista() {
    }

    public Artista(String nome) {
        this.nome = nome;
    }

    public Artista(int id, String nome) {
        super(id);
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public List<Musica> getMusicas() {
        return musicas;
    }

    public void setMusicas(List<Musica> musicas) {
        this.musicas = musicas;
    }

    @Override
    public String toString() {
        return "Artista{" +
                "nome='" + nome + '\'' +
                ", musicas=" + musicas +
                '}';
    }
}
