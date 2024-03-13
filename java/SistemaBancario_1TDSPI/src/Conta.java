public class Conta {
    public String numero;

    private double saldo = 0.00;

    private boolean chequeEspecialHabilitado = false;

    public double exibirSaldo(){
        return saldo;
    }

    public boolean alterarStatusCheque(boolean status){
        chequeEspecialHabilitado = status;
        return chequeEspecialHabilitado;
    }

    public void depositar(double valor){
        saldo += valor;
    }

    public void sacar(double valor){
        if(chequeEspecialHabilitado){
            saldo -= valor;
        }
        else if (saldo < valor || saldo == 0){
            System.out.println("VC tá LISO!!!!");
        }
        else {
            saldo -= valor;
        }

    }

}
