package models;

import java.time.LocalDateTime;

public class Veiculo {
    protected String marca;

    protected int ano;

    protected double consumoPorKm;

    protected String modelo;

    protected double quilometragem;

    protected double combustivelNoTanque;
    // protected  - serve para usar em outras classes, nos "filhos"

    public Veiculo(){

    }

    public Veiculo(String marca, int ano, double consumoPorKm, String modelo) {
        this.marca = marca;
        this.ano = ano;
        this.consumoPorKm = consumoPorKm;
        this.modelo = modelo;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        // || - ou
        if(ano < 1886 || ano > LocalDateTime.now().getYear()){
            System.out.println("o carrro não pode ser mais antigo que 1886 ou mais novo que o ano atual");
        }
        this.ano = ano;
    }

    public double getConsumoPorKm() {
        return consumoPorKm;
    }

    public void setConsumoPorKm(double consumoPorKm) {
        this.consumoPorKm = consumoPorKm;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public double getQuilometragem() {
        return quilometragem;
    }

    @Override
    public String toString() {
        return "Veiculo{" +
                "marca='" + marca + '\'' +
                ", ano=" + ano +
                ", consumoPorKm=" + consumoPorKm +
                ", modelo='" + modelo + '\'' +
                ", combustivelNoTanque=" + combustivelNoTanque +
                ", quilometragem=" + quilometragem +
                '}';
    }

    public void setQuilometragem(double quilometragem) {
        this.quilometragem = quilometragem;
    }

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
