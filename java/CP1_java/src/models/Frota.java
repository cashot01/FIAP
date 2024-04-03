package models;

import java.util.ArrayList;
import java.util.List;

public class Frota {
    // composição é tudo qua a classe tem - ex. Frota tem Veiculos
    private List<Veiculo> veiculos;
    public Frota() {
        veiculos = new ArrayList<>();
    }

    public Frota(List<Veiculo> veiculos) {
        this.veiculos = veiculos;
    }

    public List<Veiculo> getVeiculos() {
        return veiculos;
    }

    public void setVeiculos(List<Veiculo> veiculos) {
        this.veiculos = veiculos;
    }

    public void adicionarVeiculo(Veiculo veiculo){
        veiculos.add(veiculo);
    }


}
