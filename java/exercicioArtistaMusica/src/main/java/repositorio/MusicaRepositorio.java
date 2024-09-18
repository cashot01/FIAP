package repositorio;

import entidade.Musica;

import java.util.List;
import java.util.Optional;

public class MusicaRepositorio implements _RepositorioBase<Musica>{


    @Override
    public void Insert(Musica entity) {
        try{
            var conn =
        }
    }

    @Override
    public void Update(Musica entity, int id) {

    }

    @Override
    public void Delete(int id) {

    }

    @Override
    public Optional<Musica> GetById(int id) {
        return Optional.empty();
    }

    @Override
    public List<Musica> GetAll() {
        return List.of();
    }
}
