package br.com.fiap.cash_up_api.controller;

import java.util.ArrayList;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.server.ResponseStatusException;

import br.com.fiap.cash_up_api.model.Category;
import br.com.fiap.cash_up_api.repository.CategoryRepository;

@RestController // component
public class CategoryController {

    private final Logger log = LoggerFactory.getLogger(getClass());

    @Autowired // injeção de dependencia
    private CategoryRepository repository;

    @GetMapping("/categories")
    public List<Category> index() {
        log.info("Buscando todas categorias");
        return repository.findAll();
    }

    @PostMapping("/categories")
    public ResponseEntity<Category> create(@RequestBody Category category) {
        log.info("Cadastrando categoria " + category.getName());
        repository.save(category);
        // trocou o add pelo save
        return ResponseEntity.status(201).body(category);
    }

    @GetMapping("/categories/{id}")
    public ResponseEntity<Category> get(@PathVariable Long id) {
        log.info("Buscando categoria " + id);
        return ResponseEntity.ok(getCategory(id));
    }

    @DeleteMapping("/categories/{id}")
    public ResponseEntity<Object> destroy(@PathVariable Long id) {
        log.info("Apagando categoria " + id);
        repository.delete(getCategory(id));
        // trocou remove -> delete
        return ResponseEntity.noContent().build();
    }

    @PutMapping("/categories/{id}")
    public ResponseEntity<Category> update(@PathVariable Long id, @RequestBody Category category) {
        log.info("Atualizando categoria " + id + " " + category);

        getCategory(id);
        category.setId(id);
        repository.save(category);
        return ResponseEntity.ok(category);
    }

    private Category getCategory(Long id) {
        return repository.findById(id)
                .orElseThrow(
                        () -> new ResponseStatusException(
                                HttpStatus.NOT_FOUND,
                                "Categoria não encontrada"));
                // trocou o stream pelo findById
    }

}
