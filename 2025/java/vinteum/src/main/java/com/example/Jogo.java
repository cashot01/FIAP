package com.example;

public class Jogo {
    
    protected Monte monte = new Monte();
    protected Jogador jogador = new Jogador();
    protected Computador computador = new Computador();

    public Jogo(){
        monte.embaralhar();
    }

    public Carta distribuirCartaParaJogador(Jogador jogador){
        if (jogador.parou()) return null;
        var carta = monte.virar();
        jogador.receberCarta(carta);
        return carta;
    }

    public String resultado(){
        if(jogadorEstourou() && computadorEstourou() || jogador.getPontos() == computador.getPontos()){
            return "Empatou";
        }

        if( computadorEstourou() || (jogador.getPontos() > computador.getPontos() && !jogadorEstourou())){
            return "Você ganhou";
        }

        return "Você perdeu";

    }

    public boolean acabou(){
        return alguemEstourou() || jogador.parou() && computador.parou();
    }

    private boolean jogadorEstourou(){
        return jogador.getPontos() > 21;
    }

    private boolean computadorEstourou(){
        return computador.getPontos() > 21;
    }

    private boolean alguemEstourou(){
        return jogadorEstourou() || computadorEstourou();
    }

}
