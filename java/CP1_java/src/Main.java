import models.Caminhao;
import models.Carro;
import models.Frota;
import models.Veiculo;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    private static final Scanner scanner = new Scanner(System.in);

    private static List<Frota> frotas = new ArrayList<>();
    private  static List<Veiculo> veiculos = new ArrayList<>();

    public static void main(String[] args) {
        System.out.println("Sistema Iniciando!");

        Menu();

        System.out.println("Sistema Finalizado!");
    }

    public static void  cadastroBasico(Veiculo veiculo){
        System.out.println("Digite a marca do carro: ");
        veiculo.setMarca(scanner.nextLine()); // set é semelhante ao =, mas é um método
        System.out.println("Digite o modelo do carro: ");
        veiculo.setModelo(scanner.nextLine());
        System.out.println("Digite o ano do carro: ");
        veiculo.setAno(scanner.nextInt());
        scanner.nextLine();
        System.out.println("Digite o consumo do carro: ");
        veiculo.setConsumoPorKm(scanner.nextDouble());
        scanner.nextLine();

    }

    public static Carro cadastrarCarro(){
        var carro = new Carro();
        cadastroBasico(carro);
        return carro;
    }

    public static Caminhao cadastrarCaminhao() {
        var caminhao = new Caminhao();
        cadastroBasico(caminhao);
        System.out.println("digite a quantidade de eixos: ");
        caminhao.setEixos(scanner.nextInt());

    }

    public static void Menu(){
        var carro = new Carro();
        System.out.println("Bem vindo ao sistema de controle de Frotas!");

        while (true) {
            System.out.println("Digite a opção desejada: ");
            System.out.println("1 - Cadastrar Frota");
            System.out.println("2 - Cadastrar caminhão");
            System.out.println("3 - Abastecer veiculo");
            System.out.println("4 - Dirigir veiculo");
            System.out.println("5 - Previsão de autonomia");
            System.out.println("6 - Sair");
            int opcao = scanner.nextInt();
            scanner.nextLine();

            switch (opcao){
                case 1:
                    CadastrarFrota();
                    break;
                case 2:
                    CadastrarVeiculos();
                    break;
            }
        }
    }

    public static void CadastrarFrota(){
        System.out.println("Digite o nome da Frota: ");
        var nome = scanner.nextLine();
        frotas.add(new Frota(nome,  new ArrayList<>()));
        System.out.println("\\u001B[32m"+"Frota adicionada com sucesso");
    }

    public static void CadastrarVeiculos() {
        System.out.println("digite o numero da frota que deseja adicionar o veiculo");
    }
}