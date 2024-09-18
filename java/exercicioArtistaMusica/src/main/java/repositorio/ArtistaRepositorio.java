package repositorio;

import entidade.Artista;
import entidade.Musica;
import infraestrutura.ConexaoBD;

import java.sql.SQLException;
import java.util.ArrayList;
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
        Optional<Artista> artista = Optional.empty();
        try{
            var conn = ConexaoBD.getConnection();
            var query = "SELECT * FROM ARTISTAS WHERE ID = ?";
            var stmt = conn.prepareStatement(query);
            stmt.setInt(1, id);
            var rs = stmt.executeQuery();
            if(rs.next()){
                var _id = rs.getInt("ID");
                var nome = rs.getString("NOME");
                var generomusical = rs.getString("GENEROMUSICAL");
                artista = Optional.of(new Artista(_id, nome, generomusical));
            }

            rs.close();
            stmt.close();
            conn.close();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

        return artista;
    }

    @Override
    public List<Artista> GetAll() {
        var artistas = new ArrayList<Musica>();
        try{
            var conn = ConexaoBD.getConnection();
            var query = "SELECT * FROM ARTISTAS WHERE NOME LIKE ? ORDER BY ID";
            var stmt = conn.prepareStatement(query);
            stmt.setString(1, "%" + nome + "%");
            var rs = stmt.executeQuery();
            while (rs.next()){
                var id = rs.getInt("ID");
                var nome = rs.getString("NOME");
                var generomusical = rs.getString("GENEROMUSICAL");
                artistas.add(new Musica(id, nome, generomusical));
            }
            rs.close();
            stmt.close();
            conn.close();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

        return musicas;
    }

}
