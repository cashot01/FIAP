package repositorio;

import entidade.Musica;
import infraestrutura.ConexaoBD;

import java.sql.SQLException;
import java.util.List;
import java.util.Optional;

public class MusicaRepositorio implements _RepositorioBase<Musica>{


    @Override
    public void Insert(Musica entity) {
        try{
            var conn = ConexaoBD.getConnection();

        } catch (SQLException e) {
            throw new RuntimeException(e);
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
