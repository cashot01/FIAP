package repositorio;

import entidade.Musica;
import infraestrutura.ConexaoBD;

import java.sql.Date;
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
            stmt.setDate(3, (Date) musica.getDataLancamento());
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
            stmt.setString(1, entity.getNomeMusica());
            stmt.setDouble(2, entity.getDuracao());
            stmt.setDate(3, (Date) entity.getDataLancamento());
            stmt.setInt(4, id);
            stmt.executeUpdate();
            stmt.close();
            conn.close();

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
        Optional<Musica> musica = Optional.empty();
        try{
            var conn = ConexaoBD.getConnection();
            var query = "SELECT * FROM MUSICAS WHERE ID = ?";
            var stmt = conn.prepareStatement(query);
            stmt.setInt(1, id);
            var rs = stmt.executeQuery();
            if(rs.next()){
                var _id = rs.getInt("ID");
                var nomeMusica = rs.getString("NOMEMUSICA");
                var duracao = rs.getDouble("DURACAO");
                var dataLancamento = rs.getDate("DATALANCAMENTO");
                musica = Optional.of(new Musica(_id, nomeMusica, duracao, dataLancamento));
            }
            rs.close();
            stmt.close();
            conn.close();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

        return musica;

    }

    @Override
    public List<Musica> GetAll() {
        return List.of();
    }
}
