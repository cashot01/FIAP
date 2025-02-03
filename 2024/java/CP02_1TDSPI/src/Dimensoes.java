public class Dimensoes {
    private double altura;
    private double largura;
    private double profundidate;

    public Dimensoes() {
    }

    public Dimensoes(double altura, double largura, double profundidate) {
        this.altura = altura;
        this.largura = largura;
        this.profundidate = profundidate;
    }

    public double getAltura() {
        return altura;
    }

    public void setAltura(double altura) {
        this.altura = altura;
    }

    public double getLargura() {
        return largura;
    }

    public void setLargura(double largura) {
        this.largura = largura;
    }

    public double getProfundidate() {
        return profundidate;
    }

    public void setProfundidate(double profundidate) {
        this.profundidate = profundidate;
    }

    @Override
    public String toString() {
        return "Dimensoes{" +
                "altura=" + altura +
                ", largura=" + largura +
                ", profundidate=" + profundidate +
                '}';
    }
}
