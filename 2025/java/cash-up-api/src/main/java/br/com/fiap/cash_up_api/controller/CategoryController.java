package br.com.fiap.cash_up_api.controller;


import br.com.fiap.cash_up_api.model.Category;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController // component
public class CategoryController {

    private List<Category> repository = new ArrayList<>();

    // listar todas as categorias
    // GET :8080/categories -> json
    @GetMapping("/categories")
    public List<Category> index(){
        return repository;
    }

    // cadastrar categoria
    @PostMapping("/categories")
    // @ResponseStatus(code = HttpStatus.CREATED)
    public ResponseEntity<Category> create(@RequestBody Category category){
        System.out.println("Cadastrando Categoria " + category.getName());
        repository.add(category);
        return ResponseEntity.status(201).body(category);
    }

    // retornar uma categoria
    @GetMapping("/categories/{id}")
    public ResponseEntity<Category> get(@PathVariable Long id){
        System.out.println("Buscando categoria " + id);
        var category = repository.stream()
            .filter(c -> c.getId().equals(id))
            .findFirst();

        if(category.isEmpty()){
            // return ResponseEntity.status(404).build();
            return ResponseEntity.notFound().build();
        }

        //return ResponseEntity.status(200).body(category.get());
        return ResponseEntity.ok(category.get());
        // nunca chamar o get , sem antes verificar se tem algo 
    }

    // apagar categoria
}
