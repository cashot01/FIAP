import bgg.Boardgame;
import bgg.Rating;
import mtgtop8.Event;
import mtgtop8.MTG_FORMAT;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        var newEvent = new Event();
        newEvent.setName("Pro Tour 25th Anniversary");
        newEvent.setFormat(MTG_FORMAT.PIONEER);
        newEvent.setRating(4);
        newEvent.setLocation("Minneapolis, MN");
        newEvent.setData(
                LocalDateTime.parse("2018-12-03T12:00:00"));

        }
        public static void bggTeste(){
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