public class Modulo extends Curso {
    public String tituloModulo;
    public double duracaoModulo;

    public Modulo() {
    }

    public Modulo(String tituloModulo, double duracaoModulo) {
        this.tituloModulo = tituloModulo;
        this.duracaoModulo = duracaoModulo;
    }

    public String getTituloModulo() {
        return tituloModulo;
    }

    public void setTituloModulo(String tituloModulo) {
        this.tituloModulo = tituloModulo;
    }

    public double getDuracaoModulo() {
        return duracaoModulo;
    }

    public void setDuracaoModulo(double duracaoModulo) {
        this.duracaoModulo = duracaoModulo;
    }

    @Override
    public String toString() {
        return "Modulo{" +
                "tituloModulo='" + tituloModulo + '\'' +
                ", duracaoModulo=" + duracaoModulo +
                "} " + super.toString();
    }
    public void exibirDetalhes(){
        System.out.println(this);
    }
}
