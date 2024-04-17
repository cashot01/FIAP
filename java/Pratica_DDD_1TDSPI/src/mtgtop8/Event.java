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
}
