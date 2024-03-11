package _2_Classe_de_Entidade;


// uma classe é um objeto, coisa, conceito do mundo real que será representado
// no sistema

import java.util.ArrayList;
import java.util.List;

public class Album {
    // atributos da classe , é tudo q um objeto tem ou é

    public String nome;

    public String artista;

    public int anoDeLancamento;

    private int duracaoTotal = 0;


    // atributo privado (private) que so pode ser acessado por esta classe
    // usamos privado quando ele vai ser um atributo calculado
    private int quantidadeFaixas;
    private List<Musica> musicas = new ArrayList<>();

    public void adicionaMusica(Musica musica){
        System.out.println("Adicionando a musica" + musica.nome + "ao album " + nome);
        musicas.add(musica);
        quantidadeFaixas++;
        duracaoTotal += musica.duracao;
        // ++ = +1
    }

    public void removerMusicas(Musica musica){
        musicas.remove(musica);
        quantidadeFaixas--;
        duracaoTotal -= musica.duracao;
        // -- = -1
    }

    public List<Musica> apresentarMusicasDoAlbum(){
        return musicas;
    }

    public int apresentarQuantidadeDeFaixas(){
        return quantidadeFaixas;
    }

    public int apresentarDuracaoTotal(){
        return duracaoTotal;
    }

    public String  apresentarDuracaoTotalMinutos(){
        int minutos = duracaoTotal / 60;
        int segundos = duracaoTotal % 60;
        return minutos + " min e " + segundos + " seg";
    }
}
