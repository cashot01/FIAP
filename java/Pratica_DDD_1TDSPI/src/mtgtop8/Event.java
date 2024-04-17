package mtgtop8;

import java.time.LocalDateTime;
import java.util.List;

public class Event {
    private String name;
    private String format;
    private LocalDateTime data;
    private List<TournamentPlayer> players;
    private int rating;
    private String location;

    public Event() {
    }

    public Event(String name, String format, LocalDateTime data, List<TournamentPlayer> players, int rating, String location) {
        this.name = name;
        this.format = format;
        this.data = data;
        this.players = players;
        this.rating = rating;
        this.location = location;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }

    public LocalDateTime getData() {
        return data;
    }

    public void setData(LocalDateTime data) {
        this.data = data;
    }

    public List<TournamentPlayer> getPlayers() {
        return players;
    }

    public void setPlayers(List<TournamentPlayer> players) {
        this.players = players;
    }

    public int getRating() {
        return rating;
    }

    public void setRating(int rating) {
        this.rating = rating;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    @Override
    public String toString() {
        return "Event{" +
                "name='" + name + '\'' +
                ", format='" + format + '\'' +
                ", data=" + data +
                ", players=" + players +
                ", rating=" + rating +
                ", location='" + location + '\'' +
                '}';
    }
}
