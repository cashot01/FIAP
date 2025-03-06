package br.com.fiap.cash_up_api.controller;


import br.com.fiap.cash_up_api.model.Category;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@RestController // component
public class CategoryController {
    
    private  final Logger log = LoggerFactory.getLogger(getClass());

    private List<Category> repository = new ArrayList<>();

    // listar todas as categorias
    // GET :8080/categories -> json
    @GetMapping("/categories")
    public List<Category> index(){
        log.info("Buscando todas as categorias");
        return repository;
    }

    // cadastrar categoria
    @PostMapping("/categories")
    // @ResponseStatus(code = HttpStatus.CREATED)
    public ResponseEntity<Category> create(@RequestBody Category category){
        log.info("Cadastrando categoria");
        repository.add(category);
        return ResponseEntity.status(201).body(category);
    }

    // retornar uma categoria
    @GetMapping("/categories/{id}")
    public ResponseEntity<Category> get(@PathVariable Long id){
        log.info("Buscando categoria " + id);
        var category = getCategory(id);

        if(category.isEmpty()){
            // return ResponseEntity.status(404).build();
            return ResponseEntity.notFound().build();
        }

        //return ResponseEntity.status(200).body(category.get());
        return ResponseEntity.ok(category.get());
        // nunca chamar o get , sem antes verificar se tem algo 
    }

    // apagar categoria
    @DeleteMapping("/categories/{id}")
    public ResponseEntity<Object> destroy(@PathVariable Long id){
        log.info("Apagando categoria " + id);
        var category = getCategory(id);

        if(category.isEmpty()){
            return ResponseEntity.notFound().build();
        }

        repository.remove(category.get());
        return ResponseEntity.noContent().build();

    }

    //editar categoria
    @PutMapping("/categories/{id}")
    public ResponseEntity<Category> update(@PathVariable Long id, @RequestBody Category category){
        log.info("Atualizando categoria " + id + " " + category);

        var categoryToUpdate = getCategory(id);

        if(categoryToUpdate.isEmpty()){
            return ResponseEntity.notFound().build();
        }

        repository.remove(categoryToUpdate.get());
        category.setId(id);
        repository.add(category);
        return ResponseEntity.ok(category);

    }

    private Optional<Category> getCategory(Long id) {
        return repository.stream()
                .filter(c -> c.getId().equals(id))
                .findFirst();
    }
}
