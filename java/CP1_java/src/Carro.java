public class Carro {
    public String marca;

    public int ano;

    public double consumoPorKm;

    public String modelo;

    private double quilometragem = 0;

    private double combustivelNoTanque = 0;

    public double abastecer(double litros){
        combustivelNoTanque += litros;
        System.out.println("Tanque foi abastecido com: "+combustivelNoTanque +" l");
        return combustivelNoTanque;
    }
    public void dirigir(double quilometros){
        if (combustivelNoTanque < quilometros/consumoPorKm){
            System.out.println("Você tem que abastecer o tanque");
        }
        else {
            combustivelNoTanque -= quilometros/consumoPorKm;
            quilometragem += quilometros;
            System.out.println("O carro percorreu "+ quilometros +"Km");
        }
    }

    public void previsaoDeAutonomia(){
        double autonomia = quilometragem / combustivelNoTanque;
        System.out.println("Autonomia de: "+ autonomia+ " Km");
    }




}
