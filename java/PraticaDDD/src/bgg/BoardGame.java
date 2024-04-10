package bgg;

import java.util.List;

public class BoardGame {


    public BoardGame() {

    }



    private double calculateMeanRating() {
        return ratings.stream()
                .mapToDouble(Rating::getRating)
                .average()
                .orElse(0);
    }
}
