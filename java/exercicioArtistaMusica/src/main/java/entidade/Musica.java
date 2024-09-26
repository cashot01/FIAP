package entidade;

import java.time.LocalDate;
import java.util.Date;

public class Musica {
    private int id;
    private String nomeMusica;
    private  float duracao;
    private LocalDate dataLancamento;

    public Musica() {
    }

    public Musica(int id, String nomeMusica, float duracao, LocalDate dataLancamento) {
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

    public LocalDate getDataLancamento() {
        return dataLancamento;
    }

    public void setDataLancamento(LocalDate dataLancamento) {
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
