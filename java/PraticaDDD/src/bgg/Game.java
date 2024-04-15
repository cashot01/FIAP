package bgg;

import java.util.List;

public abstract class Game{
    private String name;
    private int yearlaunched;
    private int minPlayers;
    private int maxPlayers;
    private int bestNumPlayers;
    private int meanPlayTime;
    private int minAge;
    private double meanRating;
    private List<Rating> ratings;

    public Game(String name, int yearlaunched, int minPlayers, int maxPlayers,
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

    public Game() {

    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    private double calculateMeanRating() {
        return ratings.stream()
                .mapToDouble(Rating::getRating)
                .average()
                .orElse(0);
    }

    @Override
    public String toString() {
        return "Game{" +
                "name='" + name + '\'' +
                ", yearlaunched=" + yearlaunched +
                ", minPlayers=" + minPlayers +
                ", maxPlayers=" + maxPlayers +
                ", bestNumPlayers=" + bestNumPlayers +
                ", meanPlayTime=" + meanPlayTime +
                ", minAge=" + minAge +
                ", meanRating=" + meanRating +
                ", ratings=" + ratings +
                '}';
    }
}
