public class Main {
    public static void main(String[] args) {
        // criando uma conta
        var novaConta = new Conta();
        // coloca o nº da conta
        novaConta.numero = "0001";
        novaConta.sacar(100);
        System.out.println("Saldo atual: R$"+novaConta.exibirSaldo());
        novaConta.depositar(1000.0);
        System.out.println("Saldo atual: R$"+novaConta.exibirSaldo());
        novaConta.sacar(100);
        System.out.println("Saldo atual: R$"+novaConta.exibirSaldo());

        novaConta.depositar(1578);

        System.out.println("Extrato Bancario: "+novaConta.apresentarExtrato());

        System.out.println("Sistema Bancario Encerrando");
    }
}