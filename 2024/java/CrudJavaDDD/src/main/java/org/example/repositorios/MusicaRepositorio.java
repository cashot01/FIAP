package org.example.repositorios;

import org.example.entidades.Artista;
import org.example.entidades.Musica;
import org.example.infraestrutura.DatabaseConfig;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class MusicaRepositorio implements _CrudRepositorio<Musica> {
    @Override
    public void Cadastrar(Musica entidade) {
        try {
            Connection conn = DatabaseConfig.getConnection();
            String query = "INSERT INTO MUSICA (ID, TITULO, DURACAO, ARTISTA_ID) VALUES(DEFAULT, ?, ?, ?)";
            PreparedStatement stmt = conn.prepareStatement(query);
            stmt.setString(1, entidade.getTitulo());
            stmt.setInt(2, entidade.getDuracao());
            stmt.setInt(3, entidade.getArtista().getId());
            stmt.executeUpdate();
            stmt.close();
            conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void Atualizar(Musica entidade, int id) {
        try {
            Connection conn = DatabaseConfig.getConnection();
            String query = "UPDATE MUSICA SET TITULO = ?, DURACAO = ?, ARTISTA_ID = ? WHERE ID = ?";
            PreparedStatement stmt = conn.prepareStatement(query);
            stmt.setString(1, entidade.getTitulo());
            stmt.setInt(2, entidade.getDuracao());
            stmt.setInt(3, entidade.getArtista().getId());
            stmt.setInt(4, id);
            stmt.executeUpdate();
            stmt.close();
            conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void Deletar(int id) {
        try {
            Connection conn = DatabaseConfig.getConnection();
            String query = "DELETE FROM MUSICA WHERE ID = ?";
            PreparedStatement stmt = conn.prepareStatement(query);
            stmt.setInt(1, id);
            stmt.executeUpdate();
            stmt.close();
            conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    @Override
    public Optional<Musica> BuscarPorId(int id) {
        Optional<Musica> musica = Optional.empty();
        try {
            Connection conn = DatabaseConfig.getConnection();
            String query = "SELECT * FROM MUSICA WHERE ID = ?";
            PreparedStatement stmt = conn.prepareStatement(query);
            stmt.setInt(1, id);
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                var _id = rs.getInt("ID");
                var titulo = rs.getString("TITULO");
                var duracao = rs.getInt("DURACAO");
                var artistaId = rs.getInt("ARTISTA_ID");
                musica = Optional.of(new Musica(_id, titulo, duracao, new Artista(artistaId, null)));
            }
            rs.close();
            stmt.close();
            conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return musica;
    }

    @Override
    public List<Musica> Listar() {
        var musicas = new ArrayList<Musica>();
        try {
            Connection conn = DatabaseConfig.getConnection();
            String query = "SELECT * FROM MUSICA ORDER BY ID";
            PreparedStatement stmt = conn.prepareStatement(query);
            ResultSet resultSet = stmt.executeQuery();
            while (resultSet.next()) {
                var id = resultSet.getInt("ID");
                var titulo = resultSet.getString("TITULO");
                var duracao = resultSet.getInt("DURACAO");
                var artistaId = resultSet.getInt("ARTISTA_ID");
                musicas.add(new Musica(id, titulo, duracao, new Artista(artistaId, null)));
            }
            resultSet.close();
            stmt.close();
            conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return musicas;
    }
}
