public class Main {
    public static void main(String[] args) {
        var novaConta = new Conta();
        novaConta.numero = "0001";
        System.out.println("o numero da conta é: "+ novaConta.numero);
        novaConta.depositar(10.0);
        novaConta.exibirSaldo();
    }
}