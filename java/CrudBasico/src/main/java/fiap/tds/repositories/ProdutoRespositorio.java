package fiap.tds.repositories;

import fiap.tds.entities.Produto;
import fiap.tds.infrastructure.DatabaseConfig;

import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class ProdutoRespositorio implements _CrudRepositorio<Produto> {

    @Override
    public void Insert(Produto produto){
        try{
            // 1- Registrar o driver, e fazer a conexão
            var conn = DatabaseConfig.getConnection();
            // 2 - Criar o statement e definir a query
            var query =
                    "INSERT INTO PRODUTOS (ID,NOME, PRECO) VALUES (DEFAULT,?,?)";
            var stmt = conn.prepareStatement(query);
            // 2.1 - Setar os valores, substituindo os ? da query
            // eu nao posso só concatenar a query com os valores, pois isso pode ser um risco de segurança
            // por causa do SQL Injection
            stmt.setString(1, produto.getNome());
            stmt.setDouble(2, produto.getPreco());
            // 3 - Executar a query
            stmt.executeUpdate();
            // 4 - Fechar o statement
            stmt.close();
            // 5 - Fechar a conexão
            conn.close();
        }
        catch (SQLException e){
            e.printStackTrace();
        }
    }

    @Override
    public void Update(Produto entity) {

    }

    @Override
    public void Delete(int id) {

    }

    @Override
    public Produto GetById(int id) {
        return null;
    }

    @Override
    public List<Produto> GetAll() {
        var produtos = new ArrayList<Produto>();
        try{
            // 1 - registrar o driver, fazer a conexão
            var conn = DatabaseConfig.getConnection();
            // 2 - criar o statement e definir a querry
            var query = "SELECT * FROM PRODUTOS ORDER BY ID";
            var stmt = conn.prepareStatement(query);
            // 3 - executar a query
            var rs = stmt.executeQuery();
            // 4 - iterar sobre o resultado
            while (rs.next()){
                var id = rs.getInt("ID");
                var nome = rs.getString("NOME");
                var preco = rs.getDouble("PRECO");
                produtos.add(new Produto(id, nome, preco));
            }
            // 5 - fechar o resultset
            rs.close();
            // 6 - fechar o sattement
            stmt.close();
            // 7 - fechar conexão
            conn.close();
        }
        catch (SQLException e){
            e.printStackTrace();
        }

        return produtos;
    }

}
