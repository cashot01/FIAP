import java.util.List;
public class Modulo extends Curso {
    private String tituloModulo;
    private double duracaoModulo;

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

    @Override
    public String toString() {
        return "Modulo{" +
                "tituloModulo='" + tituloModulo + '\'' +
                ", duracaoModulo=" + duracaoModulo +
                "} " + super.toString();
    }
    @Override
    public void exibirDetalhes(){
        System.out.println(this);
    }
}
