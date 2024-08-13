package Entidades;

import java.time.LocalDateTime;

public class Cupom extends _EntidadeBase{
    private String codigo;
    private double desconto;
    private char tipoDesconto;
    private LocalDateTime validade;
    private int limiteUsos;

    public Cupom() {
    }

    public Cupom(int id, String codigo, double desconto, char tipoDesconto, LocalDateTime validade, int limiteUsos) {
        super(id);
        this.codigo = codigo;
        this.desconto = desconto;
        this.tipoDesconto = tipoDesconto;
        this.validade = validade;
        this.limiteUsos = limiteUsos;
    }

    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public double getDesconto() {
        return desconto;
    }

    public void setDesconto(double desconto) {
        this.desconto = desconto;
    }

    public char getTipoDesconto() {
        return tipoDesconto;
    }

    public void setTipoDesconto(char tipoDesconto) {
        this.tipoDesconto = tipoDesconto;
    }

    public LocalDateTime getValidade() {
        return validade;
    }

    public void setValidade(LocalDateTime validade) {
        this.validade = validade;
    }

    public int getLimiteUsos() {
        return limiteUsos;
    }

    public void setLimiteUsos(int limiteUsos) {
        this.limiteUsos = limiteUsos;
    }

    @Override
    public String toString() {
        return "Cupom{" +
                "codigo='" + codigo + '\'' +
                ", desconto=" + desconto +
                ", tipoDesconto=" + tipoDesconto +
                ", validade=" + validade +
                ", limiteUsos=" + limiteUsos +
                "} " + super.toString();
    }
}
