public class Conta {
    // propriedades
    public String numero; // nº de conta não tem calculo, por isso string

    private double saldo = 0.00;

    private boolean chequeEspecialHabilitado = false;

    // métodos

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
        // 2 barras em pé (||) - ou
        // 2 E comercial (&&) - and
        else if (saldo < valor || saldo == 0){
            System.out.println("VC tá LISO!!!!");
        }
        else {
            saldo -= valor;
        }

    }

}
