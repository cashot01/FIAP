package beans;

public class Debito extends Cartao {
    private double consignado;

    public Debito(String banco, String bandeira, String nome, String cor, String validade, int numero, int cvv, double saldo, double compra, double consignado) {
        super(banco, bandeira, nome, cor, validade, numero, cvv, saldo, compra);
        this.consignado = consignado;
    }

    public double getConsignado() {
        return consignado;
    }

    public void setConsignado(double consignado) {
        this.consignado = consignado;
    }
}
