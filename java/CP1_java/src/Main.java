import java.util.Scanner;

public class Main {
    private static final Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {

        var carro1 = cadastrarCarro();
       // carro1.ano = 2024;
       // carro1.marca = "Fiat";
       // carro1.modelo = "Argo";
       // carro1.consumoPorKm = 10;



        carro1.abastecer(100);
        carro1.dirigir(90);
        System.out.println(carro1.previsaoDeAutonomia());


    }

    public static Carro cadastrarCarro(){
        var carro1 = new Carro();
        System.out.println("Digite a marca do carro: ");
        carro1.marca = scanner.nextLine();
        System.out.println("Digite o modelo do carro: ");
        carro1.modelo = scanner.nextLine();
        System.out.println("Digite o ano do carro: ");
        carro1.ano = scanner.nextInt();
        scanner.nextLine();
        System.out.println("digite o consumo do carro: ");
        carro1.consumoPorKm = scanner.nextDouble();
        scanner.nextLine();
        return carro1;
    }
}