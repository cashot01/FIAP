package repositorio;

import entidade.Artista;
import infraestrutura.ConexaoBD;

import java.sql.SQLException;
import java.util.List;
import java.util.Optional;

public class ArtistaRepositorio implements _RepositorioBase<Artista>{

    @Override
    public void Insert(Artista artista) {
        try{
            var conn = ConexaoBD.getConnection();
            var query =
                    "INSERT INTO MUSICAS (ID, NOME, GENEROMUSICAL) VALUES (DEFAULT,?,?)";
            var stmt = conn.prepareStatement(query);
            stmt.setString(1, artista.getNome());
            stmt.setString(2, artista.getGeneroMusial());
            stmt.executeUpdate();
            stmt.close();
            conn.close();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

    }

    @Override
    public void Update(Artista entity, int id) {
        try{
            var conn = ConexaoBD.getConnection();
            var query =
                    "UPDATE ARTISTAS SET NOME = ?, GENEROMUSICAL = ? WHERE ID = ?";
            var stmt = conn.prepareStatement(query);
            stmt.setString(1, entity.getNome());
            stmt.setString(2, entity.getGeneroMusial());
            stmt.setInt(3, id);
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
                    "DELETE FROM ARTISTAS WHERE ID = ?";
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
    public Optional<Artista> GetById(int id) {
        return Optional.empty();
    }

    @Override
    public List<Artista> GetAll() {
        return null;
    }
}
