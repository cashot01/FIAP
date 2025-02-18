package com.example;

public class Computador extends Jogador {

    @Override // Avisa ao compilador que a intenção é sobrescrever o método
    public boolean parou() {
        return this.getPontos() > 16;
    }

}