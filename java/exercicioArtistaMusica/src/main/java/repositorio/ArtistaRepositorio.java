package repositorio;

import entidade.Artista;

import java.util.List;
import java.util.Optional;

public class ArtistaRepositorio implements _RepositorioBase<Artista>{
    @Override
    public void Insert(Artista entity) {
        
    }

    @Override
    public void Update(Artista entity, int id) {

    }

    @Override
    public void Delete(int id) {

    }

    @Override
    public Optional<Artista> GetById(int id) {
        return Optional.empty();
    }

    @Override
    public List<Artista> GetAll() {
        return List.of();
    }
}
