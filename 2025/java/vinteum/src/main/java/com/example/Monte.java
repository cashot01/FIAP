package com.example;

import java.util.ArrayList;
import java.util.List;

public class Monte {

    private List<Carta> cartas = new ArrayList<>();

    public Monte(){
        for(int numero = 0; numero <= 13; numero++){
            for (Naipe naipe : Naipe.values()){
                cartas.add( new Carta(numero, naipe));
            }
        }
    }

}
