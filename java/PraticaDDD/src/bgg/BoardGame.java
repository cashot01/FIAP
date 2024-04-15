package bgg;

import java.util.List;

public class BoardGame extends Game {

    public  BoardGame(String name, int yearlaunched, int minPlayers, int maxPlayers,
                      int bestNumPlayers, int meanPlayTime, int minAge, List<Rating> ratings){
        super(name, yearlaunched, minPlayers, maxPlayers, bestNumPlayers, meanPlayTime, minAge, ratings);
    }

    @Override
    public String toString() {
        return "BoardGame{} " + super.toString();
    }
}
