package repositorio;

import entidade.Musica;
import infraestrutura.ConexaoBD;

import java.sql.SQLException;
import java.util.List;
import java.util.Optional;

public class MusicaRepositorio implements _RepositorioBase<Musica>{


    @Override
    public void Insert(Musica musica) {
        try{
            var conn = ConexaoBD.getConnection();
            var query =
                    "INSERT INTO MUSICAS (ID, NOMEMUSICA, DURACAO, DATALANCAMENTO) VALUES (DEFAULT,?,?)";
            var stmt = conn.prepareStatement(query);
            stmt.setString(1, musica.getNomeMusica());
            stmt.setDouble(2, musica.getDuracao());
            stmt.setDate(3, musica.getDataLancamento());
            stmt.executeUpdate();
            stmt.close();
            conn.close();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public void Update(Musica entity, int id) {
        try {
            var conn = ConexaoBD.getConnection();
            var query =
                    "UPDATE MUSICAS SET NOMEMUSICA = ?, DURACAO = ?, DATALANCAMENTO = ? WHERE ID = ?";
            
            var stmt = conn.prepareStatement(query);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

    }

    @Override
    public void Delete(int id) {
        try{
            var conn = ConexaoBD.getConnection();
            var query =
                    "DELETE FROM MUSICAS WHERE ID = ?";
            var stmt = conn.prepareStatement(query);
            stmt.setInt(1, id);
            stmt.executeUpdate();
            stmt.close();
            conn.close();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

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
