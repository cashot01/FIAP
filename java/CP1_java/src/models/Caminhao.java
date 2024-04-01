package models;

public class Caminhao extends Veiculo {
    // models.Veiculo é o pai de caminhão
    public static final double Capacidade_Por_Eixo = 15000;

    public static final double EIXOS_MAXIMOS = 9;
    private int eixos;

    private double capacidadeDeCarga;

    private double pesoTotal;

    public void adicionarUnidadeDeEixo(){
        if(eixos >= EIXOS_MAXIMOS){
            System.out.println("o caminhão ja atingiu a capacidade maxima dos eixos");
            return;
        }
        eixos++;
        capacidadeDeCarga = eixos * Capacidade_Por_Eixo;
        consumoPorKm = consumoPorKm + (consumoPorKm * 0.1);
    }

    public void removerUnidadeDeEixo(){
        if(eixos <= 0){
            System.out.println("caminhão nao possui eixos");
            return;
        }
        eixos--;
        capacidadeDeCarga = eixos * Capacidade_Por_Eixo;
        consumoPorKm = consumoPorKm - (consumoPorKm * 0.1);
    }

    public void carregar(double peso){
        if (peso + pesoTotal > capacidadeDeCarga){
            System.out.println("caminhão não suporta o peso informado");
            return;
        }
        pesoTotal += peso;
        consumoPorKm = consumoPorKm + (pesoTotal * 0.0001); // 0.01% de consumo a mais por kg
    }

}
