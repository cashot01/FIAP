package br.com.fiap.cash_up_api.repository;

import br.com.fiap.cash_up_api.model.Transaction;
import org.springframework.data.jpa.repository.JpaRepository;

import java.time.LocalDate;
import java.util.List;

public interface TransactionRepository extends JpaRepository<Transaction, Long> {

    List<Transaction> findByDescriptionContainingIgnoringCase(String description); // Querry Methods

    List<Transaction> findByDescriptionContainingIgnoringCaseAndDate(String description, LocalDate date);

    List<Transaction> findByDate(LocalDate date);

}
