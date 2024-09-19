package org.example;

import entidade.Artista;
import entidade.Musica;
import repositorio.ArtistaRepositorio;
import repositorio.MusicaRepositorio;

public class Main {
    public static void main(String[] args) {

        var artistaRepositorio = new ArtistaRepositorio();
        var artista = new Artista(1, "Cauan", "Rock");
        artistaRepositorio.Insert(artista);

        var musicaRepositorio = new MusicaRepositorio();
        var musica  = new Musica(2, "Teste", 234, 2012);
        musicaRepositorio.Insert(musica);
    }
}