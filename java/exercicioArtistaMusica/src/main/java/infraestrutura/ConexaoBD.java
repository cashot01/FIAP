package infraestrutura;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class ConexaoBD {
    private static String URL = "jdbc:oracle:thin:@oracle.fiap.com.br:1521:ORCL";
    private static String USER = "RM555466";
    private static String PASSWORD = "071105";

    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(URL, USER, PASSWORD);
    }
}