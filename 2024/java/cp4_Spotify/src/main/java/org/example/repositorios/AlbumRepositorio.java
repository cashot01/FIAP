package org.example.repositorios;

import org.example.entidades.Album;

import java.util.List;

public class AlbumRepositorio extends RepositorioBaseImp<Album>{
    public List<Album> buscarPorAno(int ano) {
        return lista.stream()
                .filter(album -> album.getAnoDeLancamento() == ano)
                .toList();
    }
}
