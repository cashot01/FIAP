// importar biblioteca do log4j
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static Logger logger = LogManager.getLogger(Main.class);
    public static void main(String[] args){
        //var logger = LogManager.getLogManager();
        //logger.getLogger("").info("teste");

        try{
            var conteudo = "Esse é o conteúdo que será exportado para o arquivo txt";
            var arquivo = new File("arquivo.txt");

            // Criar o Processo de Escrita no Arquivo

            try(var writer = new FileWriter(arquivo)){
                writer.write(conteudo);
                writer.flush();
            }
            catch (IOException e){
                logger.error("Erro ao escrever no arquivo: " + e.getMessage());
            }
        }
        catch (Exception e){
            // problema muito grave que irá fechar o sistema
            logger.fatal("Erro fatal: " + e.getMessage() + " - " + Arrays.toString(e.getStackTrace()));

        }
    }
}