package bgg;

import java.util.List;

public class BoardGame {
    private String name;
    private int yearlaunched;
    private int minPlayers;
    private int maxPlayers;
    private int bestNumPlayers;
    private int meanPlayTime;
    private int minAge;
    private double meanRating;
    private List<Rating> ratings;

    public BoardGame() {

    }

    public BoardGame(String name, int yearlaunched, int minPlayers, int maxPlayers,
                     int bestNumPlayers, int meanPlayTime, int minAge, List<Rating> ratings) {
        this.name = name;
        this.yearlaunched = yearlaunched;
        this.minPlayers = minPlayers;
        this.maxPlayers = maxPlayers;
        this.bestNumPlayers = bestNumPlayers;
        this.meanPlayTime = meanPlayTime;
        this.minAge = minAge;
        this.ratings = ratings;
        this.meanRating = calculateMeanRating();
    }

    private double calculateMeanRating() {
        return 0;
    }
}
