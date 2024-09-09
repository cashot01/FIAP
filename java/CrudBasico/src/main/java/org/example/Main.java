package org.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        System.out.println("Fazendo insert no oracle");

        var URL = "jdbc:oracle:thin:@oracle.fiap.com.br:1521:ORCL";
        var USER = "RM555466";
        var PASSWORD = "071105";

        try{
            var conn = DriverManager.getConnection(URL, USER, PASSWORD);
            var query =
                    "INSERT INTO PRODUTOS (ID, NOME, PRECO) VALUES (DEFAULT, 'Coca-cola', 5.0)";
            var stmt = conn.createStatement();
            stmt.executeUpdate(query);
            stmt.close();
        }
        catch (SQLException e){
            e.printStackTrace();
        }

        }
    }
