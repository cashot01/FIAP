public class Conta {
    // propriedades
    public String numero; // nº de conta não tem calculo, por isso string

    private double saldo = 0.00;

    private boolean chequeEspecialHabilitado = false;

    public double exibirSaldo(){
        return saldo;
    }

    // metodos

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
