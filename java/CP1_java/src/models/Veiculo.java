package models;

public class Veiculo {
    public String marca;

    public int ano;

    public double consumoPorKm;

    public String modelo;

    protected double combustivelNoTanque;
    // protected  - serve para usar em outras classes, nos "filhos"

    protected double quilometragem;

    public void abastecer(double litros){
        combustivelNoTanque += litros;
        System.out.println("Abastecendo " + litros + "litros no tanque.");
    }

    // Reduzir a quantidade de combustivel no tanque com base na distancia percorrida e no consumo por quilometro no carro.
    // Aumentar a quilometragem do veiculo.
    // Caso nao haja combustivel suficiente para a distancia desejada, o carro nao deve "dirigir" e deve imprimir uma mensagem indicando falta de combustivel
    public void dirigir(double distancia){
        double combustivelNecessario = distancia / consumoPorKm; // ex: 100km / 10km/l = 10 litros
        if (combustivelNoTanque >= combustivelNecessario){
            combustivelNoTanque -= combustivelNecessario;
            quilometragem += distancia;
            System.out.println("Dirigindo "+ distancia +"km");
        }
        else
            System.out.println("Combustivel insuficiente para dirigir "+ distancia +"km");
    }

    public double previsaoDeAutonomia(){
        return combustivelNoTanque * consumoPorKm;
    }
}
