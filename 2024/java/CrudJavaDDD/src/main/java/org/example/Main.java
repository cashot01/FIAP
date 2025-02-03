package org.example;

import org.example.entidades.Artista;
import org.example.entidades.Musica;
import org.example.repositorios.ArtistaRepositorio;
import org.example.repositorios.MusicaRepositorio;



public class Main {
    public static MusicaRepositorio musicaRepositorio = new MusicaRepositorio();
    public static ArtistaRepositorio artistaRepositorio = new ArtistaRepositorio();
    public static void main(String[] args) {



        var artista = new Artista(1,"MC Daniel");
        artistaRepositorio.Cadastrar(artista);
        var artista2 = new Artista(2,"Gustavo Lima");
        artistaRepositorio.Cadastrar(artista2);

        var musica3 = new Musica(3, "Dentro da Hilux", 148, artista);
        var musica4 = new Musica(4, "Vamo de Pagodin", 209, artista);
        artista.getMusicas().add(musica3);
        artista.getMusicas().add(musica4);


        var musica = new Musica(1, "60 segundos", 226, artista2);
        var musica2 = new Musica(2, "Desejo Imortal", 215, artista2);
        artista.getMusicas().add(musica);
        artista.getMusicas().add(musica2);



        for ( Musica mus: artista.getMusicas()) {
            musicaRepositorio.Cadastrar(mus);
        }

        for ( Musica mus: artista2.getMusicas()) {
            musicaRepositorio.Cadastrar(mus);
        }

    }
}