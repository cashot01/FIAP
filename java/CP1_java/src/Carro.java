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
        double combustivelNecessario = quilometros / consumoPorKm;
        if (combustivelNoTanque < combustivelNecessario){
            System.out.println("Você tem que abastecer o tanque");
        }
        else {
            combustivelNoTanque -= combustivelNecessario;
            quilometragem += quilometros;
            System.out.println("O carro percorreu "+ quilometros +"Km");
        }
    }

    public double previsaoDeAutonomia(){
        return  consumoPorKm * combustivelNoTanque;
    }




}
