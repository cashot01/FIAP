public class Main {
    public static void main(String[] args) {
        // criando uma conta
        var novaConta = new Conta();
        novaConta.numero = "0001";
        System.out.println("o numero da conta é: "+ novaConta.numero);
        // novaConta.sacar(100);
        System.out.println("Saldo atual: R$"+ novaConta.exibirSaldo());
        novaConta.depositar(1000.0);
        System.out.println("Saldo atual: R$"+novaConta.exibirSaldo());
        novaConta.sacar(100);
        System.out.println("Saldo atual: R$"+novaConta.exibirSaldo());
        System.out.println("Sistema Bancario Encerrando");
    }
}