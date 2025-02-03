package org.example.servicos;

public class ValidadorEntidades {
    public static boolean PalavraValida(String palavra){
        if (palavra == null || palavra.trim().isEmpty()){
            System.out.println("Palavra Vazia");
        }
        return true;
    }
    public static boolean NumeroValido(int numero){
        if(numero < 0){
            System.out.println("Numero Negativo");
            return false;
        }
        return true;
    }
}
