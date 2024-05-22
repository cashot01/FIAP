import java.util.List;
public class Main {
    public static void main(String[] args) {
        var cursoJava = new Curso(
                "Learn Java",
                "Popular for its versatility and ability to create a wide variety of applications, learning Java opens up your possibilities when coding. With it, you’ll be able to develop large systems, software, and mobile applications — and even create mobile apps for Android. Learn important Java coding fundamentals and practice your new skills with real-world projects."
                ,16,
                List.of(
                        new Avaliacao("Leonardo", 5, "Muito bom"),
                        new Avaliacao("Rafael",4, "Bom")
                )

        );
        cursoJava.exibirDetalhes();
    }
}