package br.com.fiap.epictaskg.poder;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PoderService {

    private final PoderRepository poderRepository;

    public PoderService(PoderRepository poderRepository) {
        this.poderRepository = poderRepository;
    }

    public List<Poder> getAllPoderes(){
        return  poderRepository.findAll();
    }
}
