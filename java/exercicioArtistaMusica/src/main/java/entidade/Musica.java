package entidade;

import java.util.Date;

public class Musica {
    private int id;
    private String nomeMusica;
    private  double duracao;
    private Date dataLancamento;

    public Musica() {
    }

    public Musica(int id, String nomeMusica, double duracao, Date dataLancamento) {
        super(id);
        this.nomeMusica = nomeMusica;
        this.duracao = duracao;
        this.dataLancamento = dataLancamento;
    }

    public String getNomeMusica() {
        return nomeMusica;
    }

    public void setNomeMusica(String nomeMusica) {
        this.nomeMusica = nomeMusica;
    }

    public double getDuracao() {
        return duracao;
    }

    public void setDuracao(double duracao) {
        this.duracao = duracao;
    }

    public Date getDataLancamento() {
        return dataLancamento;
    }

    public void setDataLancamento(Date dataLancamento) {
        this.dataLancamento = dataLancamento;
    }

    @Override
    public String toString() {
        return "Musica{" +
                "nomeMusica='" + nomeMusica + '\'' +
                ", duracao=" + duracao +
                ", dataLancamento=" + dataLancamento +
                "} " + super.toString();
    }
}
