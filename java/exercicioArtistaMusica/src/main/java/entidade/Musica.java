package entidade;

import java.util.Date;

public class Musica {
    private int id;
    private String nomeMusica;
    private  float duracao;
    private Date dataLancamento;

    public Musica() {
    }

    public Musica(int id, String nomeMusica, float duracao, Date dataLancamento) {
        this.id = id;
        this.nomeMusica = nomeMusica;
        this.duracao = duracao;
        this.dataLancamento = dataLancamento;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNomeMusica() {
        return nomeMusica;
    }

    public void setNomeMusica(String nomeMusica) {
        this.nomeMusica = nomeMusica;
    }

    public float getDuracao() {
        return duracao;
    }

    public void setDuracao(float duracao) {
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
                "id=" + id +
                ", nomeMusica='" + nomeMusica + '\'' +
                ", duracao=" + duracao +
                ", dataLancamento=" + dataLancamento +
                '}';
    }
}
