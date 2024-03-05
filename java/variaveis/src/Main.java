import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("aplicação iniciando");
        var scanner = new Scanner(System.in);
        System.out.println("digite o n1: ");
        var n1 = scanner.nextInt();
        scanner.nextLine();
        System.out.println("digite n2: ");
        var n2 = scanner.nextInt();
        scanner.nextLine();

        System.out.println("a soma dos numeros é: " + (n1 + n2));

        /* int numero = 0 ;
        // comentario
        // sout - atalho do println
        System.out.println("o nº da variavel é " + numero);
        numero = (int) 20.5; // converte para inteiro, mas pode perder informações


        double numDecimal = numero + numero + 0.6 + 0.7;
        System.out.println(numDecimal);

        boolean maiordeIdade = false;
        int idade = 17;
        if (idade >= 18){
            maiordeIdade = true;
        }
        System.out.println("maior de idade? " + maiordeIdade);
        */
       // var numero = 0;
       // var numero2 = 12.3;
    }
}