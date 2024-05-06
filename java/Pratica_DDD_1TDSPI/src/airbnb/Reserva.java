package airbnb;

import java.time.LocalDateTime;
import java.util.List;

public class Reserva {
    private String codigo;
    private LocalDateTime dataInicio;
    private LocalDateTime dataFim;
    private double valorTotal;
    private String observacoes;
    private Hospede hospede;
    private List<Hospede> acompanhantes;
    private Imovel imovel;
}
