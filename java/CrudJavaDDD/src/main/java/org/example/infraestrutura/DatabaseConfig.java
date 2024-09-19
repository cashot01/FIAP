package org.example.infraestrutura;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConfig {
    private static String URL = "jdbc:oracle:thin:@oracle.fiap.com.br:1521:ORCL";
    private static String USER = "RM557884";
    private static String PASSWORD = "210506";

    public DatabaseConfig() {

    }

    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(URL, USER, PASSWORD);
    }
}
