public class Conta {
    public String numero;

    private double saldo = 0.00;

    public void exibirSaldo(){
        System.out.println("o saldo da conta é: "+ saldo);
    }

    public void depositar(double valor){
        saldo += valor;
    }

    public void sacar(double valor){
        saldo -= valor;
    }

}
