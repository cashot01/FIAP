package org.example.repositorios;

import org.example.entidades.Artista;
import org.example.infraestrutura.DatabaseConfig;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class ArtistaRepositorio implements _CrudRepositorio<Artista> {
    @Override
    public void Cadastrar(Artista entidade) {
        try {
            Connection conn = DatabaseConfig.getConnection();
            String query = "INSERT INTO ARTISTA (ID, NOME) VALUES(DEFAULT, ?)";
            PreparedStatement stmt = conn.prepareStatement(query);
            stmt.setString(1, entidade.getNome());
            stmt.executeUpdate();
            stmt.close();
            conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void Atualizar(Artista entidade, int id) {
        try {
            Connection conn = DatabaseConfig.getConnection();
            String query = "UPDATE ARTISTA SET NOME = ? WHERE ID = ?";
            PreparedStatement stmt = conn.prepareStatement(query);
            stmt.setString(1, entidade.getNome());
            stmt.setInt(2, id);
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
            String query = "DELETE FROM ARTISTA WHERE ID = ?";
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
    public Optional<Artista> BuscarPorId(int id) {
        Optional<Artista> artista = Optional.empty();
        try {
            Connection conn = DatabaseConfig.getConnection();
            String query = "SELECT * FROM ARTISTA WHERE ID = ?";
            PreparedStatement stmt = conn.prepareStatement(query);
            stmt.setInt(1, id);
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                var _id = rs.getInt("ID");
                var nome = rs.getString("NOME");
                artista = Optional.of(new Artista(_id, nome));
            }
            rs.close();
            stmt.close();
            conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return artista;
    }

    public List<Artista> BuscarPorNome(String name) {
        var artistas = new ArrayList<Artista>();
        try {
            Connection conn = DatabaseConfig.getConnection();
            String query = "SELECT * FROM ARTISTA WHERE NOME LIKE ? ORDER BY ID";
            PreparedStatement stmt = conn.prepareStatement(query);
            stmt.setString(1, "%" + name + "%");
            ResultSet resultSet = stmt.executeQuery();
            while (resultSet.next()) {
                var id = resultSet.getInt("ID");
                var nome = resultSet.getString("NOME");
                artistas.add(new Artista(id, nome));
            }
            resultSet.close();
            stmt.close();
            conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return artistas;
    }

    @Override
    public List<Artista> Listar() {
        var artistas = new ArrayList<Artista>();
        try {
            Connection conn = DatabaseConfig.getConnection();
            String query = "SELECT * FROM ARTISTA ORDER BY ID";
            PreparedStatement stmt = conn.prepareStatement(query);
            ResultSet resultSet = stmt.executeQuery();
            while (resultSet.next()) {
                var id = resultSet.getInt("ID");
                var nome = resultSet.getString("NOME");
                artistas.add(new Artista(id, nome));
            }
            resultSet.close();
            stmt.close();
            conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return artistas;
    }
}
