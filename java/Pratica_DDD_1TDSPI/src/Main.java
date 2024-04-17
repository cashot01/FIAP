import bgg.Boardgame;
import bgg.Rating;

import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        var boardgame = new Boardgame("Catan", 1995, 3,4,
                4,60,4, new ArrayList<>(Arrays.asList(
                new Rating("user1", 8, "good game"),
                new Rating("user2", 5, "nice game"),
                new Rating("user3", 1, "bad game, its a piece of shit"),
                new Rating("user4", 5, "It's ok")
        )));

        // tirar a media das avaliações
        System.out.println(boardgame.getRatings()
                .stream()
                .mapToDouble(Rating::getRating)
                .average()
                .orElse(0));

        // remover palavrões dos comentários
        boardgame.getRatings().stream()
                .map(rating -> rating.getComment()
                        .replace("shit", "%#$%#")).forEach(System.out::println);

        //avaliações com mais de 5
        boardgame.getRatings().stream().filter(nota -> nota.getRating() > 5).forEach(System.out::println);

        //contar as avaliações que tiveram nota 5
        System.out.println(boardgame.getRatings().stream().filter(nota -> nota.getRating() == 5).count());
    }
}