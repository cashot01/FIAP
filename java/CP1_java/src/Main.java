public class Main {
    public static void main(String[] args) {
        var carro1 = new Carro();

        carro1.ano = 2024;
        carro1.marca = "Fiat";
        carro1.modelo = "Argo";
        carro1.consumoPorKm = 10;
        carro1.abastecer(100);
        carro1.dirigir(100);
        carro1.previsaoDeAutonomia();


    }
}