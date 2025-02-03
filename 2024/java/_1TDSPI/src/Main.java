import _2_Classe_de_Entidade.Album;
import _2_Classe_de_Entidade.Musica;

public class Main {
    public static void main(String[] args) {

       }
       public void ExecutarAula2(){
           var album = new Album();
           album.nome = "Led Zeppelin IV";
           album.artista = "Led Zeppelin";
           album.anoDeLancamento = 1971;


           var musica1 = new Musica();
           musica1.nome = "Black Dog";
           musica1.artista = "Led Zeppelin";
           musica1.duracao = 294;

           var musica2 = new Musica();
           musica2.nome = "Rock and Rool";
           musica2.artista = "Led Zeppelin";
           musica2.duracao = 220;

           System.out.println("nº de faixas " + album.apresentarQuantidadeDeFaixas());
           album.adicionaMusica(musica1);
           System.out.println("duração total "+ album.apresentarDuracaoTotalMinutos());
           album.adicionaMusica(musica2);
           System.out.println("nº de faixas " + album.apresentarQuantidadeDeFaixas());
           System.out.println("duração total "+ album.apresentarDuracaoTotalMinutos());

       }
}