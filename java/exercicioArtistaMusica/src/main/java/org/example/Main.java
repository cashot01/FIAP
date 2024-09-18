package org.example;

import entidade.Artista;
import repositorio.ArtistaRepositorio;

public class Main {
    public static void main(String[] args) {
        var artistaRepositorio = new ArtistaRepositorio();

        var artistas = artistaRepositorio.GetAll();

        var artista = artistaRepositorio.GetById(1);

        artistas.forEach(System.out::println);

        artistaRepositorio.Update(new Artista(1, "Cauan", "Rock"),1);
    }
}