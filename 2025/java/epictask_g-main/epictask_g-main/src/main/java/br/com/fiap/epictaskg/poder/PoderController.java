package br.com.fiap.epictaskg.poder; 

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/poder")
public class PoderController {

    private final PoderService poderService;

    public PoderController(PoderService poderService) {
        this.poderService = poderService;
    }

    @GetMapping
    public String index(Model model){
        var poderes = poderService.getAllPoderes();
        model.addAttribute("poderes", poderes);
        return "index";
    }
}
