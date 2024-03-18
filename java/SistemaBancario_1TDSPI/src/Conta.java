public class Conta {
    //propriedades
    public String numero; //0001 por ex, numero da conta não tem calculo, por isso pode ser string
    private double saldo = 0.0; //saldo da conta, pode ser decimal, por isso double
    private boolean chequeEspecialHabilitado = false; //cheque especial, pode ser true ou false, por isso boolean

    //métodos ou funções
    public void depositar(double valor){
        saldo += valor;
        System.out.println("Depósito de " + valor + " realizado com sucesso!");
    }

    public void sacar(double valor){
        // condição de cheque especial
        if(saldo < 0)
            System.out.println("Aviso! você está no cheque especial, " +
                    "por isso juros poderão ser cobriados");

        // condição de saque
        if(chequeEspecialHabilitado || saldo >= valor) {
            saldo -= valor;
            System.out.println("\u001B[32m"+"Saque de " + valor + " realizado com sucesso!"+"\u001B[0m");
        }
        else
            System.out.println("\u001B[33m"+ "Saldo insuficiente! você é um liso!!!!" + "\u001B[0m");
    }

    public double exibirSaldo(){
        return saldo;
    }

    public void habilitarChequeEspecial(){
        chequeEspecialHabilitado = true;
    }

    public void desabilitarChequeEspecial(){
        chequeEspecialHabilitado = false;
    }
}
