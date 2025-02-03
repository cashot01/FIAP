package org.example.repositorios;

import org.example.entidades.Artista;

import java.util.List;

public class ArtistaRepositorio extends RepositorioBaseImp<Artista>{
    public List<Artista> buscarPorGenero(String genero){
        return lista.stream()
                .filter(artista -> artista.getGeneroMusical().equalsIgnoreCase(genero))
                .toList();
    }
}
