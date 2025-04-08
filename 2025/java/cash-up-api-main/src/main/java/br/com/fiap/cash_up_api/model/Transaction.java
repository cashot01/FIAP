package br.com.fiap.cash_up_api.model;

import jakarta.persistence.*;
import jakarta.validation.constraints.*;
import lombok.Builder;
import lombok.Data;

import java.math.BigDecimal;
import java.time.LocalDate;

@Entity
@Builder
@Data
public class Transaction {

    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @NotBlank(message = "campo obrigatório")
    @Size(min = 5, max = 255, message = "deve ter pelo menos 5 caracteres")
    private String description;

    @Positive(message = "deve ser maior que zero")
    private BigDecimal amount;

    @PastOrPresent(message = "não pode ser no futuro")
    private LocalDate date;

    @NotNull(message = "campo obrigatório")
    @Enumerated(EnumType.STRING)
    private TransactionType type;

    @NotNull(message = "campo obrigatório")
    @ManyToOne
    private Category category;
}
