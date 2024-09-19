package org.example;

import org.example.entidades.Artista;
import org.example.entidades.Musica;
import org.example.repositorios.ArtistaRepositorio;
import org.example.repositorios.MusicaRepositorio;



public class Main {
    public static MusicaRepositorio musicaRepositorio = new MusicaRepositorio();
    public static ArtistaRepositorio artistaRepositorio = new ArtistaRepositorio();
    public static void main(String[] args) {



        var artista = new Artista(1,"MC IG");
        artistaRepositorio.Cadastrar(artista);
        var artista2 = new Artista(2,"Cristiano Araújo");
        artistaRepositorio.Cadastrar(artista2);

        var musica3 = new Musica(3, "Sorriso no Rosto", 148, artista);
        var musica4 = new Musica(4, "Goodnight Menina 3", 209, artista);
        artista.getMusicas().add(musica3);
        artista.getMusicas().add(musica4);


        var musica = new Musica(1, "É Com Ela Que Estou", 226, artista2);
        var musica2 = new Musica(2, "Caso Indefinido", 215, artista2);
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