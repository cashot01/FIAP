package org.example.entidades;

import org.example.servicos.ValidadorEntidades;

import java.util.ArrayList;
import java.util.List;

public class Artista extends _EntidadeBase{
    private String nome;
    private String generoMusical;
    private List<Album> albuns = new ArrayList<>();

    public Artista() {
    }

    public Artista(int id, String nome, String generoMusical) {
        super(id);
        setNome(nome);
        setGeneroMusical(generoMusical);
    }

    public List<Album> getAlbuns() {
        return albuns;
    }

    public void setAlbuns(List<Album> albuns) {
        this.albuns = albuns;
    }

    public String getGeneroMusical() {
        return generoMusical;
    }

    public void setGeneroMusical(String generoMusical) {
        if (ValidadorEntidades.PalavraValida(generoMusical)){
            this.generoMusical = generoMusical;
        }
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        if (ValidadorEntidades.PalavraValida(nome)){
            this.nome = nome;
        }
    }

    @Override
    public String toString() {
        return "Artista{" +
                "nome='" + nome + '\'' +
                ", generoMusical='" + generoMusical + '\'' +
                ", albuns=" + albuns +
                "} " + super.toString();
    }
}
