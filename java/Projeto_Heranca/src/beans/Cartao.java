package beans;

public class Cartao {
    private String banco;
    private String bandeira;
    private String nome;
    private  String cor;
    private String validade;
    private int numero;
    private int cvv;
    private double saldo;
    private double compra;

    public Cartao() {
    }

    public Cartao(String banco, String bandeira, String nome, String cor, String validade, int numero, int cvv, double saldo, double compra) {
        this.banco = banco;
        this.bandeira = bandeira;
        this.nome = nome;
        this.cor = cor;
        this.validade = validade;
        this.numero = numero;
        this.cvv = cvv;
        this.saldo = saldo;
        this.compra = compra;
    }

    public String getBanco() {
        return banco;
    }

    public void setBanco(String banco) {
        this.banco = banco;
    }

    public String getBandeira() {
        return bandeira;
    }

    public void setBandeira(String bandeira) {
        this.bandeira = bandeira;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    public String getValidade() {
        return validade;
    }

    public void setValidade(String validade) {
        this.validade = validade;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public int getCvv() {
        return cvv;
    }

    public void setCvv(int cvv) {
        this.cvv = cvv;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public double getCompra() {
        return compra;
    }

    public void setCompra(double compra) {
        this.compra = compra;
    }

    @Override
    public String toString() {
        return "Cartao{" +
                "banco='" + banco + '\'' +
                ", bandeira='" + bandeira + '\'' +
                ", nome='" + nome + '\'' +
                ", cor='" + cor + '\'' +
                ", validade='" + validade + '\'' +
                ", numero=" + numero +
                ", cvv=" + cvv +
                ", saldo=" + saldo +
                ", compra=" + compra +
                '}';
    }
}
