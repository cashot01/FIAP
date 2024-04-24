import lego.Avaliacao;
import lego.Produto;

import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {

    }

    public static void legoTeste(){
        var newLego = new Produto();
        newLego.setNome("TIE Interceptor");
        newLego.setTema("Star Wars");
        newLego.setDescricao("eeste");
        newLego.setIdade(18);
        newLego.setId_produto("75382");
        new ArrayList<>(Arrays.asList(
                new Avaliacao(8, "brinquedo bom", "user1" ),
                new Avaliacao(6, "mais ou menos", "user2")
        ));


    }
}