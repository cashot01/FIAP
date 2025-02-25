package br.com.fiap.cash_up_api.controller;


import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController // component
public class CategoryController {

    // listar todas as categorias
    // GET :8080/categories -> json
    @RequestMapping(method = {RequestMethod.GET}, path = "/categories", produces = "application/json")
    public String index(){
        return "Listar todas as categorias";
    }
}
