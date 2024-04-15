import bgg.BoardGame;

import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        var jogosSerieProjectL = new ArrayList<BoardGame>();
        var jogoPrincipal = new BoardGame("Project L", 2020,
                1, 4, 3, 45,
                8, new ArrayList<>());
        var primeiraExpansao = new BoardGame("Project L: Finesse",
                2021, 1, 4, 3,
                45, 8, new ArrayList<>());
        var segundaExpansao = new BoardGame("Project L: Research",
                2021, 1, 4, 3,
                45, 8, new ArrayList<>());

        jogosSerieProjectL.add(jogoPrincipal);
        jogosSerieProjectL.add(primeiraExpansao);
        jogosSerieProjectL.add(segundaExpansao);

        //apresentar só as expansões
        System.out.println("Expansões da serie Project L: " +
               // jogosSerieProjectL.subList(1, jogosSerieProjectL.size()));
                Arrays.toString(jogosSerieProjectL.stream().filter(jogo -> jogo.getName()
                        .contains("Project L:")).toArray()));
        // só apresentar a string de expansões

        jogosSerieProjectL
                // o stream() é um método de Listas que significa que vamos manipular os elementos da lista
                .stream()
                // o filter é um método que filtra os elementos da lista
                // o parametro jogo -> jogo é uma função lambda que recebe o item da lista e retorna um booleano
                // neste caso, estamos filtrando os jogos que contém ":" no nome
                .filter(jogo -> jogo.getName()
                        // o contains é um método que verifica se a string contém outra string
                        .contains(":"))
                // o map é um método que transforma os elementos da lista em outros elementos
                // no caso, estamos transformando os jogos em uma lista de strings
                .map(boardgame -> boardgame
                        .getName()
                        // o split é um método que divide uma string em partes
                        .split(":")[1])
                // o forEach é um método que executa uma ação para cada elemento da lista
                .toList()
                .forEach(System.out::println);
    }
}