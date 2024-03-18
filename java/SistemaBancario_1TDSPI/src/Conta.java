import java.util.ArrayList;
import java.util.List;

public class Conta {
    // propriedades
    public String numero; // nº de conta não tem calculo, por isso string

    private double saldo = 0.00;

    private boolean chequeEspecialHabilitado = false;

    private List<String> historicoMovimentacao = new ArrayList<>();

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
        System.out.println("Deposito de: R$"+ valor + " com sucesso");
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
            System.out.println("Saque de: R$"+ valor);
        }

    }

}
